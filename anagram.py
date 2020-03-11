s1=input().strip()
s2=input().strip()
c=0
d=0
if(len(s1)!=len(s2)):
    print("False")
else:
    for i in s1:
        c= c | ord(i)
        #print(c)
    for j in s2:
        d= d | ord(j)
        #print(d)
    if(c==d):
        print("True")
    else:
        print("False")
