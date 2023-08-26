val=43
x=3
for i in range(5,val,7):
 x+=2
 if((x+i)%2==1):
     print(val-i)
 else:
     print(x)
