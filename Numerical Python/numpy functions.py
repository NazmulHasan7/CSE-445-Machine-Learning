import numpy as np

# copy vs view
# copy owns the data, 
# any changes made to the copy doesn't affect the original array and vice versa
org_arr = np.array([1, 2, 3, 4, 5])
cpy_arr = org_arr.copy()
org_arr[0] = 100
cpy_arr[4] = 50
print('Original: {}'.format(org_arr))
print('Copy: {}'.format(cpy_arr))

# view doesn't own the data, 
# any changes made to the view will affect the original array and vice versa
org_arr = np.array([1, 2, 3, 4, 5])
cpy_arr = org_arr.view()
org_arr[0] = 100
cpy_arr[4] = 50
print('Original: {}'.format(org_arr))
print('View: {}'.format(cpy_arr))

# SHAPE
arr_5d = np.array([1, 2, 3, 4], ndmin=5)
print(arr_5d)
print('Shape: {}'.format(arr_5d.shape))

# RESHAPE: One dimension to another dimension
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# reshape to 3x3 array: 3 arrays, each with 3 elements
reshaped_2d_arr = arr_1d.reshape(3, 3)
print('Original: {}'.format(arr_1d))
print('Reshaped 2D: {}'.format(reshaped_2d_arr))

# reshape to 3x3x1 array: outermost has 3 arrays that contains 3 arrays each with 1 element
reshaped_3d_arr = arr_1d.reshape(3, 3, 1)
print('Reshaped 3D: {}'.format(reshaped_3d_arr))

# unknown dimension
# pass -1, numpy calculates the number
new_arr = arr_1d.reshape(9, 1, -1)
print(new_arr)

# flattening the array
flattened_arr = new_arr.reshape(-1)
print('Flattened: {}'.format(flattened_arr))