import numpy as np

def learning_from_observations(X, y, n_features, n_samples):
  """
  Simulates the process of learning from observations in supervised learning.

  Args:
    X: A 2D numpy array of shape (n_samples, n_features) representing the input data.
    y: A 1D numpy array of shape (n_samples,) representing the target output values.
    n_features: The number of features in the input data.
    n_samples: The number of samples in the training data.

  Returns:
    None.
  """

  # Print the basic information about the data.
  print("Data shape:", X.shape)
  print("Target shape:", y.shape)

  # Visualize the data (if possible).
  if n_features == 2:
    import matplotlib.pyplot as plt
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Visualization of the data")
    plt.show()

  # Define a simple learning algorithm (e.g., linear regression).
  def linear_regression(X, y):
    # Add a column of ones for the bias term.
    X_with_bias = np.hstack((np.ones((n_samples, 1)), X))

    # Calculate the weights using the closed-form solution.
    w = np.linalg.inv(X_with_bias.T @ X_with_bias) @ X_with_bias.T @ y

    return w

  # Train the learning algorithm.
  w = linear_regression(X, y)

  # Print the learned weights.
  print("Learned weights:", w)

  # Make predictions on new data (if available).
  # ...

# Example usage:
n_features = 2
n_samples = 100

# Generate random data.
X = np.random.rand(n_samples, n_features)
y = np.sin(3 * X[:, 0]) + np.cos(2 * X[:, 1])

learning_from_observations(X, y, n_features, n_samples)