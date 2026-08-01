# Matplotlib + Seaborn 完整学习笔记
> 学习日期: 2026-07-31  |  matplotlib 3.11.1  |  seaborn 0.13.2

## 目录

1. [matplotlib 基础](#1-matplotlib-基础)
2. [figure 与 axes](#2-figure-与-axes)
3. [常用图表类型](#3-常用图表类型)
4. [样式与美化](#4-样式与美化)
5. [子图布局](#5-子图布局)
6. [seaborn 风格与主题](#6-seaborn-风格与主题)
7. [seaborn 分类图](#7-seaborn-分类图)
8. [seaborn 分布图](#8-seaborn-分布图)
9. [seaborn 关系图](#9-seaborn-关系图)
10. [seaborn 矩阵图与回归](#10-seaborn-矩阵图与回归)
11. [图表保存与中文字体](#11-图表保存与中文字体)
12. [实战技巧汇总](#12-实战技巧汇总)

---

## 1. matplotlib 基础

matplotlib 是 Python 最基础的绘图库，seaborn 建立在它之上。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)          # 画折线图
plt.title('正弦曲线')    # 标题
plt.xlabel('x')         # x轴标签
plt.ylabel('y')         # y轴标签
plt.show()              # 显示图表
```

### 两种绘图方式

| 方式 | 说明 | 适用场景 |
|------|------|---------|
| 函数式 plt.plot() | 简单快速，自动管理 figure | 快速画图 |
| 面向对象 fig, ax = plt.subplots() | 精确控制每个元素 | 复杂图表/子图 |

```python
# 函数式
plt.plot(x, y)
plt.show()

# 面向对象（推荐用于复杂图）
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('标题')
plt.show()
```

---

## 2. figure 与 axes

| 对象 | 说明 |
|------|------|
| figure | 整个画布/窗口 |
| axes | 画布上的一个坐标系（可多个） |

```python
fig, ax = plt.subplots(figsize=(8, 5))  # 8x5英寸的画布
ax.plot(x, y, label='sin')              # 画线并加标签
ax.legend()                             # 显示图例
ax.grid(True)                           # 显示网格
ax.set_xlim(0, 10)                      # 设置x轴范围
ax.set_ylim(-1.5, 1.5)                  # 设置y轴范围
ax.set_xticks([0, 5, 10])               # 自定义刻度
plt.show()
```

---

## 3. 常用图表类型

### 折线图 plot
```python
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o')
```

### 散点图 scatter
```python
plt.scatter(x, y, s=50, c='blue', alpha=0.7)  # s=点大小 c=颜色 alpha=透明度
```

### 柱状图 bar
```python
plt.bar(['A','B','C'], [10, 20, 15], color=['red','green','blue'])
plt.barh(['A','B','C'], [10, 20, 15])   # 水平柱状图
```

### 直方图 hist
```python
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='white')  # bins=分箱数
```

### 饼图 pie
```python
plt.pie([30, 40, 30], labels=['A','B','C'], autopct='%1.1f%%')
```

### 箱线图 boxplot
```python
plt.boxplot(data, vert=False)
```

---

## 4. 样式与美化

```python
plt.style.available        # 查看所有可用样式
plt.style.use('ggplot')    # 使用样式

# 常用颜色
# 颜色名: red, blue, green
# 缩写: r, b, g, k(黑), w(白), c(青), m(品红), y(黄)
# 十六进制: #FF5733

# 线型 linestyle
# '-'实线 '--'虚线 '-.'点划线 ':'点线

# 标记 marker
# 'o'圆点 's'方块 '^'三角 'x'叉号 '*'星号

# 常用设置
plt.rcParams['font.size'] = 12
plt.rcParams['figure.dpi'] = 100
plt.grid(True, alpha=0.3)
plt.tight_layout()   # 自动调整布局防重叠
```

---

## 5. 子图布局

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))  # 2行2列

axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar([1,2,3], [3,1,2])
axes[1, 1].hist(np.random.randn(100), bins=20)

plt.tight_layout()
plt.show()
```

```python
# 共享坐标轴
fig, axes = plt.subplots(2, 1, sharex=True, sharey=True)
```

---

## 6. seaborn 风格与主题

seaborn 基于 matplotlib，提供更美观的默认样式和高级绘图接口。

```python
import seaborn as sns
import pandas as pd

sns.set_theme()                  # 设置默认主题
sns.set_style('whitegrid')       # 风格: white/dark/whitegrid/darkgrid/ticks
sns.set_palette('Set2')          # 调色板
sns.set_context('notebook')      # 上下文: paper/notebook/talk/poster
```

### 内置数据集
```python
df = sns.load_dataset('tips')        # 小费数据
df = sns.load_dataset('iris')        # 鸢尾花数据
df = sns.load_dataset('titanic')     # 泰坦尼克数据
df = sns.load_dataset('flights')     # 航班数据
```

---

## 7. seaborn 分类图

```python
df = sns.load_dataset('tips')

# 分类柱状图
sns.barplot(data=df, x='day', y='total_bill', hue='sex')

# 分类箱线图
sns.boxplot(data=df, x='day', y='total_bill')

# 小提琴图（箱线图+核密度）
sns.violinplot(data=df, x='day', y='total_bill')

# 分类散点图
sns.stripplot(data=df, x='day', y='total_bill', jitter=True)
sns.swarmplot(data=df, x='day', y='total_bill')

# 计数图
sns.countplot(data=df, x='day')
```

---

## 8. seaborn 分布图

```python
data = df['total_bill']

# 直方图+核密度
sns.histplot(data, kde=True, bins=30)

# 核密度图
sns.kdeplot(data, shade=True)

# 双变量分布图
sns.jointplot(data=df, x='total_bill', y='tip', kind='hex')  # kind: scatter/hex/kde
```

---

## 9. seaborn 关系图

```python
# 散点图
sns.scatterplot(data=df, x='total_bill', y='tip', hue='sex', size='size')

# 线图
sns.lineplot(data=df, x='day', y='total_bill')

# 多变量关系矩阵
sns.pairplot(df[['total_bill','tip','size']], hue='sex')
```

---

## 10. seaborn 矩阵图与回归

```python
# 相关性热力图
corr = df[['total_bill','tip','size']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')

# 回归图（散点+拟合线）
sns.regplot(data=df, x='total_bill', y='tip')
sns.lmplot(data=df, x='total_bill', y='tip', hue='sex')  # 分组回归
```

---

## 11. 图表保存与中文字体

### 保存图片
```python
plt.savefig('figure.png', dpi=300, bbox_inches='tight')
plt.savefig('figure.pdf')   # 矢量图
```

### 中文字体显示（Windows）
```python
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块
```

---

## 12. 实战技巧汇总

### 一次画多个图
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

sns.histplot(data=df, x='total_bill', kde=True, ax=axes[0,0])
sns.boxplot(data=df, x='day', y='total_bill', ax=axes[0,1])
sns.scatterplot(data=df, x='total_bill', y='tip', hue='sex', ax=axes[1,0])
sns.heatmap(corr, annot=True, ax=axes[1,1])

plt.tight_layout()
plt.show()
```

### seaborn 图形对象接口（新）
```python
p = sns.relplot(data=df, x='total_bill', y='tip', col='sex', kind='scatter')
p = sns.catplot(data=df, x='day', y='total_bill', kind='box', col='sex')
p = sns.displot(data=df, x='total_bill', kind='hist', kde=True, col='sex')
```

### 颜色调色板
```python
sns.color_palette('husl', 8)      # HUSL色环
sns.color_palette('Spectral', 10) # 光谱色
sns.color_palette('Set1', 5)      # 分类色
sns.color_palette('Reds', 5)      # 单色渐变
```

### 常见陷阱

- matplotlib 和 seaborn 混用时注意坐标系
- seaborn 函数都接受 ax= 参数指定绘图位置
- 中文字体必须配置，否则显示方块
- plt.show() 后图像无法再修改
- 先用 sns.set_theme() 统一风格

---

> 更多练习见 [viz_exercises.py](./viz_exercises.py)
> 答案见 [viz_answers.py](./viz_answers.py)
