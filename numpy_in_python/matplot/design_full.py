import numpy as np
import matplotlib.pyplot as plt
import math
a=np.zeros([100,100])
a[:18,0:18]=1
a[83:,0:18]=1
a[83:,83:]=1
a[0:18:,83:]=1
a[30:70,30:70]=1
a[35:65,0:10]=1
a[0:10,35:65]=1
a[35:65,90:]=1
a[90:,35:65]=1
a[25,25:75]=1
a[25:75,25]=1
a[75,25:76]=1
a[25:75,75]=1
a[31,0:14]=1
a[31:69,13]=1
a[69,0:14]=1
a[31,86:]=1
a[31:69,86]=1
a[69,86:]=1
a[86,31:69]=1
a[86:,31]=1
a[86:,69]=1
a[0:14,31]=1
a[14,31:70]=1
a[0:14,69]=1
a[22,0:21]=1
a[0:22,21]=1
a[0:21,79]=1
a[21,79:]=1
a[79,0:21]=1
a[79:,21]=1
a[22,0:22]=1
a[79,79:]=1
a[79:,79]=1
plt.imshow(a)
plt.show()