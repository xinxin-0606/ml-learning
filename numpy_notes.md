# NumPy 完整学习笔记

> 学习日期: 2026-07-29  |  NumPy v2.5.1

## 目录

1. [创建数组](#1-创建数组)
2. [数组属性](#2-数组属性)
3. [索引与切片](#3-索引与切片)
4. [形状操作](#4-形状操作)
5. [数学运算与广播](#5-数学运算与广播)
6. [统计函数与 axis](#6-统计函数与-axis)
7. [通用函数 ufunc](#7-通用函数-ufunc)
8. [线性代数](#8-线性代数)
9. [随机数](#9-随机数)
10. [实战技巧](#10-实战技巧)

## 1. 创建数组

```python
# 从列表创建
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])   # 二维数组

# 常用初始化函数
np.zeros((2, 3))     # 全0矩阵
np.ones((3, 2))      # 全1矩阵
np.eye(4)            # 单位矩阵
np.full((2,3), 7)    # 指定值填充

# 序列生成
np.arange(0, 10, 2)           # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)          # [0, 0.25, 0.5, 0.75, 1.0]
```

## 2. 数组属性

```python
arr.shape       # 形状元组 (行, 列, ...)
arr.ndim        # 维度数
arr.size        # 元素总数
arr.dtype       # 数据类型 (int32, float64)
arr.itemsize    # 每个元素字节数
```

## 3. 索引与切片

```python
arr[row, col]              # 单个元素
arr[start:stop:step]       # 一维切片
arr[:, 1]                  # 所有行，第1列
arr[0, :]                  # 第0行，所有列
arr[:2, :3]                # 前2行，前3列
arr[::-1]                  # 反转所有行
arr[[0, 2, 4]]             # 花式索引
arr[arr > 5]               # 布尔索引
```

## 4. 形状操作

```python
arr.reshape(3, 4)            # 改变形状
arr.reshape(-1, 4)           # -1 自动计算
arr.flatten()                # 展平（返回副本）
arr.ravel()                  # 展平（返回视图）
arr.T                        # 转置
np.vstack((a, b))            # 垂直拼接
np.hstack((a, b))            # 水平拼接
np.concatenate((a,b), axis=0) # 指定轴拼接
```

## 5. 数学运算与广播

```python
# 元素级运算
a + b, a - b, a * b, a / b, a ** 2

# 矩阵乘法
A @ B              # Python 3.5+ 推荐用法
np.dot(A, B)       # 等价

# 广播 Broadcast
[1,2,3] + 10                 # 标量广播 -> [11,12,13]
np.ones((3,3)) + [1,2,3]     # 向量广播

# 广播规则：从后往前比较维度，相等/为1/缺失则兼容
```

## 6. 统计函数与 axis

```python
arr.sum()       arr.mean()       arr.std()
arr.var()       arr.min()        arr.max()
np.median(arr)  np.percentile(arr, 25)
arr.cumsum()    arr.cumprod()

# axis 参数核心理解
arr.sum(axis=0)    # 按列操作（压扁行）
arr.sum(axis=1)    # 按行操作（压扁列）

# keepdims 保持维度
arr.max(axis=1, keepdims=True)
```

> axis 口诀：axis=第几维，第几维就消失

## 7. 通用函数 ufunc

```python
np.abs / np.sign / np.clip         # 条件函数
np.exp / np.log / np.log10 / np.log2  # 指数对数
np.sin / np.cos / np.tan           # 三角函数
np.round / np.floor / np.ceil      # 取整
np.where(cond, x, y)               # 条件选择
np.add.reduce([1,2,3])              # reduce 聚合
np.add.accumulate([1,2,3])          # accumulate 累计
```

## 8. 线性代数

```python
np.linalg.det(A)         # 行列式
np.linalg.inv(A)         # 逆矩阵
np.linalg.solve(A, b)    # 解方程组 Ax=b
np.linalg.eig(A)         # 特征值/特征向量
np.linalg.svd(A)         # SVD分解
np.linalg.norm(v)        # 范数
```

## 9. 随机数

```python
# 新式API (推荐)
rng = np.random.default_rng(42)  # 固定种子
rng.random(n)              # [0,1) 均匀分布
rng.normal(0, 1, n)        # 正态分布
rng.integers(0, 10, n)     # 随机整数
rng.choice(arr, p=[...])   # 按概率抽样
rng.shuffle(arr)           # 打乱

# 常见分布
rng.binomial(n, p, size)    # 二项分布
rng.poisson(lambda, size)   # 泊松分布
rng.exponential(scale, size)

# 旧式API
np.random.seed(42)
np.random.rand(3) / np.random.randn(3)
np.random.randint(0, 10, 5)
```

## 10. 实战技巧

### 数据清洗
```python
data[data > 1000] = np.median(data)    # 替换异常值
z = (data - data.mean()) / data.std()  # Z-score标准化
```

### 蒙特卡洛估算圆周率
```python
x = rng.uniform(-1, 1, 100000)
y = rng.uniform(-1, 1, 100000)
pi_est = 4 * ((x**2 + y**2) <= 1).mean()
```

### 图像翻转
```python
img[::-1]        # 上下翻转
img[:, ::-1]     # 左右翻转
```

### 解线性方程组
```python
A = np.array([[2, 3], [5, -1]])
b = np.array([7, 9])
x = np.linalg.solve(A, b)
```

---

## 项目文件

- [练习题](numpy_exercises_questions.py)
- [答案](numpy_answers.py)
- [复习脚本](review_numpy.py)

---

> 学习路线下一站: Pandas -> Scikit-learn -> 深度学习