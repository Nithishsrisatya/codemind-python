n=int(input())
t=n
n=abs(n)
c=0
while(n):
        x=n%10
        c=c*10+x
        n=n//10
if t<0:
    print(c-(2*c))
else:
    print(c)
