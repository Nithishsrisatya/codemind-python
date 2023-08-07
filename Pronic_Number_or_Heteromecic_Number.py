n=int(input())
c=0
for i in range(n+1):
    if (i*(i+1))==n:
        c+=1
        break
    else:
        c=0
if c==1:
    print("YES")
else:
    print("NO")