# Write a Python program to append text to a file and display the text

f=open('my_intro.txt','a+')
f.write("\nI want to travel all over world")
f.seek(0,0)
print(f.read())
f.close()
