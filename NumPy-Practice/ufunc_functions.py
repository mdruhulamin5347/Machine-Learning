import numpy as np





# create function


# def myadd(x,y,z):
#     return x + y + z

# myadd = np.frompyfunc(myadd, 3, 1)

# print(myadd([1,5,3,5,3],[4,7,5,8,4],[3,6,8,7,6]))








# simple mathmatic operations function

# x = np.array([10, 20, 30, 40, 50, 60])
# y = np.array([2, 1, 2, 3, 4, 5])

# add = np.add(x,y)
# print(add)

# subtract = np.subtract(x,y)
# print(subtract)

# multiply = np.multiply(x,y)
# print(multiply)


# divide = np.divide(x,y)
# print(divide)

# power = np.power(x,y)
# print(power)


# mod = np.mod(x,y)
# print(mod)

# remainder = np.remainder(x,y)
# print(remainder)



# divmod = np.divmod(x,y)
# print(divmod)



# z = np.array([-1, -2, 1, 2, 3, -4])

# absolute = np.absolute(z)
# print(absolute)










# Rounding Decimals

# trunc = np.trunc([3.532,6.2342])
# print(trunc)


# fix = np.fix([32.4234,53.23424])
# print(fix)


# around = np.around(3.572,2)
# print(around)

# floor = np.floor([43.324,46.64353])
# print(floor)

# ceil = np.ceil([5.45343,-64.32423])
# print(ceil)










# Logs
# from math import log

# num = np.arange(1,10)
# print(np.log2(num))

# print(np.log10(num))

# print(np.log(num))

# custom = np.frompyfunc(log,2,1)
# print(custom(32,2))









# summations

# x = np.array([3,5,6,4])
# y = np.array([6,3,5,6])

# print(np.sum([x,y]))

# print(np.sum([x,y],axis=1))

# print(np.cumsum([x,y],axis=1))






# NumPy Products

# x = np.array([2,3,5,6,4])
# y = np.array([4,6,4,3,7])

# print(np.prod(x))
# print(np.prod([x,y]))
# print(np.cumprod([x,y],axis=1))







# NumPy Differences

# x = np.array([4,5,6,4])

# print(np.diff(x))
# print(np.diff(x,n=2))









# NumPy LCM Lowest Common Multiple

num1 = 6
num2 = 4
print(np.lcm(num1,num2))

x = np.array([2,3,5,6])
print(np.lcm.reduce(x))