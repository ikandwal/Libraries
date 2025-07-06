import matplotlib.pyplot as plt

#plt.subplots(nrows, ncols, index)
 
# x= [1, 2, 3, 4, 5]
# y = [10, 25, 20, 35, 40]
# plt.subplot(1,2,1) #1 row, 2 columns, first subplot
# plt.plot(x,y)
# plt.title('Line Plot') #title of the graph
# plt.subplot(1,2,2) #1 row, 2 columns, second subplot
# plt.bar(x,y)
# plt.tight_layout()
# plt.title('Bar Chart') #title of the graph
# plt.show()  # Show the plots

#new way of plotting


x = [1, 2, 3, 4, 5]
y = [10, 25, 20, 35, 40]

fig, axs = plt.subplots(1, 2)  # 1 row, 2 columns

axs[0].plot(x, y)
axs[0].set_title('Line Plot')

axs[1].bar(x, y)
axs[1].set_title('Bar Plot')

plt.tight_layout()
plt.show()