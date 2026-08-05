import numpy as np





# create function


# def myadd(x,y,z):
#     return x + y + z

# myadd = np.frompyfunc(myadd, 3, 1)

# print(myadd([1,5,3,5,3],[4,7,5,8,4],[3,6,8,7,6]))








# simple mathmatic operations function

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([2, 1, 2, 3, 4, 5])

add = np.add(x,y)
print(add)

subtract = np.subtract(x,y)
print(subtract)

multiply = np.multiply(x,y)
print(multiply)


divide = np.divide(x,y)
print(divide)

power = np.power(x,y)
print(power)


mod = np.mod(x,y)
print(mod)

remainder = np.remainder(x,y)
print(remainder)



divmod = np.divmod(x,y)
print(divmod)



z = np.array([-1, -2, 1, 2, 3, -4])

absolute = np.absolute(z)
print(absolute)