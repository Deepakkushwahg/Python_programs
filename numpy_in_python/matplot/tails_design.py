import numpy as np
import matplotlib.pyplot as plt
a=np.zeros([100,100])
for j in range(5,91,10):
    for i in range(0,91,5):
        a[i:i+5,i+j:i+j+5]=1
    for i in range(0,91,5):
        a[i+j:i+j+5,i:i+5]=1


plt.imshow(a)
plt.show()