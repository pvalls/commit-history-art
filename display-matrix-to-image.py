from matplotlib import pyplot as plt
import numpy as np


data = [
[1,4,4,4,1,1,4,4,1,4,4,1,1,1,1,4,4,4,4,1,4,4,4,1,4,4,4,1,1,1,1,4,1,1,4,1,1,1,4,4,4,4,4,4,1],
[1,1,4,1,1,4,3,3,4,3,3,4,1,1,4,1,1,1,1,1,1,4,1,1,1,4,1,1,1,1,4,4,4,4,4,4,1,1,4,3,3,3,3,4,1],
[1,1,4,1,1,4,3,3,3,3,3,4,1,1,4,1,1,1,1,1,1,4,1,1,1,4,1,1,1,1,4,1,3,3,1,4,1,1,4,1,3,3,1,4,1],
[1,1,4,1,1,4,2,2,3,2,2,4,1,1,4,1,4,4,1,1,1,4,1,1,1,4,1,1,4,1,4,4,4,4,4,4,1,1,4,3,3,3,3,4,1],
[1,1,4,1,1,1,4,2,2,2,4,1,1,1,4,1,1,1,4,1,1,4,1,1,1,4,1,1,1,4,1,1,4,4,1,1,1,1,4,4,4,4,4,4,1],
[1,1,4,1,1,1,1,4,2,4,1,1,1,1,4,1,1,1,4,1,1,4,1,1,1,4,1,1,1,1,4,4,4,4,4,1,1,1,1,1,4,4,1,1,1],
[1,4,4,4,1,1,1,1,4,1,1,1,1,1,1,4,4,4,4,1,4,4,4,1,1,4,1,1,1,1,1,1,4,4,4,1,1,1,4,4,4,4,4,4,1]
]

data = np.divide(data, max(max(data)))

plt.imshow(data, cmap='Greens', interpolation='nearest')
plt.show()
