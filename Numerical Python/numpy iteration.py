import numpy as np
# numpy array iteration

arr_1d = np.array([1, 2, 3, 4, 5])
print('1D array: ',end='')
for element in arr_1d:
    print(element, end='')

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print('\n2D array:')
for element in arr_2d:
    print(element)
print('Scalar: ', end='')
for array in arr_2d:
    for element in array:
        print(element, end='')

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('\n3D array:', end='')
for element in arr_3d:
    print(element)
print('Scalar: ', end='')
for array_2d in arr_3d:
    for array_1d in array_2d:
        for element in array_1d:
            print(element, end='')


# iterating using nditer()
print('\nElement wise:', end='')
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for element in np.nditer(arr):
    print(element, end='')