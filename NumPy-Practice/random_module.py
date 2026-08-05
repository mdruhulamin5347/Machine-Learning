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

# x = random.poisson(lam=2,size=10)
# print(x)

# sns.displot(random.poisson(lam=2,size=1000))
# plt.show()

#Difference Between Normal and Poisson Distribution


# data = {
#   "normal": random.normal(loc=50, scale=7, size=1000),
#   "poisson": random.poisson(lam=50, size=1000)
# }

# sns.displot(data, kind="kde")

# plt.show()




# uniform Distribution

# x = random.uniform(size=(2,3))
# y = random.uniform(low=0,high=10,size=100)
# print(y)

# sns.displot(random.uniform(size=1000), kind='kde')
# plt.show()





#Logistic Distribution

# x = random.logistic(loc=1, scale=2, size=(2,3))
# print(x)


# sns.displot(random.logistic(size=1000), kind='kde')
# plt.show()

# #different between logistic and normal distribution

# data = {
#     "normal" : random.normal(scale=2, size=1000),
#     "logistic" : random.logistic(size=1000)

# }

# sns.displot(data, kind="kde")
# plt.show()






# Multinomial Distribution

# x = random.multinomial(n=5, pvals=[1/5,1/5,1/5,1/5,1/5], size=10)
# print(x)




#Exponential Distribution

x = random.exponential(scale=2,  size=(2,3))
print(x)

sns.displot(random.exponential(size=1000), kind='kde')
plt.show()