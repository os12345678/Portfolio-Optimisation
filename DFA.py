from FireflyAlgorithm import *


def Fun(D, x):
    returns = [4.46, 3.246, 5.127, 2.47]
    price = [248.189, 151.986, 85.635, 206.754]
    budget = 33000
    val = 0
    cost = 0
    for i in range(D):
        val += returns[i] * x[i]
        cost += price[i] * x[i]
        return val if cost<=budget else 0


