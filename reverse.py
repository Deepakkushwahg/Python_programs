# program to display reverse of a number 
n=int(input("Enter the number: "))
i=0
print("Number before reverse =", n)
while(n>0):
    r=n%10
    i=i*10+r
    n=n//10
print("Number after reverse =", i)