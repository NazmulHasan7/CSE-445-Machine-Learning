
# NumPy introduction
import numpy as np

# Array dimensions
arr_0d = np.array(10)
print('Dimension: {}'.format(arr_0d.ndim))

arr_1d = np.array([1, 2, 3, 4, 5])
print('Dimension: {}'.format(arr_1d.ndim))

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print('Dimension: {}'.format(arr_2d.ndim))

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print('Dimension: {}'.format(arr_3d.ndim))

# Accessing array elements
print(arr_1d[0])
print(arr_2d[0, 2])
print(arr_3d[1, 1, 1])

# Array Slicing - [start:end] or [start:end:step]
arr_org_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr_org_1d[1:5])
print(arr_org_1d[0:7:2])

arr_org_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_org_2d[1, 1:4])
print(arr_org_2d[0:2, 1:4])