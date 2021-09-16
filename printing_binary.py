# Q:2 (c)
l=1
n=int(input("Enter the size : "))
for i in range(n):
    binary=0
    m=1
    while(l!=0):
        r = l%2
        l = l//2
        binary = binary+(r*m)
        m = m*10
    print(binary)
    l=4*l+1
    
