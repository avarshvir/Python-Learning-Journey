import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 10.0)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plotting data on each subplot
axs[0, 0].plot(x, y1, 'r')
axs[0, 0].set_title('Sine Wave')

axs[0, 1].plot(x, y2, 'g')
axs[0, 1].set_title('Cosine Wave')

axs[1, 0].plot(x, y3, 'b')
axs[1, 0].set_title('Tangent Wave')
axs[1, 0].set_ylim(-10, 10)  # Limiting y-axis for better visibility

axs[1, 1].plot(x, y4, 'm')
axs[1, 1].set_title('Exponential Growth')

# Adding overall title and labels
fig.suptitle('Various Functions')
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust the layout to fit the suptitle

plt.show()
