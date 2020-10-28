import pulp

ans = pulp.LpProblem("Problem",pulp.LpMaximize)

A = pulp.LpVariable("internet",lowBound = 0)
B = pulp.LpVariable("print",lowBound = 0)

# Maximize
ans += 3000*A + 900*B

# Constraints
ans += 3000*A + 900*B <= 75000
ans += B - 5*A >= 0
ans += 5 >= A <= 15
ans += A >= 0
ans += B >= 0

# show
print(ans)

# result
status = ans.solve()
# print(pulp.LpStatus[status])

# show ans
print("Internet :",pulp.value(A),"   Print :",pulp.value(B),"   Max :",pulp.value(ans.objective))

