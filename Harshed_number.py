v=int(input())
t=v
s=0
while(v>0):
    r=v%10
    s=s+r
    v=v//10
if(t%s==0):
    print('True')
else:
    print('False')