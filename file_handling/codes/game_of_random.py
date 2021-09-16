import random

v2=random.randrange(1,100)
c=0
while 1:
    v1=int(input('enter'))
    c+=1
    if v1<v2:
        print("No. is smaller")
    elif v1>v2:
        print("No. is greater")
    else:
        print("Right no. with count", c)
        break