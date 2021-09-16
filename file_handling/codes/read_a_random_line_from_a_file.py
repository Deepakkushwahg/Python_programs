import random

f=open('copy_my_intro.txt','r+')
lst=f.readlines()
data=random.choice(lst)
print(data)
f.close()