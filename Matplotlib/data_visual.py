import matplotlib.pyplot as plt

# Bar Chart
# Uncomment the following lines to create a bar chart

# products = ['Product A', 'Product B', 'Product C', 'Product D']
# sales = [150, 200, 300, 250]
# plt.bar(products, sales, color='skyblue', edgecolor='black',label='Sales Data')
# plt.xlabel('Products')  
# plt.ylabel('Sales')
# plt.title('Product Sales Comparison')
# plt.legend(['Sales Data'])
# plt.show()

#Pie Chart
# Uncomment the following lines to create a pie chart

#plt.pie(sales, labels=products, autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])  this is how you write pie chart

# regions = ['North', 'South', 'East', 'West']
# revenue = [50000, 60000, 70000, 80000]
# plt.pie(revenue, labels=regions, autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
# plt.title('Regional Revenue Distribution')
# plt.show()


# Histogram
# Uncomment the following lines to create a histogram

#plt.hist(data, bins=no. of bins, color='color name', edgecolor='black')
scores = [55, 65, 75, 85, 95, 60, 70, 80, 90, 100,10, 20, 30, 40, 50]
plt.hist(scores, bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.title('Distribution of Scores')
plt.show()
