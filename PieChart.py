import matplotlib.pyplot as plt

slices = [30, 25, 20, 25]
labels = ['Apple', 'Banana', 'Mango', 'Grapes']
colors = ['red', 'yellow', 'orange', 'purple']

plt.pie(slices, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart Example")
plt.show()
