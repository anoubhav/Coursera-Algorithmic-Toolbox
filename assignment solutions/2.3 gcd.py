# Python3
a, b = [int(i) for i in input().split()]

# print(a,b)
def euclid_gcd(a, b):
    if b == 0:
        print(a)
        quit()
    c = a%b
    euclid_gcd(b, c)

if a>b:
    euclid_gcd(a, b)
else:
    euclid_gcd(b, a)
