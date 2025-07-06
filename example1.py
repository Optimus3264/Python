# Create an array containing 250 random floats between 0 and 5:

import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

x=np.random.uniform(0.0,5.0,250)
#plt.plot(x, marker='o')
plt.hist(x, bins=10, color="blue", edgecolor='black')
plt.title("uniform")
plt.xlabel("a")
plt.ylabel("b")
plt.grid(True)
plt.show()

