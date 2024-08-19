import numpy as np
import matplotlib.pyplot as plt

# creating a list of
# uniformly distributed values
uniform = np.arange(-100, 100)

# creating a list of normally
# distributed values
normal = np.random.normal(size = 100)*30

# creating figure and axes to
# plot the image
fig, (ax1, ax2) = plt.subplots(nrows = 1,
                            ncols = 2,
                            figsize =(9, 4),
                            sharey = True)

# plotting violin plot for
# uniform distribution
ax1.set_title('Uniform Distribution') 
ax1.set_ylabel('Observed values')
ax1.violinplot(uniform)

# plotting violin plot for
# normal distribution
ax2.set_title('Normal Distribution')
ax2.violinplot(normal)

# Function to show the plot
plt.show()