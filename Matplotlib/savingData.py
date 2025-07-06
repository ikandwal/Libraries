#savefig('filename.png', dpi=value, bbox_inches='tight')
import matplotlib.pyplot as plt
# Example data
x = [1, 2, 3, 4, 5]
y = [10, 25, 20, 35, 40]
# Create a plot
plt.plot(x, y, color='blue', linestyle='--', marker='o', linewidth=2, label='Sales Data')
plt.title('Sales Data Over Time')

plt.xlabel('Time (days)')
plt.ylabel('Sales (units)')
plt.legend(loc='upper left')
plt.grid(True, color='gray', linestyle='-', linewidth=1)    
# Save the plot as a PNG file
plt.savefig('sales_data_plot.png', dpi=300, bbox_inches='tight')
plt.show()