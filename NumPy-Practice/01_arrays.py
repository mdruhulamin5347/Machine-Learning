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
print(datatypearr.dtype)