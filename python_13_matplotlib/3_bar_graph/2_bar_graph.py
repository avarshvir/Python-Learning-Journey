import matplotlib.pyplot as plt
categories = ['Data Analysis', 'Data Science', 'Machine Learning', 'Deep Learning', 'AI', 'Electronics', 'Embedded System', 'IoT', 'Robotics']
values = [1,2,3,4,5,6,7,8,9]

plt.barh(categories,values,color='green')
plt.title('Barh')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()