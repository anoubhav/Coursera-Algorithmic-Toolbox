# Python3
n, W = [int(i) for i in input().split()]
lst = []

if W == 0:
    print(0)
    quit()

for _ in range(n):
    v, w = [int(i) for i in input().split()]
    if v == 0:
        continue
    lst.append((v, w))

lst.sort(key = lambda x: x[0]/x[1], reverse = True)

total_value = 0

for v,w in lst:
    if W==0:
        print(total_value)
        quit()
    amt = min(w, W)
    total_value += amt*v/w
    W -= amt

print(total_value)

