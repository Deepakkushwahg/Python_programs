#Q:3
q=int(input("Enter the no. of quantity which you buy\n"))
c=q*100
if(c>1000):
    d=(c*10)//100
    c=c-d
    print("Total cost is =", c)
else:
    print("Total cost is =", c)