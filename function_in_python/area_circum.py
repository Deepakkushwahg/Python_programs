# function to calculate area and circumference of a circle.
def area_circum(r):
    a=3.14*r*r
    c=2*3.14*r
    return a, c

r= int(input("Enter the radius of circle: "))
a, c=area_circum(r)
print(f"Area of a circle is {a} and circumference of circle is {c}")
