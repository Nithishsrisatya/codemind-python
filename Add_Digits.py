def d(n):
    c=0
    while n>0:
        x=n%10
        c+=x
        n=n//10
    return c
n=int(input())
while n>10:
    n=d(n)
print(n)
