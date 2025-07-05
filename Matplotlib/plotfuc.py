import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales = [10, 25, 20, 35, 40]
plt.plot(months, sales,color='blue',linestyle='--',marker='o',linewidth=2,label='Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.legend(loc='upper left')
plt.grid(True,color='gray',linestyle='-',linewidth=1)
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May'])  # Custom x-tick labels
plt.show()