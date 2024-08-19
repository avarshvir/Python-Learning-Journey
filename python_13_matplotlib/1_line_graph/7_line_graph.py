import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [5,2,6,2]
x2 = [5,7,9,10]
y2 = [1,5,3,7]

plt.plot(x,y,'r',label='line one', linewidth=5)
plt.plot(x2,y2,'b',label='line two', linewidth=5 )
plt.title('Two Line Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(title='Legend Lines')
plt.grid(True,color='k')
plt.show()