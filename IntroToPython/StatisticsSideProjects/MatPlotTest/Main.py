import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Create a basic line plot
plt.plot(x, y, label='Example Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Line Graph')
plt.legend()
plt.show()