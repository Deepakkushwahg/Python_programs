# program to create 2D array by numpy
import numpy as np
lst1=list(map(int, input().split()))
r, c=map(int,input().split())
if r*c==len(lst1):
    ls=[]
    lst=[]
    for i in lst1:
        ls.append(i)
        if(len(ls)==c):
            lst.append(ls)
            ls=[]
arr=np.array(lst)
print(arr)