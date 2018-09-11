#Python3
n = int(input())
count = 0
for i in [10, 5, 1]:
    if n>=i:
        q = n//i
        count += q
        n = n%i
        if n==0:
            print(count)
            quit()

