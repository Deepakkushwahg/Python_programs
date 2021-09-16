#Q:8
total=int(input("Enter the number of classes held: "))
attend=int(input("Enter the number of classes attended: "))
per=(attend*100)/total
print("Percentage of class attended is =", per,"%")
if(per<75):
    print("Student will not be allowed to sit in exam")
else:
    print("Student is allowed to sit in exam")