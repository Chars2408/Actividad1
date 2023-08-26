v1 = 500
c2 = 75
hj = 12
ef = 3
v2 = 2

for x in range(6):
    c2 = v1 + c2
    hj = (c2 % hj)
    v2 = ef * hj
    if v2 % 2 == 0:
        print(c2)
    else:
        print(10)
