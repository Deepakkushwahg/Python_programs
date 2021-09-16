#Q34 program to check the number is perfect number or not
def perfect(n):
    s=0
    i=1
    while(i<n):
        if(n%i==0):
            s=s+i
        i+=1
    if(s==n):
        return True
    else:
        return False

num=int(input("Enter the number whose number is find that it is perfect or not:-\n"))
p=perfect(num)
print("Number is perfect") if(p) else print("Number is not perfect")
