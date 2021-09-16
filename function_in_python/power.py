# Q10 program to find power by function
power=lambda a, b :  a**b
a, b=map(int, input("Enter the numbers\n").split())
p=power(a, b)
print(f"Power of a number raised to other is {p}")
