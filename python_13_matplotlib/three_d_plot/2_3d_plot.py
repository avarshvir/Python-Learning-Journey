import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Generate sample data
np.random.seed(0)  # For reproducibility
x = np.random.standard_normal(100)  # 100 random values for x-axis
y = np.random.standard_normal(100)  # 100 random values for y-axis
z = np.random.standard_normal(100)  # 100 random values for z-axis

# Create a figure
fig = plt.figure()

# Add 3D axes
ax = fig.add_subplot(111, projection='3d')

# Create a 3D scatter plot
ax.scatter(x, y, z, c='blue', marker='o')

# Add titles and labels
ax.set_title('3D Scatter Plot')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Show the plot
plt.show()
