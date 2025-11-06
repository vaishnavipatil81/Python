import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [10, 8, 12, 15, 9, 11]

plt.scatter(x, y, color='red', marker='*', s=100)
plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()
