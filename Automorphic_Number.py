n=int(input())
s=len(str(n))
a=n**2
c=a%pow(10,s)
if c==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")