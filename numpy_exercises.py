# ============================================================
# NumPy 实战练习题 — 真实场景数据【完整可运行版本】
# ============================================================
# 运行: python exercises.py
# 每题先自己写，写不出的看答案
# ============================================================

import numpy as np

print("=" * 60)
print("  NumPy 实战练习题")
print("=" * 60)

rng = np.random.default_rng(2024)


# ════════════════════════════════════════════════════════════
# 第一关：数据清洗（处理真实数据中的常见问题）
# ════════════════════════════════════════════════════════════
print("\n" + "-" * 60)
print("第一关：数据清洗")
print("-" * 60)

# 场景：某公司销售数据，包含异常值和缺失值
sales = np.array([120, 135, 99999, 118, 122, -5, 130, 128, 99999, 125, 0, 132])
print("原始销售数据：", sales)

# 题目1: 找出数据中 > 1000 的异常值，把它们替换成前后两个值的平均数
# 注意：首尾元素边界特殊处理，这里简化方案
sales_clean = sales.copy()
mask_outlier = sales > 1000
sales_clean[mask_outlier] = (np.roll(sales,1)[mask_outlier] + np.roll(sales,-1)[mask_outlier]) / 2
print("题目1: 替换>1000异常值后：", sales_clean)

# 题目2: 找出数据中 <= 0 的无效值，替换为该列的中位数
median_val = np.median(sales_clean[sales_clean <= 1000])
mask_invalid = sales_clean <= 0
sales_clean[mask_invalid] = median_val
print("题目2: 替换<=0无效值后：", sales_clean)

# 题目3: 计算清洗后的数据：均值、标准差、最大值、最小值
cleaned_mean = np.mean(sales_clean)
cleaned_std = np.std(sales_clean)
cleaned_max = np.max(sales_clean)
cleaned_min = np.min(sales_clean)
print(f"题目3 统计量：均值={cleaned_mean:.2f}, 标准差={cleaned_std:.2f}, max={cleaned_max:.2f}, min={cleaned_min:.2f}")


# ════════════════════════════════════════════════════════════
# 第二关：股票收益率计算（金融数据分析）
# ════════════════════════════════════════════════════════════
print("\n" + "-" * 60)
print("第二关：股票收益率计算")
print("-" * 60)

prices = np.array([100, 102, 101, 105, 108, 107, 110, 115, 112, 118])
print("股价：", prices)

# 题目4: 每日收益率 (今日-昨日)/昨日
returns = (prices[1:] - prices[:-1]) / prices[:-1]
print("题目4 每日收益率：", np.round(returns,4))

# 题目5: 累计收益率
cumulative_return = (prices[-1] / prices[0]) - 1
print(f"题目5 累计收益率：{cumulative_return:.4f}")

# 题目6: 收益率最高、最低索引
max_return_idx = np.argmax(returns)
min_return_idx = np.argmin(returns)
print(f"题目6 最高收益率索引:{max_return_idx}, 最低收益率索引:{min_return_idx}")

# 题目7: 波动率（收益率标准差）
volatility = np.std(returns)
print(f"题目7 波动率：{volatility:.4f}")


# ════════════════════════════════════════════════════════════
# 第三关：图像处理基础（计算机视觉入门）
# ════════════════════════════════════════════════════════════
print("\n" + "-" * 60)
print("第三关：图像处理基础")
print("-" * 60)

img = np.random.randint(0, 256, (5, 5), dtype=np.uint8)
print("原始图像 (5x5):")
print(img)

# 题目8: 二值化 >127→255，其余→0
img_bin = np.where(img > 127, 255, 0)
print("\n题目8 二值图像：")
print(img_bin)

# 题目9: 3×3均值滤波（边界不处理）
img_blur = img.copy().astype(np.float32)
h, w = img.shape
for i in range(1, h-1):
    for j in range(1, w-1):
        region = img[i-1:i+2, j-1:j+2]
        img_blur[i,j] = np.mean(region)
print("\n题目9 均值模糊图像：")
print(img_blur.astype(np.uint8))

# 题目10: 上下翻转
img_flip_ud = np.flipud(img)
print("\n题目10 上下翻转：")
print(img_flip_ud)

# 题目11: 左右翻转
img_flip_lr = np.fliplr(img)
print("\n题目11 左右翻转：")
print(img_flip_lr)


# ════════════════════════════════════════════════════════════
# 第四关：学生成绩分析（教育数据分析）
# ════════════════════════════════════════════════════════════
print("\n" + "-" * 60)
print("第四关：学生成绩分析")
print("-" * 60)

scores = np.array([
    [85, 92, 78],   # 学生0
    [90, 88, 95],   # 学生1
    [76, 65, 82],   # 学生2
    [95, 98, 92],   # 学生3
    [68, 72, 70],   # 学生4
])
print("成绩单 (行=学生, 列=语/数/英):")
print(scores)

# 题目12: 每个学生总分、平均分
total_scores = np.sum(scores, axis=1)
average_scores = np.mean(scores, axis=1)
print("\n题目12 每位学生总分：", total_scores)
print("每位学生平均分：", np.round(average_scores,2))

# 题目13: 每门课班级平均分
average_per_subject = np.mean(scores, axis=0)
print("题目13 各科平均分：", np.round(average_per_subject,2))

# 题目14: 总分最高学生索引
max_total_idx = np.argmax(total_scores)
print(f"题目14 总分最高学生索引：{max_total_idx}")

# 题目15: >=90分位置
high_scores = np.where(scores >= 90)
print("\n题目15 90分以上坐标(学生,课程)：")
for row,col in zip(*high_scores):
    print(f"学生{row},课程{col},分数={scores[row,col]}")

# 题目16: Z-score标准化【按列（每门课程）标准化】
mean_sub = np.mean(scores, axis=0)
std_sub = np.std(scores, axis=0)
scores_norm = (scores - mean_sub) / std_sub
print("\n题目16 标准化成绩：")
print(np.round(scores_norm,2))


# ════════════════════════════════════════════════════════════
# 第五关：蒙特卡洛模拟（概率/风险分析）
# ════════════════════════════════════════════════════════════
print("\n" + "-" * 60)
print("第五关：蒙特卡洛模拟")
print("-" * 60)

rng = np.random.default_rng(2024)

# 题目17: 抛硬币10000次，正面概率
n_flip = 10000
coin = rng.integers(0,2,size=n_flip)
prob_head = np.sum(coin == 1) / n_flip
print(f"题目17 正面概率：{prob_head:.4f}")

# 题目18: 两个骰子，点数和为7的概率
n_dice = 100000
d1 = rng.integers(1,7,size=n_dice)
d2 = rng.integers(1,7,size=n_dice)
sum_dice = d1 + d2
prob_seven = np.sum(sum_dice == 7) / n_dice
print(f"题目18 两点数之和为7概率：{prob_seven:.4f}")

# 题目19【选做】股票随机游走
sim_times = 1000
days = 30
start_price = 100
# 每次随机增量 N(0,1)
changes = rng.normal(loc=0, scale=1, size=(sim_times, days))
price_path = start_price + np.cumsum(changes, axis=1)
final_price = price_path[:, -1]
prob_over_110 = np.sum(final_price > 110) / sim_times
print(f"\n题目19 30天后价格>110概率：{prob_over_110:.4f}")


# ════════════════════════════════════════════════════════════
# 第六关：线性代数实战
# ════════════════════════════════════════════════════════════
print("\n" + "-" * 60)
print("第六关：线性代数实战")
print("-" * 60)

# 题目20: 解线性方程组
#   x + 2y + z = 10
#   2x + 3y + 2z = 17
#   3x + y + z = 13
A = np.array([[1, 2, 1], [2, 3, 2], [3, 1, 1]])
b = np.array([10, 17, 13])
x = np.linalg.solve(A, b)
print("题目20 方程组解 x,y,z =", np.round(x,2))

# 题目21: SVD，取前2个奇异值做低秩近似
A = np.random.randint(1, 10, (4, 4)).astype(float)
print("\n原始矩阵 A:")
print(A)

U, S, Vt = np.linalg.svd(A)
# 保留前2个奇异值
S2 = np.zeros_like(S)
S2[:2] = S[:2]
Sigma2 = np.zeros((4,4))
np.fill_diagonal(Sigma2, S2)
A_approx = U @ Sigma2 @ Vt
print("\n题目21 保留前2奇异值近似矩阵：")
print(np.round(A_approx,2))


print("\n" + "=" * 60)
print("  NumPy练习全部运行完毕！")
print("=" * 60)
print(np.__version__)