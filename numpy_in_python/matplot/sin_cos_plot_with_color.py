import numpy as np
import matplotlib.pyplot as plt
x_axis=np.arange(0,11,.1)
y_data1=np.sin(x_axis)
y_data2=np.cos(x_axis)
plt.plot(x_axis,y_data1,color='blue',linewidth=5)
plt.plot(x_axis,y_data2,color='red',linewidth=5)
plt.show()
