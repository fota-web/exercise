import pulp

ans = pulp.LpProblem("Problem",pulp.LpMinimize)

A = pulp.LpVariable("A",lowBound = 0)
B = pulp.LpVariable("B",lowBound = 0)

# Minimize
ans += 0.10*A + 0.15*B

# Constraints
ans += 5*A + 10*B >= 45
ans += 4*A + 3*B >= 24
ans += 0.5*A >= 1.5
ans += A >= 1.5
ans += B >= 0

# show
print(ans)

# result
status = ans.solve()
# print(pulp.LpStatus[status])

# show ans
print(pulp.value(A),pulp.value(B),pulp.value(ans.objective))

