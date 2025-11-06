

import array


arr = array.array('i', [10, 20, 30, 40, 50])


print("Array elements:")
for i in arr:
    print(i)


arr.insert(2, 25)
print("\nAfter insertion:", arr.tolist())


arr.remove(40)
print("After removal:", arr.tolist())

print("Element at index 3:", arr[3])


arr[0] = 5
print("After updating:", arr.tolist())
