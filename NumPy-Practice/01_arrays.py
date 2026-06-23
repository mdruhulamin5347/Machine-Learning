import numpy as np


# print(np.__version__)   this line check numpy version

list_data = [43,53,5,65,23,64,234,632]
tuple_data = (43,65,45,34,23,64,34,64)
list_arr = np.array(list_data)              # this initialize is 1-D array
tuple_arr = np.array([list_data,tuple_data])   # this is initialize is 2-D array

three_d_arr = np.array([[list_data,tuple_data],[[4,5,3,2,3,4,5,3],[43,53,34,23,43,45,44,34]]])     # this is initialize is 3-D array
# print(list_arr.ndim, " " , tuple_arr.ndim, " " , three_d_arr.ndim) 


higher_dim_arr = np.array([43,53,23,343,23], ndmin=5)
# print(three_d_arr.shape)


# print(list_arr[0] + list_arr[-1])   # array access of numpy
# print(three_d_arr[1,1,-1])            # multi dim array accessing of numpy
# print(three_d_arr[0:2,0:2,2])           # slicing array value of numpy

datatypearr = np.array([4,32,34,52])
# print(datatypearr.dtype)
cparr = datatypearr.copy()
vwarr = datatypearr.view()
cparr[0]=100
vwarr[0]=100
# print(datatypearr)
# print(cparr.base)
# print(vwarr.base)


reshapearr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshapenewarr = reshapearr.reshape(4, 3)
# print(reshapenewarr)
# print(reshapearr.reshape(4, 3).base)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(6)


# arr = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
# newarr = arr.reshape(-1)
# print(newarr)


# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x)


# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   print(x)


# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)



# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#   print(x)


# arr = np.array([1, 2, 3])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)



# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for x in np.nditer(arr[:, ::2]):
#   print(x)



# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for idx, x in np.ndenumerate(arr):
#   print(idx, x)




# arr = np.array(['a', 'b', 'c'])
# for x in arr:
#   print('Hello ' + x)



# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr)



# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)


# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.dstack((arr1, arr2))
# print(arr)