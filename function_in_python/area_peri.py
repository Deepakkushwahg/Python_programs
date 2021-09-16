# function to calculate area and perimeter of a rectangle.
def area_peri(l, b):
    p=2*(l+b)
    a=l*b
    return p, a


l, b=map(int, input("Enter the length and breadth:\n").split())
p, a=area_peri(l, b)
print(f"Perimeter of rectangle is {p} and Area of rectange is {a}")
