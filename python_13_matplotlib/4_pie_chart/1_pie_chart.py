import matplotlib.pyplot as plt
labels = ['Data Analysis', 'Data Science', 'Machine Learning', 'Deep Learning', 'AI']
sizes = [15, 30, 45, 5, 5]  # Corresponding sizes for each category
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']  # Colors for each slice
explode = (0.1, 0, 0, 0, 0)  # "explode" the 1st slice (Data Analysis) slightly

# Create a pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Add a title
plt.title('Pie Chart Example')

# Show the plot
plt.show()
