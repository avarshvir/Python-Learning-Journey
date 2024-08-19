import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # X-axis values
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Y-axis values

x2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # X-axis values
y2 = [4, 6, 10, 20, 22, 26, 19, 22, 23, 29]  # Y-axis values

# Create a scatter plot
plt.scatter(x, y, color='blue', edgecolor='black')
plt.scatter(x2, y2, color='red', edgecolor='black')
# Add titles and labels
plt.title('Scatter Plot Example')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Show the plot
plt.show()
