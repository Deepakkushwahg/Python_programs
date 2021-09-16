# program to display fabonocai series
n=int(input("Enter the number of digit\n"))
a=0
b=1
print("Fabonaci series is")
print(a,end=' ')
while(n-1>0):
    c=a
    a=a+b
    b=c
    print(a,end=' ')
    n=n-1	
