n=int(input())
c=0
s=n
while n>0:
    x=n%10
    c=c*10+x
    n=n//10
if(c==s):
    print("True")
else:
    print("False")
    