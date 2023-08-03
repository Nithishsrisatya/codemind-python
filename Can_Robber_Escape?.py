n=int(input())
a=list(map(int,input().split()))
c=0
for j in a:
    if j%2!=0:
            c+=1
if c<=2:
    print("YES")
else:
    print("NO")
            