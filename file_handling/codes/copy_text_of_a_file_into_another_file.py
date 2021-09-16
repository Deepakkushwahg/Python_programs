# Write a Python program to copy the contents of a file to another file

f=open('my_intro.txt','r+')
x=open('copy_my_intro.txt','w')
x.write(f.read())
x.close()
f.close()