# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import sys
import io

# 解决 Windows 控制台中文乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


print("=" * 60)
print("  Pandas 实战练习题")
print("=" * 60)

# 创建数据
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十"],
    "语文": [85, 92, 78, 95, 68, 88, 73, 90],
    "数学": [90, 88, 65, 98, 72, 91, 80, 85],
    "英语": [78, 95, 82, 92, 70, 85, 76, 88],
    "城市": ["北京", "上海", "广州", "深圳", "北京", "上海", "广州", "深圳"],
    "工资": [12000, 15000, 9000, 20000, 11000, 14000, 9500, 18000]
})

print("\n原始数据:")
print(df)

print("\n" + "=" * 60)
print("第一关: 数据查看与选择")
print("=" * 60)

# 1
print("\n1. 显示前3行")
print(df.head(3))

# 2
print("\n2. 显示所有列名")
print(df.columns.tolist())

# 3
print("\n3. 显示数学成绩列")
print(df['数学'])

# 4
print("\n4. 显示第4行(赵六)的所有信息")
print(df.iloc[3])

# 5
print("\n5. 显示前3行、姓名和语文两列")
print(df.loc[0:2, ['姓名', '语文']])

print("\n" + "=" * 60)
print("第二关: 条件筛选")
print("=" * 60)

# 6
print("\n6. 筛选出数学成绩大于85的学生")
print(df[df['数学'] > 85])

# 7
print("\n7. 筛选出北京和上海的学生")
print(df[df['城市'].isin(['北京', '上海'])])

# 8
print("\n8. 筛选出语文>80且英语>80的学生")
print(df[(df['语文'] > 80) & (df['英语'] > 80)])

# 9
print("\n9. 筛选出姓张的学生")
print(df[df['姓名'].str.contains('张')])

print("\n" + "=" * 60)
print("第三关: 数据清洗与修改")
print("=" * 60)

# 10
print("\n10. 新增一列[总分] = 语+数+英")
df['总分'] = df['语文'] + df['数学'] + df['英语']

# 11
print("\n11. 新增一列[评级]: 总分>=270为优秀,>=240为良好,其余为一般")
def get_grade(total):
    if total >= 270:
        return '优秀'
    elif total >= 240:
        return '良好'
    else:
        return '一般'
df['评级'] = df['总分'].apply(get_grade)

# 12
print("\n12. 按总分从高到低排序")
print(df.sort_values('总分', ascending=False))

# 13
print("\n13. 给每个人加薪10%, 更新工资列")
df['工资'] = (df['工资'] * 1.1).astype(float)

print("\n" + "=" * 60)
print("第四关: 分组聚合")
print("=" * 60)

# 14
print("\n14. 按城市分组,计算每个城市的人数")
print(df.groupby('城市').size())

# 15
print("\n15. 按城市分组,计算每个城市的平均工资(保留整数)")
print(df.groupby('城市')['工资'].mean().astype(int))

# 16
print("\n16. 按城市分组,统计各科平均分")
print(df.groupby('城市')[['语文', '数学', '英语']].mean().astype(int))

print("\n" + "=" * 60)
print("第五关: 综合实战")
print("=" * 60)

# 17
print("\n17. 找出总分最高的学生叫什么")
max_idx = df['总分'].idxmax()
print(df.loc[max_idx, '姓名'])

# 18
print("\n18. 找出工资大于平均工资的学生")
avg_salary = df['工资'].mean()
print(df[df['工资'] > avg_salary])

# 19
print("\n19. 使用apply: 根据总分评等级(A:>=270, B:>=240, C:其他)")
def get_grade_v2(total):
    if total >= 270:
        return 'A'
    elif total >= 240:
        return 'B'
    else:
        return 'C'
df['评级2'] = df['总分'].apply(get_grade_v2)
print(df[['姓名', '总分', '评级2']])

# 20
print("\n20. 保存数据到CSV文件,不要索引列")
df.to_csv('E:/codex_projects/ml-learning/students_result.csv', index=False, encoding='utf-8-sig')
print("数据已保存到 students_result.csv 文件中")

print("\n" + "=" * 60)
print("练习完成！")
print("=" * 60)