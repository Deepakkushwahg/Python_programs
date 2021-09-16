import numpy as np
import matplotlib.pyplot as plt
a=np.zeros([100,100])
for i in range(0,91,5):
    a[i:i+5,i+5:i+10]=1
for i in range(0,91,5):
    a[i:i+5,i+15:i+20]=1
plt.imshow(a)
plt.show()