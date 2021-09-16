import numpy as np
arr1=np.array(list(map(float, input().split())))
if np.all(arr1)==False:
    print("Zero exists\nindexes of zeros is ")
    for i in range(len(arr1)):
        if arr1[i]==0:
            print(i,end=' ')
else:
    print("No zeros")
