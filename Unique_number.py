n=int(input())
s=str(n)
c=set(s)
if len(s)==len(c):
    print("Unique Number")
else:
    print("Not Unique Number")