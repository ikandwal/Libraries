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
# scores = [55, 65, 75, 85, 95, 60, 70, 80, 90, 100,10, 20, 30, 40, 50]
# plt.hist(scores, bins=5, color='skyblue', edgecolor='black')
# plt.xlabel('Scores')
# plt.ylabel('Frequency')
# plt.title('Distribution of Scores')
# plt.show()

# Scatter Plot
# Uncomment the following lines to create a scatter plot

#plt.scatter(x,y, color='color name', marker='marker style', label='label')
# hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# scores = [55, 65, 75, 85, 95, 60, 70, 80, 90, 100]
# plt.scatter(hours_studied, scores, color='blue', marker='o', label='student scores')
# plt.xlabel('Hours Studied') 
# plt.ylabel('Scores')
# plt.title('Scatter Plot of Study Hours vs Scores')  
# plt.legend() 
# plt.show()

# new example
plt.scatter([1, 2, 3, 4, 5], [10, 25, 20, 35, 40], color='red', marker='x', label='Class A') #G1
plt.scatter([1, 2, 3, 4, 5], [15, 30, 25, 40, 45], color='green', marker='o', label='Class B') #G2
plt.xlabel('Hours Studied') 
plt.ylabel('Scores')
plt.title('Comparison of Class A and Class B')  
plt.grid(True, linestyle='--', alpha=0.5)  # Add grid for better readability
plt.legend() 
plt.show()