# Python3

a, b = [int(i) for i in input().split()]

def euclid_gcd(a, b):
    if b == 0:
        return a
    c = a%b
    return euclid_gcd(b, c)

if a>b:
    gcd = euclid_gcd(a, b)
else:
    gcd = euclid_gcd(b, a)

print(a*b//gcd)