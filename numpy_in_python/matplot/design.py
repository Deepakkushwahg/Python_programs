import numpy as np
import matplotlib.pyplot as plt
import math
a=np.zeros([100,100])
a[:20,0:20]=1
a[80:,0:20]=1
a[80:,80:]=1
a[0:20:,80:]=1
a[30:70,30:70]=1
a[35:65,0:10]=1
a[0:10,35:65]=1
a[35:65,90:]=1
a[90:,35:65]=1
plt.imshow(a)
plt.show()