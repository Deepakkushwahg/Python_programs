# program to display 1 to n number which is factor of 5
n=int(input("Enter the limit\n"))
for i in range(1,n+1):
    if(i%5==0 and i%2!=0):
        print(i,end=' ')
