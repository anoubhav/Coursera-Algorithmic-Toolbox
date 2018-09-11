#Naive approach
def max_prod_naive(arr):
    product = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            product = max(product,arr[i]*arr[j])
    return product
#Fast approach
def max_prod_fast(arr):
    p1 = max(arr)
    arr.remove(p1)
    p2 = max(arr)
    return p1*p2
#Stress test
from random import randint
def max_prod_stress(N,M):
    while True:
        n = randint(2,N)
        A = [None]*n
        for i in range(n):
            A[i] = randint(0,M)
        print(A)
        result1 = max_prod_naive(A)
        result2 = max_prod_fast(A)
        if result1==result2:
            print('OK')
        else:
            print('Wrong answer:',result1,result2)
            return
max_prod_stress(5,100)
