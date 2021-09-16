# Q11 program to find no. is prime or not by function
def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=1
    if c==0:
        return 'Prime'
    else:
        return 'not Prime'

n=int(input("Enter the number: "))
result=prime(n)
print("Number is",result)