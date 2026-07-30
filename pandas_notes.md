# Pandas 完整学习笔记
> 学习日期: 2026-07-30  |  Pandas v3.0.5

## 目录

1. [两种核心数据结构](#1)
2. [读写数据](#2)
3. [数据查看](#3)
4. [选择数据](#4)
5. [条件筛选](#5)
6. [数据清洗](#6)
7. [新增/修改列](#7)
8. [分组聚合](#8)
9. [排序](#9)
10. [合并拼接](#10)
11. [apply函数](#11)
12. [实战技巧](#12)

---

## 1. 两种核心数据结构

### Series - 一维带标签数组

```python
import pandas as pd
s = pd.Series([85, 92, 78], index=["语文","数学","英语"])
s.values    # [85, 92, 78]
s.index     # 索引标签
s.mean()    # 计算均值
```

### DataFrame - 二维表格

```python
df = pd.DataFrame({
    "姓名": ["张三","李四","王五"],
    "年龄": [25, 30, 28],
    "城市": ["北京","上海","广州"]
})
print(df)
```

---

## 2. 读写数据

```python
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)

df = pd.read_excel("data.xlsx")
df.to_excel("output.xlsx", index=False)

df = pd.read_json("data.json")
```

---

## 3. 数据查看

```python
df.head()       # 前5行
df.tail()       # 后5行
df.sample(3)    # 随机3行
df.info()       # 列信息/类型/非空数
df.describe()   # 数值列统计摘要
df.shape        # (行数,列数)
df.columns      # 所有列名
df.dtypes       # 每列类型
```

---

## 4. 选择数据

```python
# 选列
df['姓名']          # 单列 -> Series
df[['姓名','年龄']] # 多列 -> DataFrame

# loc 标签索引
df.loc[0]          # 第0行
df.loc[0:2]        # 0-2行(含末尾)

# iloc 位置索引
df.iloc[0]         # 第0行
df.iloc[0:3]       # 0-2行(不含末尾)
df.iloc[0:3, 0:2]  # 前3行前2列
```

---

## 5. 条件筛选

```python
df[df['年龄'] > 25]

# 多条件用 & 连接(不是 and) 每个条件加()
df[(df['年龄']>25) & (df['城市']=='北京')]

# isin 多个值
df[df['城市'].isin(['北京','上海'])]

# 字符串方法
df[df['姓名'].str.contains('张')]

# query
df.query('年龄 > 25')
```

---

## 6. 数据清洗

```python
df.isna().sum()           # 缺失值统计

df.dropna()               # 删除缺失行
df.dropna(subset=['年龄'])

df.fillna(0)              # 用0填充
df['年龄'].fillna(df['年龄'].mean())
df['年龄'].fillna(method='ffill')

df.duplicated()           # 重复标记
df.drop_duplicates()      # 删除重复

df['年龄'] = df['年龄'].astype(float)
df['日期'] = pd.to_datetime(df['日期'])
```

---

## 7. 新增/修改列

```python
df['总分'] = df['语文']+df['数学']+df['英语']
df['平均分'] = df[['语文','数学','英语']].mean(axis=1)

df['评级'] = '不及格'
df.loc[df['总分']>=180, '评级'] = '及格'
df.loc[df['总分']>=240, '评级'] = '优秀'

df.rename(columns={'姓名':'name'}, inplace=True)
df.drop(columns=['评级'])
```

---

## 8. 分组聚合

```python
df.groupby('城市')['年龄'].mean()

df.groupby('城市').agg({
    '年龄': ['mean','max','min'],
    '姓名': 'count'
})

df['城市工资均值'] = df.groupby('城市')['工资'].transform('mean')
df.groupby('城市')['工资'].mean().reset_index()
```

---

## 9. 排序

```python
df.sort_values('年龄')#默认升序
df.sort_values('年龄', ascending=False)降序
df.sort_values(['城市','年龄'], ascending=[True,False])
df.sort_index()
```

---

## 10. 合并拼接

```python
pd.merge(df1, df2, on="学号", how="inner")   # 内连接
pd.merge(df1, df2, on="学号", how="left")     # 左连接
pd.concat([df1, df2], axis=0)                 # 行拼接
pd.concat([df1, df2], axis=1)                 # 列拼接

```

---

## 11. apply函数

```python
df['年龄分组'] = df['年龄'].apply(lambda x: '青年' if x<30 else '中年')

df['总分'] = df.apply(lambda r: r['语文']+r['数学']+r['英语'], axis=1)

def score_level(s):
    if s >= 90: return 'A'
    if s >= 75: return 'B'
    return 'C'
df['等级'] = df['总分'].apply(score_level)
```

---

## 12. 实战技巧

### 批量改列名
```python
df.columns = ['a','b','c']
```

### 随机采样
```python
df.sample(n=10)
df.sample(frac=0.1)
```

### 时间序列
```python
# 手动指定格式
dates = ['2020-01-15', '2021-03-20', '2022-05-10']

# %Y: 四位年份, %m: 月份, %d: 日
result = pd.to_datetime(dates, format='%Y-%m-%d')
print(result)

# 其他格式
dates2 = ['15-01-2020', '20-03-2021', '10-05-2022']
result2 = pd.to_datetime(dates2, format='%d-%m-%Y')
print(result2)
df['日期'] = pd.to_datetime(df['日期'])
df.set_index('日期', inplace=True)
df['2024']
df.resample('M')['销售额'].sum()
```

### 数据透视表
```python
df.pivot_table(
    values='要计算的列',      # 对哪一列做计算
    index='行标签',           # 按什么分组（行）
    columns='列标签',         # 按什么分组（列）
    aggfunc='聚合函数',       # 怎么算：sum, mean, count, max, min...
    fill_value=0,            # 空值填什么
    margins=True,            # 是否显示汇总行/列
    margins_name='总计'      # 汇总行/列的名字
)
pd.pivot_table(df, values='工资', index='城市', columns='部门', aggfunc='mean')

```

---
