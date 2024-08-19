import matplotlib.pyplot as plt
data = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]

plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
