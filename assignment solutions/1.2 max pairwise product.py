a=int(input())
c=list(input().split())
b=[]
for i in c:
  b.append(int(i))
p1 = max(b)
b.remove(p1)
p2 = max(b)
print(p1*p2)
