#Q:6
age1=int(input("Enter the age of first people\n"))
age2=int(input("Enter the age of second people\n"))
age3=int(input("Enter the age of third people\n"))
if(age1>age2):
    if(age1>age3):
        print("First people is oldest")
        if(age2>age3):
            print("Third people is youngest")
        else:
            print("Second people is youngest")
    else:
        print("Third people is oldest")
        print("Second people is youngest")
else:
    if(age2>age3):
        print("Second people is oldest")
        if(age1>age3):
            print("Third people is youngest")
        else:
            print("First people is youngest")
    else:
        print("Third people is oldest")
        print("First people is youngest")
