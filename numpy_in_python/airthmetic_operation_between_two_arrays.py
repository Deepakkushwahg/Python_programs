# program to perform airthmetic operation between two arrays
import numpy as np
r, c=map(int, input().split())
lst1=[]
lst2=[]
for i in range(r):
    ls1=list(map(int, input().split()))
    lst1.append(ls1)
for i in range(r):
    ls2=list(map(int, input().split()))
    lst2.append(ls2)
arr1=np.array(lst1)
arr2=np.array(lst2)
print("Addition of arrays is\n",np.add(arr1,arr2))
print("Substraction of arrays is\n",np.subtract(arr1,arr2))
print("Multiplication of arrays is\n",np.multiply(arr1,arr2))
print("Division of arrays is\n",np.floor_divide(arr1,arr2))
print("Modulus of arrays is\n",np.mod(arr1,arr2))
print("Power of arrays is\n",np.power(arr1,arr2))