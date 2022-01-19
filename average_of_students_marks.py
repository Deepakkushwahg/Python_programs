# program to find average of students marks
n=int(input("Enter No. of student: "))
marks=[]
for i in range(0,n):
    ls=list(input().split(' '))
    marks.append(ls)
    ls.clear
student=input("Enter student name whose average marks you want: ")
s=0
c=0
for i in marks:
    if(i[0]==student):
        for k in range(0,len(i)-1):
            s=s+float(i[k+1])
            c=c+1
print("{:.2f}".format(s/c))
