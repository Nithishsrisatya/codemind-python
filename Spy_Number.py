def palin(n):
    c=0
    while n:
        x=n%10
        c+=x
        n=n//10
    return c
def product(n):
    c=1
    while n:
        x=n%10
        c*=x
        n=n//10
    return c
n=int(input())
c=palin(n)
d=product(n)
if(c==d):
    print("Spy Number")
else:
    print("Not Spy Number")