import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D', 'E']
y = [23, 45, 56, 78, 33]

plt.bar(x, y, color='orange', width=0.5)
plt.title("Bar Graph Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
