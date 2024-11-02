# NumPy, short for Numerical Pyton, is a Python library for scientific computing.
# It provides a high-performance multidimensional array object, and tools for working with these arrays.
# 1 NumPy Array
# 1.1 Creation of numpy array
import numpy as np

print('1.1 ', '_' * 20)
a = np.array([1, 2, 3])
b = np.array([1, 2, 3], dtype=np.float32)
print(a, b)  # [1 2 3] [1. 2. 3.]
np.random.seed(0)  # set random seed for reproducibility
rd = np.random.rand(2, 3)  # create a 2x3 array with random values
print(rd)
# [[0.5488135  0.71518937 0.60276338]
# [0.54488318 0.4236548  0.64589411]]

# 1.2 array attributes
print('1.2 ', '_' * 20)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr.shape)  # (2, 3)
print(arr.dtype)  # int64
print(arr.ndim)  # 2
print(arr.size)  # 6
print(arr.itemsize)  # 8 bytes for int64
# 1.3 array indexing
print('1.3 ', '_' * 20)
print(arr[0, 0])  # 1
print(arr[1, 1])  # 5
# 1.4 array slicing
print('1.4 ', '_' * 20)
s1 = arr[0, :]  # [1 2 3]
s1[0] = 10
print(arr)  # [[10 2 3][4 5 6]]
# As we can see, the original array is also changed, because slicing returns a view of the original array, not a copy.
# To avoid this, we can use the copy method.
s2 = arr[0, :].copy()
# 1.5 array reshaping
print('1.5 ', '_' * 20)
print(arr.reshape(3, 2))  # [[10 2][3 4][5 6]]
print('1.6 ', '_' * 20)
# 1.6 array arithmetic
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print(a + b)  # [[6 8][10 12]]
print(a - b)  # [[-4 -4][-4 -4]]
print(a * b)  # [[5 12][21 32]] element-wise multiplication
print(a / b)  # [[0.2 0.33333333][0.42857143 0.5]]
print(a.dot(b))  # [[19 22][43 50]] matrix multiplication
print(a.T)  # [[1 3][2 4]] transpose

# 1.7 array aggregation
print('1.7 ', '_' * 20)
print(arr.sum())  # 30
print(arr.mean())  # 5.0
print(arr.max())  # 10
print(arr.min())  # 2
print(arr.std())  # 2.581988897471611
print(arr.var())  # 6.666666666666667
print(arr.argmax())  # 0
print(arr.argmin())  # 1

# 1.8 equation solving
print('1.8 ', '_' * 20)
a = np.array([[8, 5, 3],
              [7, 6, 9],
              [3, 2, 5]])
b = np.array([315, 154, 110])
x = np.linalg.solve(a, b)
c = np.array([8, 3, 7])
print(c.dot(x))  # [ 86.90909091 -76.27272727   0.36363636]