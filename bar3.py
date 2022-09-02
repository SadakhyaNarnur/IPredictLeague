# libraries
import numpy as np
import matplotlib.pyplot as plt

# Make a fake dataset
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=['black', 'red', 'green', 'blue', 'gray'])
plt.xticks(y_pos, bars)
plt.show()
