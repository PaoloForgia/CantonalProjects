import pulp as p

problem = p.LpProblem("Bag Problem", p.LpMaximize)

x1 = p.LpVariable("Project 1", cat="Binary")
x2 = p.LpVariable("Project 2", cat="Binary")
x3 = p.LpVariable("Project 3", cat="Binary")
x4 = p.LpVariable("Project 4", cat="Binary")
x5 = p.LpVariable("Project 5", cat="Binary")
x6 = p.LpVariable("Project 6", cat="Binary")
x7 = p.LpVariable("Project 7", cat="Binary")
x8 = p.LpVariable("Project 8", cat="Binary")

# Objective function
problem += 55 * x1 + 75 * x2 + 85 * x3 + 90 * x4 + 67 * x5 + 97 * x6 + 98 * x7 + 59 * x8

# Constraints
problem += x1 == 1  # Project 1 needs to be done
problem += x1 + x2 + x3 >= 1  # At least one project of renewable energy needs to be done
# Max 1 project per company
problem += x2 + x4 <= 1
problem += x5 + x6 <= 1
problem += x3 + x7 <= 1
# Max budget of 1M
problem += 5 * x1 + 7 * x2 + 125 * x3 + 250 * x4 + 25 * x5 + 327 * x6 + 456 * x7 + 250 * x8 <= 1000

status = problem.solve()
print(p.LpStatus[status])

print(x1, ": ", p.value(x1))
print(x2, ": ", p.value(x2))
print(x3, ": ", p.value(x3))
print(x4, ": ", p.value(x4))
print(x5, ": ", p.value(x5))
print(x6, ": ", p.value(x6))
print(x7, ": ", p.value(x7))
print(x8, ": ", p.value(x8))
