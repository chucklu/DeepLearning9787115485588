import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.linspace(-5, 5, 100)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()