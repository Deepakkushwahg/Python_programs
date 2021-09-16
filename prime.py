# program to check no. is prime or not
n=int(input())
f=0
for i in range(2,n,1):
    if(n%i==0):
        f=1
if(f==0):
    print("Number is prime")
else:
    print("Number is not prime")
