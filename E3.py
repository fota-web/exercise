import pulp

ans = pulp.LpProblem("Problem",pulp.LpMinimize)

A = pulp.LpVariable("C-30",lowBound = 0)
B = pulp.LpVariable("C-92",lowBound = 0)
C = pulp.LpVariable("D-21",lowBound = 0)
D = pulp.LpVariable("E-11",lowBound = 0)


# Maximize
ans += 0.12*A + 0.09*B + 0.11*C + 0.04*D

# Constraints
ans += D >= 7.5
ans += A + B >= 22.5
ans += B + C <= 15
ans += A + B + C + D == 50
ans += A >= 0
ans += B >= 0
ans += C >= 0
ans += D >= 0

# show
print(ans)

# result
status = ans.solve()
# print(pulp.LpStatus[status])

# show ans
print(pulp.value(A),pulp.value(B),pulp.value(C),pulp.value(D),pulp.value(ans.objective))

