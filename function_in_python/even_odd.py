# Q9 program to find even or odd by function
def even_odd(n):
    if(n%2==0):
        return "even"
    else:
        return "not even"
    
n=int(input("Enter the number: "))
v=even_odd(n)
print(f"Number is {v}")
