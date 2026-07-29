# -*- coding: utf-8 -*-
import numpy as np

rng = np.random.default_rng(2024)

sales = np.array([120, 135, 99999, 118, 122, -5, 130, 128, 99999, 125, 0, 132])
sales_clean = sales.copy()
for i in np.where(sales_clean > 1000)[0]:
    sales_clean[i] = (sales_clean[i-1] + sales_clean[i+1]) / 2
sales_clean[sales_clean <= 0] = np.median(sales_clean[sales_clean > 0])
print("Q1-Q3:", sales_clean)
print("mean:", round(sales_clean.mean(), 2))

prices = np.array([100, 102, 101, 105, 108, 107, 110, 115, 112, 118])
dr = (prices[1:] - prices[:-1]) / prices[:-1]
print("Q4 daily return(%):", (dr*100).round(2))
print("Q5 total return(%):", round((prices[-1]/prices[0]-1)*100, 2))
print("Q7 volatility(%):", round(np.std(dr)*100, 2))

scores = np.array([[85,92,78],[90,88,95],[76,65,82],[95,98,92],[68,72,70]])
print("Q12 total:", scores.sum(axis=1))
print("Q13 subject avg:", scores.mean(axis=0).round(1))
z = (scores - scores.mean(axis=0)) / scores.std(axis=0)
print("Q16 Z-score:")
print(z.round(2))

print("Q17 coin:", rng.binomial(1, 0.5, 10000).mean())
d1, d2 = rng.integers(1, 7, (2, 100000))
print("Q18 sum=7:", ((d1+d2)==7).mean())

A = np.array([[1,2,1],[2,3,2],[3,1,1]], dtype=float)
x = np.linalg.solve(A, [10, 17, 13])
print(f"Q20: x={x[0]:.1f} y={x[1]:.1f} z={x[2]:.1f}")

print("=== All answers done! ===")
