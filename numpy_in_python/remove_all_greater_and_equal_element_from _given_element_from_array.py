# program to remove all greater and equal element from given element from array
import numpy as np
arr=np.array(list(map(int, input().split())))
num=int(input())
print("Before removing element of array\n",arr)
print("After the removing element of array")
arr1=np.array(list(filter(lambda x:x<num , arr)))
print(arr1)