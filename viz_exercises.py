# Matplotlib + Seaborn 实战练习
# 运行: python viz_exercises.py   (先自己写,答案在 viz_answers.py)

import matplotlib
matplotlib.use('Agg')  # 无窗口模式,保存图片
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
sns.set_theme()

df = sns.load_dataset('tips')
print(df.head())

print('=' * 60)
print('第一关: matplotlib 基础')
print('=' * 60)

# 1. 画一条 y = x^2 的折线图 (x从0到10)
print('1. 折线图 y=x^2')

# 2. 画散点图: x=total_bill, y=tip, 用红色圆点
print('2. 散点图 total_bill vs tip')

# 3. 画柱状图: 每天的平均消费
print('3. 柱状图 每日平均消费')

# 4. 画直方图: total_bill 分布, 30个箱子
print('4. 直方图 total_bill')

print('=' * 60)
print('第二关: 子图与美化')
print('=' * 60)

# 5. 创建2x2子图: 折线/散点/柱状/直方
print('5. 2x2子图')

# 6. 画红色虚线带圆点的正弦曲线, 加标题/标签/图例/网格
print('6. 美化折线图')

print('=' * 60)
print('第三关: seaborn 分类图')
print('=' * 60)

# 7. barplot: 每天平均消费, 按性别分组(hue)
print('7. seaborn 分类柱状图')

# 8. boxplot: 每天消费分布
print('8. seaborn 箱线图')

# 9. countplot: 每天订单数量
print('9. seaborn 计数图')

print('=' * 60)
print('第四关: seaborn 分布与关系')
print('=' * 60)

# 10. histplot: total_bill 分布, 带核密度曲线
print('10. 直方图+核密度')

# 11. heatmap: 数值列相关性热力图, 显示数值
print('11. 相关性热力图')

# 12. regplot: total_bill vs tip 回归拟合线
print('12. 回归图')

# 13. jointplot: total_bill vs tip 联合分布
print('13. 联合分布图')

print('=' * 60)
print('第五关: 综合实战')
print('=' * 60)

# 14. 用 subplots 一次画4张图并保存为 result.png
print('14. 综合四联图保存')

# 15. pairplot: 数值列两两关系, 按性别着色
print('15. pairplot')

print('全部完成! 检查生成的图片')
