f=open('my_intro.txt','r')
c=0
for line in f:
    c+=1
print(f"No. of lines are {c}")
f.close()