f=open('copy_my_intro.txt','r+')
print("before read location is",f.tell())
f.read()
print("after read location is",f.tell())
f.close()
if(f.closed):
    print("File is closed")
else:
    print("File is not closed