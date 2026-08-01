# -*- coding: utf-8 -*-
"""
可复用的数据预处理管道 (Reusable Data Preprocessing Pipeline)

包含:
- missing_report: 缺失值报告
- detect_outliers_iqr / detect_outliers_zscore: 异常值检测
- make_preprocessor: 数值+类别混合预处理(ColumnTransformer)
- make_full_pipeline: 预处理+模型一键组装
- split_data: 训练/测试集划分
- run_demo: 完整演示(直接运行本文件即可)

用法:
    from preprocessing_pipeline import make_preprocessor, make_full_pipeline, split_data
"""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split, cross_val_score


def missing_report(df):
    """缺失值报告: 返回每列缺失数量与比例"""
    missing = df.isna().sum()
    missing = missing[missing > 0]
    if missing.empty:
        return "没有缺失值"
    return pd.DataFrame({
        "缺失数": missing,
        "缺失比例%": (missing / len(df) * 100).round(2)
    })


def detect_outliers_iqr(df, columns, factor=1.5):
    """IQR 法检测异常值, 返回布尔掩码(True=异常)"""
    mask = pd.Series(False, index=df.index)
    for col in columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower, upper = q1 - factor * iqr, q3 + factor * iqr
        mask = mask | (df[col] < lower) | (df[col] > upper)
    return mask


def detect_outliers_zscore(df, columns, threshold=3):
    """Z-score 法检测异常值, |z| > threshold 视为异常"""
    mask = pd.Series(False, index=df.index)
    for col in columns:
        z = (df[col] - df[col].mean()) / df[col].std()
        mask = mask | (z.abs() > threshold)
    return mask


def make_preprocessor(numeric_features, categorical_features,
                      num_strategy="median", cat_strategy="most_frequent",
                      scaler="standard", handle_unknown="ignore"):
    """构建数值+类别混合预处理

    参数:
        numeric_features: 数值列名列表
        categorical_features: 类别列名列表
        num_strategy: 数值填充策略 mean/median/most_frequent/constant
        cat_strategy: 类别填充策略 most_frequent/constant
        scaler: standard / minmax / robust / None
        handle_unknown: 独热编码遇到未知类别时的处理

    返回:
        ColumnTransformer 预处理对象
    """
    if scaler == "standard":
        s = StandardScaler()
    elif scaler == "minmax":
        s = MinMaxScaler()
    elif scaler == "robust":
        s = RobustScaler()
    else:
        s = "passthrough"

    num_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy=num_strategy)),
        ("scaler", s),
    ])

    cat_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy=cat_strategy)),
        ("encoder", OneHotEncoder(handle_unknown=handle_unknown)),
    ])

    preprocessor = ColumnTransformer([
        ("num", num_pipe, numeric_features),
        ("cat", cat_pipe, categorical_features),
    ])
    return preprocessor


def make_full_pipeline(preprocessor, model):
    """预处理 + 模型 组装成一条完整管道"""
    return Pipeline([("preprocess", preprocessor), ("model", model)])


def split_data(df, target, test_size=0.2, random_state=42, stratify=True):
    """划分训练/测试集, 分类任务默认分层抽样"""
    X = df.drop(columns=[target])
    y = df[target]
    stratify_arg = y if stratify else None
    return train_test_split(X, y, test_size=test_size,
                            random_state=random_state, stratify=stratify_arg)


def run_demo():
    """完整演示: 模拟泰坦尼克风格数据跑通整个流程"""
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score

    rng = np.random.default_rng(42)
    n = 500
    df = pd.DataFrame({
        "age": rng.normal(35, 12, n).round(0),
        "fare": rng.lognormal(3, 0.8, n).round(2),
        "class": rng.choice(["First", "Second", "Third"], n, p=[0.2, 0.3, 0.5]),
        "embarked": rng.choice(["S", "C", "Q"], n, p=[0.6, 0.3, 0.1]),
        "survived": rng.integers(0, 2, n),
    })
    df.loc[rng.random(n) < 0.1, "age"] = np.nan
    df.loc[rng.random(n) < 0.05, "embarked"] = np.nan

    print("缺失值报告:")
    print(missing_report(df))
    print()

    num_cols = ["age", "fare"]
    cat_cols = ["class", "embarked"]

    print("异常值检测(IQR):", detect_outliers_iqr(df, num_cols).sum(), "行")
    print("异常值检测(Z-score):", detect_outliers_zscore(df, num_cols).sum(), "行")
    print()

    X_train, X_test, y_train, y_test = split_data(df, "survived")
    print("训练集:", X_train.shape, "测试集:", X_test.shape)
    print()

    for model in [
        LogisticRegression(max_iter=1000),
        RandomForestClassifier(n_estimators=100, random_state=42),
    ]:
        pipe = make_full_pipeline(make_preprocessor(num_cols, cat_cols), model)
        pipe.fit(X_train, y_train)
        acc = accuracy_score(y_test, pipe.predict(X_test))
        scores = cross_val_score(pipe, X_train, y_train, cv=5)
        print(f"{type(model).__name__}:")
        print(f"  测试集准确率 = {acc:.4f}")
        print(f"  5折交叉验证 = {scores.mean():.4f} +/- {scores.std():.4f}")
        print(f"  管道步骤 = {list(pipe.named_steps.keys())}")
        print()


if __name__ == "__main__":
    run_demo()
