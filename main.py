from pulp import *
from FireflyAlgorithm import FireflyAlgorithm

######################################### Firefly Algorithm #########################################


def Fun(D, x):
    returns = [4.46, 3.246, 5.127, 2.47]
    price = [248.189, 151.986, 85.635, 206.754]
    budget = 40000
    val = 0
    cost = 0
    for i in range(D):
        val += returns[i] * x[i]
        cost += price[i] * x[i]

    val *= -1
    return val if cost <= budget else 0

######################################### LINEAR PROGRAM #########################################


my_lp_problem = pulp.LpProblem("My_LP_Problem", LpMaximize)

# Data definitions
# use 200 day moving average for price
COMPANIES = ['BA', 'APPL', 'XOM', 'GS']
n = len(COMPANIES)
k=4
PRICE = [248.189, 151.986, 85.635, 206.754]
RETURNS = [4.46, 3.246, 5.127, 2.47]
LOWER_BOUND = [20, 50, 100, 55]
UPPER_BOUND = [48, 60, 120, 90]
BUDGET = 40000

# initialise decision variables
x_vars = [pulp.LpVariable('x_'+str(i+1), lowBound=0, cat='Integer') for i in range(n)]
y_vars = [pulp.LpVariable('y_'+str(i+1), lowBound=0, cat='Binary') for i in range(n)]

# Constraints
my_lp_problem += (lpSum([PRICE[i]*x_vars[i] for i in range(n)]) <= BUDGET, "red_constraint")
for i in range(n):
    my_lp_problem += (LOWER_BOUND[i] * y_vars[i] <= x_vars[i], "blue_constraint_"+str(i+1)+"-a")
    my_lp_problem += (x_vars[i] <= UPPER_BOUND[i] * y_vars[i], "blue_constraint_"+str(i+1)+"-b")
my_lp_problem += (lpSum(y_vars) == k, "green_constraint")

# Objective function
my_lp_problem += (lpSum([RETURNS[i] * x_vars[i] for i in range(n)]), "Z")

# Print and solve
print(my_lp_problem)
status = my_lp_problem.solve()

print(f"status: {my_lp_problem.status}, {LpStatus[my_lp_problem.status]}")
print(f"objective: {my_lp_problem.objective.value()}")
for var in my_lp_problem.variables():
    print(f"{var.name}: {var.value()}")
# for name, constraint in my_lp_problem.constraints.items():
#     print(f"{name}: {constraint.value()}")
# my_lp_problem.variables()


######################################### Firefly Algorithm #########################################


Algorithm = FireflyAlgorithm(4, 20, 10000, 0.5, 0.2, 1.0, LOWER_BOUND, UPPER_BOUND, Fun)
Best = Algorithm.Run()
print(Best)
