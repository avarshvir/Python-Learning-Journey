import matplotlib.pyplot as plt

# Sample data
actual = [3, 5, 2.5, 7, 9]
predicted = [2.8, 5.1, 2.4, 6.8, 8.9]
residuals = [a - p for a, p in zip(actual, predicted)]

# Residual plot
plt.scatter(predicted, residuals, color='blue', edgecolor='black')
plt.axhline(0, color='red', linestyle='--')
plt.title('Residual Plot')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.show()
