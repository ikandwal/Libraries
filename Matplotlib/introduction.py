import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[10,25,20,35,40]
# plt.plot(x, y)
# plt.show()

x= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] #x axis
y = [10, 25, 20, 35, 40] #y axis
plt.plot(x,y)
plt.title('Bakery Sales') #title of the graph
plt.xlabel('Days of the Week') #x axis label
plt.ylabel('Sales per day') #y axis label
plt.show() #show the graph
