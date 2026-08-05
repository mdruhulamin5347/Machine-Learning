import numpy as np





# create function


def myadd(x,y,z):
    return x + y + z

myadd = np.frompyfunc(myadd, 3, 1)

print(myadd([1,5,3,5,3],[4,7,5,8,4],[3,6,8,7,6]))