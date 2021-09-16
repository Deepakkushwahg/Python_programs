# program to check number is armstrong or not
n=int(input("Enter the number\n"))
x=n
z=n
p=0
a=0
while(x>0):
    x=x//10
    p=p+1
while(z>0):
    r=z%10
    a=r**p+a
    z=z//10
if(a==n):
    print("Number is armstrong")
else:
    print("Number is not armstrong")
