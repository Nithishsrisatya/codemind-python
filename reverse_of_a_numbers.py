n=int(input())
c=0
while n>0:
    x=n%10
    c=c*10+x
    n=n//10
print(c)