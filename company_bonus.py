#Q:4
sal=int(input("Enter the salary\n"))
y=int(input("Enter the year of service\n"))
if(y>5):
    bo=(5*sal)//100
    sal=sal+bo
    print("Bonus is =", bo)
    print("Net bonus amount is =", sal)
else:
    print("Bonus is = 0")
    print("Net amount is =", sal)