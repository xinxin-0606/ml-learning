# Day 3 数据预处理与 Scikit-learn 管道 学习笔记

> 学习日期: 2026-08-01 | sklearn + pandas + numpy

## 目录

1. [为什么要做数据预处理](#1-为什么要做数据预处理)
2. [缺失值处理](#2-缺失值处理)
3. [异常值处理](#3-异常值处理)
4. [特征缩放](#4-特征缩放)
5. [类别编码](#5-类别编码)
6. [划分训练测试集](#6-划分训练测试集)
7. [sklearn Pipeline 管道](#7-sklearn-pipeline-管道)
8. [ColumnTransformer 混合处理](#8-columntransformer-混合处理)
9. [常见陷阱](#9-常见陷阱)

---

## 1. 为什么要做数据预处理

- 真实数据几乎都有问题：缺失、异常、量纲不同、非数值
- 模型对数据质量敏感，预处理直接影响效果
- 好的预处理 = 特征工程的基础

预处理四件套：

| 步骤 | 解决什么问题 |
|------|------------|
| 缺失值处理 | 数据有空缺 |
| 异常值处理 | 数据有离群点 |
| 特征缩放 | 不同特征量纲差异大 |
| 类别编码 | 数据是文本/类别 |

---

## 2. 缺失值处理

### 检测缺失

```python
df.isna().sum()          # 每列缺失数量
df.isnull().mean() * 100 # 缺失比例(%)
```

### 处理方式

| 方式 | 适用场景 | pandas 写法 |
|------|---------|-------------|
| 删除行 | 缺失很少 | df.dropna() |
| 常数填充 | 业务含义明确 | df.fillna(0) |
| 均值填充 | 数值型、分布较对称 | df.fillna(df.mean()) |
| 中位数填充 | 数值型、有异常值 | df.fillna(df.median()) |
| 众数填充 | 类别型 | df.fillna(df.mode()[0]) |
| 前向/后向填充 | 时间序列 | fillna(method='ffill') |

### sklearn 版（管道内使用）

```python
from sklearn.impute import SimpleImputer

# 数值列用中位数
num_imputer = SimpleImputer(strategy='median')
# 类别列用众数
cat_imputer = SimpleImputer(strategy='most_frequent')
# 策略: mean / median / most_frequent / constant
```

---

## 3. 异常值处理

### IQR 法（四分位距）

```python
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['col'] < lower) | (df['col'] > upper)]
```

### Z-score 法

```python
z = (df['col'] - df['col'].mean()) / df['col'].std()
outliers = df[abs(z) > 3]   # |z| > 3 视为异常
```

### 处理方法

- 删除（异常确实无意义）
- 截断到边界（winsorize）
- 替换为中位数（稳健）

---

## 4. 特征缩放

### 三种缩放器

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

ss = StandardScaler()   # 标准化: (x-mean)/std, 均值0方差1
mm = MinMaxScaler()     # 归一化: (x-min)/(max-min), 范围[0,1]
rs = RobustScaler()     # 稳健: 用中位数和IQR, 抗异常值
```

### 选择原则

| 场景 | 推荐 |
|------|------|
| 线性回归/逻辑回归/神经网络 | StandardScaler |
| 有边界的数据（像素、分数） | MinMaxScaler |
| 数据有大量异常值 | RobustScaler |
| 树模型（RF/GBDT） | 不需要缩放 |

### 为什么必须缩放

- 距离类模型（KNN/SVM/线性）对量纲敏感
- 例如: 年龄(0-100) 和 工资(0-100000)，工资会主导距离

---

## 5. 类别编码

```python
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

# 标签编码: 给类别编数字 0,1,2... (适合目标变量)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 独热编码: 每种类别一列 0/1 (适合特征)
ohe = OneHotEncoder(handle_unknown='ignore')
X_encoded = ohe.fit_transform(X_cat)

# 有序编码: 类别有顺序时
oe = OrdinalEncoder(categories=[['低','中','高']])
```

### 注意

- 独热编码后数据变稀疏，用稀疏矩阵存
- 特征类别很多时考虑保留 top-K 或目标编码
- pandas 的 get_dummies 适合探索，管道里用 OneHotEncoder

---

## 6. 划分训练测试集

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 测试集比例
    random_state=42,    # 固定随机种子保证可复现
    stratify=y          # 按类别比例分层抽样(分类任务推荐)
)
```

### 黄金法则

- 只用训练集 fit，测试集只能 transform
- 防止数据泄露（测试集信息流入训练）

---

## 7. sklearn Pipeline 管道

### 为什么用 Pipeline

- 把预处理+模型串成一条流水线
- 交叉验证/网格搜索时自动只对训练集 fit
- 防止数据泄露
- 部署时一个对象搞定全部

### 基本用法

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipe.fit(X_train, y_train)          # 依次 fit
pipe.predict(X_test)                # 依次 transform + predict
pipe.score(X_test, y_test)
```

### 网格搜索搭配管道

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'model__C': [0.1, 1, 10],       # 双下划线访问管道内步骤参数
    'model__penalty': ['l2']
}
grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(X_train, y_train)
```

---

## 8. ColumnTransformer 混合处理

不同类型列走不同预处理流程：

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

numeric_features = ['age', 'fare']
categorical_features = ['sex', 'embarked']

# 数值列: 中位数填充 + 标准化
num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# 类别列: 众数填充 + 独热编码
cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', num_pipe, numeric_features),
    ('cat', cat_pipe, categorical_features)
])

# 最终完整管道
full_pipe = Pipeline([
    ('preprocess', preprocessor),
    ('model', LogisticRegression())
])

full_pipe.fit(X_train, y_train)
```

### 完整可复用管道

见配套文件 `preprocessing_pipeline.py`，包含：

- `make_preprocessor()` 构建数值+类别混合预处理
- `make_full_pipeline()` 预处理+模型一键组装
- `run_demo()` 用泰坦尼克风格数据完整演示
- 缺失值/异常值检测辅助函数

---

## 9. 常见陷阱

1. **数据泄露**：缩放/编码只用 fit_transform 训练集，测试集只 transform
2. **缺失值在缩放前处理**：SimpleImputer 必须在 StandardScaler 之前
3. **随机种子不固定**：结果不可复现
4. **分类问题不 stratified**：类别不均衡时划分要分层
5. **测试集做 EDA**：一切探索性分析只针对训练集
6. **树模型不需要缩放**：别浪费算力

---

## 速查：什么时候用什么

| 问题 | 工具 |
|------|------|
| 数值缺失 | SimpleImputer(strategy='median') |
| 类别缺失 | SimpleImputer(strategy='most_frequent') |
| 量纲不同 | StandardScaler / MinMaxScaler |
| 文本类别 | OneHotEncoder |
| 有序类别 | OrdinalEncoder |
| 异常值多 | RobustScaler |
| 防数据泄露 | Pipeline + ColumnTransformer |
| 调参 | GridSearchCV + Pipeline |
