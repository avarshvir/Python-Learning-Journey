from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5, 8, 10]
y = [12, 16, 6]

x2 = [6, 9, 11]
y2 = [7, 15, 7]

plt.bar(x, y, color='y', align='center',label='x,y')
plt.bar(x2, y2, color='c', align='center',label='x1,y1')

plt.title('Information')

plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.show()