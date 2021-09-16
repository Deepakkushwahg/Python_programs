#Q:9
total=int(input("Enter the number of classes held: "))
attend=int(input("Enter the number of classes attended: "))
per=(attend*100)/total
print("Percentage of class attended is =", per,"%")
if(per<75):
    print("Your attendence is less than 75% so you can not allowed to sit in exam")
    print("If you have madical cause then you will allowed to sit in exam")
    m=input("You have madical cause or not\n")
    if(m=='Y'):
        print("then you will be allowed to sit in exam")
    elif(m=='N'):
        print("then you will not be allowed to sit in exam")
else:
    print("Student is allowed to sit in exam")