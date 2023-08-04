n=int(input())
s=pow(n,2)
c=0
while s>0:
    x=s%10
    c+=x
    s=s//10
if c==n:
    print("Neon Number")
else:
    print("Not Neon Number")