#Q:11
age=int(input("Enter your age\n"))
sex=input("Enter your sex or gender\n")
m=input("You have marital status\n")
if(m=='Y'):
    if(sex=='F'):
        print("You will work only in urban areas.")
    elif(sex=='M' and age>=20 and age<40):
        print("You may work in anywhere.")
    elif(sex=='M' and age>=40 and age<60):
        print("You will work in urban areas only.")
    else:
        print("ERROR")
elif(m=='N'):
    print("ERROR")