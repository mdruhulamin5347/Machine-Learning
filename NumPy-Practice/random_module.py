from numpy import random
import matplotlib.pyplot as  plt
import seaborn as sns



# normal distribution----------------------------------------------------------

# x = random.normal(loc=1, scale=2, size=(2, 3))

# sns.displot(random.normal(size=(1000)), kind="kde")
# plt.show()




# binomial distribution

# x = random.binomial(n=10, p=0.4, size=20)

# sns.displot(random.binomial(n=10,p=0.5,size=10))
# plt.show()

#Difference Between Normal and Binomial Distribution

# data  = {
#     "normal": random.normal(loc=50,scale=5, size=1000),
#     "binomial": random.binomial(n=100, p=0.5, size=1000)
# }

# sns.displot(data, kind="kde")
# plt.show()





#Poisson Distribution