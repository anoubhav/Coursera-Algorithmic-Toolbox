# python3
# https://math.stackexchange.com/questions/442459/for-the-fibonacci-numbers-show-for-all-n-f-12f-22-dotsf-n2-f-nf-n1
n = int(input())
lesser_n = n%60
lesser_nplus = (n+1)%60

def fibo(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        c = a+b
        c = c% 10
        b, a = c, b
    return c

if lesser_n<=1:
    a = lesser_n
else:
    a = fibo(lesser_n)
if lesser_nplus<=1:
    b = lesser_nplus
else:
    b = fibo(lesser_nplus)

 
print((a*b)%10)