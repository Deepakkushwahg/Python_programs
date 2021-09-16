# Your task is to print an array of size NxM with its main diagonal elements as 1’s and 0’s everywhere else
import numpy as np
r, c=map(int,input().split())
# if(r==c):
#     ls=[]
#     lst=[]
#     for i in range(r):
#         ls.insert(i,1.)
#         for j in range(r):
#             if(j!=i):
#                 ls.insert(j,0.)
#         lst.append(ls)
#         ls=[]
#     arr=np.array(lst)
#     print(arr)

arr=np.eye(r,c)
print(arr)