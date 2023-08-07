a=int(input())
b=int(input())
l=[]
for i in range(1,a):
    if a%i==0:
       l.append(i) 
m=[]
for i in range(1,b):
    if b%i==0:
        m.append(i)
c=sum(l)
d=sum(m)
if a==d and b==c:
    print("Amicable")
else:
    print("Not Amicable")