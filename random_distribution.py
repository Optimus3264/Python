import numpy as np
import matplotlib.pyplot as plt

x=  np.random.normal(5.0,1.0,1000)
y= np.random.normal(10.0,2.0,1000)

plt.scatter(x,y)
plt.show()