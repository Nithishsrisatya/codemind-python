h,m=map(int,input().split(":"))
ma=m*6
ha=h*30+m*0.5
a=max(ha,ma)-min(ha,ma)
b=360-a
print(min(a,b))