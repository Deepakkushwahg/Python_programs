f=open('copy_my_intro.txt','r+')
array=[]
for line in f:
    array.append(line)
print(array)
f.close()