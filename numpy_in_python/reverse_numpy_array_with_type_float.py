# program to reverse numpy array with type float
import numpy as np
arr=np.array(list(map(float,list(map(int,input().split())))))
print(arr[::-1])