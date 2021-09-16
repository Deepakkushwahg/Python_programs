# Write a Python program to combine each line from first file with the corresponding line in second file.

f=open('copy_my_intro.txt','r+')
x=open('praveen_intro.txt','r+')
v=open('combined_two_file.txt','w')
for line in f:
    data=line.replace('\n',' ')
    v.write(data+' '+x.readline())
f.close()