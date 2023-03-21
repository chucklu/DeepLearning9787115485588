import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def step_function(x):
    return np.array(x > 0, dtype=np.int)


#x=np.arange(-5,5,0.1)
x = np.linspace(-5, 5, 100)
y = step_function(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
