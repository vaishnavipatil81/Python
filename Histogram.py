import matplotlib.pyplot as plt

data = [12, 15, 17, 18, 19, 21, 21, 22, 25, 25, 27, 28, 30]

plt.hist(data, bins=5, color='green', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Data Range")
plt.ylabel("Frequency")
plt.show()
