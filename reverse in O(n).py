n=int(input())
l=[]
for i in range(0,n):
    l.append(int(input()))
for i in range(n//2):
    l[i],l[n-1-i]=l[n-1-i],l[i]
print(l)
