
add = lambda a, b: a + b
print("Addition:", add(10, 5))

square = lambda x: x * x
print("Square:", square(4))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even)


double = list(map(lambda x: x * 2, numbers))
print("Doubled Numbers:", double)
