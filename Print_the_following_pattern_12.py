n= int(input())
a=1
for i in range(n,0,-1):
    for j in range(a,n+1):
        print(j,end=" ")
    a+=1
    print()