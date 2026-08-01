import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties

# 【核心】强制加载系统字体文件
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf")
plt.rcParams['axes.unicode_minus'] = False  # 解决负号

sns.set_theme()

# 离线tips数据集
tips_data = {
    "total_bill": [16.99,10.34,21.01,23.68,24.59,25.29,8.77,26.88,15.04,14.78,
                   18.43,24.08,15.04,29.80,17.92],
    "tip": [1.01,1.66,3.50,3.31,3.61,4.71,2.00,3.12,1.96,3.23,
            3.02,3.92,1.66,4.50,3.08],
    "sex": ["Male","Male","Male","Male","Female","Male","Male","Male","Male","Male",
            "Male","Male","Male","Male","Female"],
    "smoker": ["No","No","No","No","No","No","No","No","No","No",
               "No","No","No","No","No"],
    "day": ["Sun","Sun","Sun","Sun","Sun","Sun","Sun","Sun","Sun","Sun",
            "Sun","Sun","Sun","Sun","Sun"],
    "time": ["Dinner","Dinner","Dinner","Dinner","Dinner","Dinner","Dinner","Dinner","Dinner","Dinner",
             "Dinner","Dinner","Dinner","Dinner","Dinner"],
    "size": [2,3,3,2,4,4,2,4,2,2,
             2,4,2,4,2]
}
df = pd.DataFrame(tips_data)

print('=' * 60)
print('第一关')
print('=' * 60)

x = np.linspace(0, 10, 100)

# 1. 折线图
plt.figure(figsize=(8, 5))
plt.plot(x, x**2, color='blue')
plt.title('y = x^2', fontproperties=font)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.show()
print('1. 折线图绘制完成')

# 2. 散点图
plt.figure(figsize=(8, 5))
plt.scatter(df['total_bill'], df['tip'], color='red', alpha=0.7)
plt.title('total_bill vs tip', fontproperties=font)
plt.xlabel('total_bill')
plt.ylabel('tip')
plt.show()
print('2. 散点图绘制完成')

# 3. 柱状图
day_avg = df.groupby('day')['total_bill'].mean()
plt.figure(figsize=(8, 5))
plt.bar(day_avg.index, day_avg.values, color='steelblue')
plt.title('每日平均消费', fontproperties=font)
plt.ylabel('平均消费')
plt.show()
print('3. 柱状图绘制完成')

# 4. 直方图
plt.figure(figsize=(8, 5))
plt.hist(df['total_bill'], bins=30, edgecolor='white')
plt.title('total_bill 分布', fontproperties=font)
plt.show()
print('4. 直方图绘制完成')

print('=' * 60)
print('第二关')
print('=' * 60)

# 5. 2x2子图
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0,0].plot(x, np.sin(x), color='red')
axes[0,0].set_title('sin(x)', fontproperties=font)
axes[0,1].scatter(df['total_bill'], df['tip'], alpha=0.5)
axes[0,1].set_title('bill vs tip', fontproperties=font)
axes[1,0].bar(day_avg.index, day_avg.values)
axes[1,0].set_title('每日均值', fontproperties=font)
axes[1,1].hist(df['total_bill'], bins=20, edgecolor='white')
axes[1,1].set_title('bill分布', fontproperties=font)
plt.tight_layout()
plt.show()
print('5. 子图绘制完成')

# 6. 美化折线
plt.figure(figsize=(8, 5))
plt.plot(x, np.sin(x), color='red', linestyle='--', linewidth=2, marker='o', markersize=4, label='sin(x)')
plt.plot(x, np.cos(x), color='blue', linestyle='-', linewidth=1.5, label='cos(x)')
plt.title('sin 和 cos 曲线', fontproperties=font)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
print('6. 美化折线绘制完成')

print('=' * 60)
print('第三关')
print('=' * 60)

# 7. barplot
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='day', y='total_bill', hue='sex')
plt.title('每日消费(按性别)', fontproperties=font)
plt.show()
print('7. barplot绘制完成')

# 8. boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='day', y='total_bill')
plt.title('每日消费分布', fontproperties=font)
plt.show()
print('8. boxplot绘制完成')

# 9. countplot
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='day')
plt.title('每日订单数', fontproperties=font)
plt.show()
print('9. countplot绘制完成')

print('=' * 60)
print('第四关')
print('=' * 60)

# 10. histplot
plt.figure(figsize=(8, 5))
sns.histplot(df['total_bill'], kde=True, bins=30)
plt.title('total_bill 分布', fontproperties=font)
plt.show()
print('10. histplot绘制完成')

# 11. heatmap
corr = df[['total_bill','tip','size']].corr()
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('相关性热力图', fontproperties=font)
plt.show()
print('11. heatmap绘制完成')

# 12. regplot
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='total_bill', y='tip')
plt.title('回归拟合', fontproperties=font)
plt.show()
print('12. regplot绘制完成')

# 13. jointplot
g = sns.jointplot(data=df, x='total_bill', y='tip', kind='scatter')
g.fig.suptitle('散点联合分布图', fontproperties=font, y=1.02)
plt.show()
print('13. jointplot绘制完成')

print('=' * 60)
print('第五关')
print('=' * 60)

# 14. 综合四联图
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
sns.histplot(df['total_bill'], kde=True, ax=axes[0,0])
sns.boxplot(data=df, x='day', y='total_bill', ax=axes[0,1])
sns.scatterplot(data=df, x='total_bill', y='tip', hue='sex', ax=axes[1,0])
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', ax=axes[1,1])
fig.suptitle('综合数据分析', fontsize=16, fontproperties=font)
plt.tight_layout()
plt.show()
print('14. 综合图绘制完成')

# 15. pairplot
g = sns.pairplot(df[['total_bill','tip','size','sex']], hue='sex')
g.fig.suptitle('特征两两关系图', fontproperties=font, y=1.01)
plt.show()
print('15. pairplot绘制完成')

print('全部绘图结束！')