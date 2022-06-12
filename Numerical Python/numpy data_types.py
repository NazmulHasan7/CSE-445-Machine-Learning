# Data types in Numpy
import numpy as np
'''
    i - integer             b - boolean
    u - unsigned integer    f - float
    c - complex float       m - timedelta
    M - datetime            O - object
    S - string              U - unicode string
    V - fixed chunk of memory for other type (void)
'''
print(type(10.5))

# array.dtype returns the data type of the array
int_arr = np.array([1, 2, 3, 4, 5])
flt_arr = np.array([1.0, 2, 3.5])
# creating array with datatype: string
str_arr = np.array(['abc', 'def', 'ghi'], dtype='S')

print(int_arr.dtype)
print(flt_arr.dtype)
print(str_arr.dtype)

# converting data type on existing array
org_arr = np.array([1.5, 3.3, 5.7])
new_arr = org_arr.astype('i')
print(org_arr)
print(new_arr)
print(new_arr.dtype)