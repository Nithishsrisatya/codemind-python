def add(n):
    c=0
    while n>0:
        x=n%10
        c+=x
        n=n//10
    return c
def product(n):
    c=1
    while n>0:
        x=n%10
        c*=x
        n=n//10
    return c
n=int(input())
a=add(n)
b=product(n)
c=b-a
print(c)