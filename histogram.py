import matplotlib.pyplot as plt
import numpy as np

x=np.random.uniform(0.0,5.0,250)

plt.hist(x,5)
plt.show()