import numpy as np

print("=" * 60)
print("  NumPy Complete Review (v" + np.__version__ + ")")
print("=" * 60)

# 1. Creating arrays
print("\n" + "#" * 60)
print("# 1. Creating arrays")
print("#" * 60)

print("\n--- From lists ---")
print(np.array([1, 2, 3, 4, 5]))
print(np.array([[1, 2], [3, 4]]))

print("\n--- Common initializers ---")
print("zeros(2,3):")
print(np.zeros((2, 3)))
print("ones(3,2):")
print(np.ones((3, 2)))
print("eye(3):")
print(np.eye(3))
print("full((2,3), 7):")
print(np.full((2, 3), 7))

print("\n--- Sequences ---")
print("arange(0,10,2):", np.arange(0, 10, 2))
print("linspace(0,1,5):", np.linspace(0, 1, 5))

# 2. Array properties
print("\n" + "#" * 60)
print("# 2. Array properties")
print("#" * 60)

arr = np.random.randint(0, 101, (4, 5))
print("arr:")
print(arr)
print("shape:", arr.shape)
print("ndim:", arr.ndim)
print("size:", arr.size)
print("dtype:", arr.dtype)

# 3. Indexing
print("\n" + "#" * 60)
print("# 3. Indexing & Slicing")
print("#" * 60)

arr = np.arange(12).reshape(3, 4)
print("arr:")
print(arr)
print("arr[1,2]:", arr[1, 2])
print("arr[0,:]:", arr[0, :])
print("arr[:,1]:", arr[:, 1])
print("arr[:2,:2]:")
print(arr[:2, :2])
print("arr[::-1] (reverse rows):")
print(arr[::-1])
print("fancy index arr[[0,2]]:")
print(arr[[0, 2]])
print("boolean arr[arr > 5]:", arr[arr > 5])

# 4. Shape ops
print("\n" + "#" * 60)
print("# 4. Shape operations")
print("#" * 60)

arr = np.arange(12)
print("arange(12):", arr)
print("reshape(3,4):")
print(arr.reshape(3, 4))
print("reshape(-1,4):")
print(arr.reshape(-1, 4))

arr2d = arr.reshape(3, 4)
print("flatten:", arr2d.flatten())
print("T (transpose):")
print(arr2d.T)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("vstack:")
print(np.vstack((a, b)))
print("hstack:")
print(np.hstack((a, b)))

# 5. Math
print("\n" + "#" * 60)
print("# 5. Math operations")
print("#" * 60)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a:", a)
print("b:", b)
print("a+b:", a + b)
print("a-b:", a - b)
print("a*b:", a * b)
print("a/b:", a / b)
print("a**2:", a ** 2)
print("a+10:", a + 10)

print("\n--- Matrix multiply ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("A @ B:")
print(A @ B)

# 6. Broadcasting
print("\n" + "#" * 60)
print("# 6. Broadcasting")
print("#" * 60)

print("scalar: [1,2,3] + 10 =", np.array([1, 2, 3]) + 10)
m = np.ones((3, 3))
v = np.array([1, 2, 3])
print("matrix(3x3) + vector(3):")
print(m + v)

# 7. Statistics
print("\n" + "#" * 60)
print("# 7. Statistics")
print("#" * 60)

arr = np.random.randint(1, 101, (4, 5))
print("arr:")
print(arr)
print("sum:", arr.sum())
print("mean:", round(arr.mean(), 2))
print("std:", round(arr.std(), 2))
print("min:", arr.min(), "max:", arr.max())
print("axis=0 (col) mean:", arr.mean(axis=0))
print("axis=1 (row) sum:", arr.sum(axis=1))

# 8. ufunc
print("\n" + "#" * 60)
print("# 8. Universal functions")
print("#" * 60)

arr = np.array([-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0])
print("abs:", np.abs(arr))
print("exp:", np.exp(arr).round(3))
print("clip:", np.clip(arr, -1, 1))
print("sin:", np.sin(arr).round(3))

# 9. Linear algebra
print("\n" + "#" * 60)
print("# 9. Linear Algebra")
print("#" * 60)

A = np.array([[1, 2], [3, 4]])
print("det:", round(np.linalg.det(A), 4))
print("inv:")
print(np.linalg.inv(A))
print("eigvals:", np.linalg.eigvals(A))

# Solve linear system
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print("\nSolve 3x+y=9, x+2y=8")
print("x =", x)
print("verify:", A @ x)

# 10. Random
print("\n" + "#" * 60)
print("# 10. Random numbers")
print("#" * 60)

rng = np.random.default_rng(42)
print("uniform:", rng.random(5).round(3))
print("normal:", rng.normal(0, 1, 5).round(3))
print("integers:", rng.integers(0, 10, 5))

print("\n" + "=" * 60)
print("  Done! Continue to Day 1: Pandas")
print("=" * 60)
