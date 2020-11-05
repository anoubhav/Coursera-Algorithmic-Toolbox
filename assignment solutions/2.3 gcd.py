
#python3
#using Euclidean algo
#method to compute gcd
a, b = [int(i) for i in input().split()]
    
def computeGCD(a, b): 
    while(b):
        a, b = b, a % b 
        
    return a 
  
print (computeGCD(a,b)) 
