#while loop

#print natural no upto n 
print("Natural nos")
n = int(input("Enter the value of n: "))
i = 1
while i <= n:
    print(i)
    i += 1
    
#print even nos upto n
print("Even nos")
n = int(input("Enter the value of n: "))
i = 2
while i <= n:
    print(i)
    i += 2

#odd nos upto n
print("odd nos")
n = int(input("Enter the value of n: "))
i = 1
while i <= n:
    print(i)
    i += 2

#sum of natural nos upto n
print("Sum of natural nos")
n = int(input("Enter the value of n: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("Sum =", sum)


#sum of odd nos upto n
print("Sum of odd nos")
n = int(input("Enter the value of n: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 2
print("Sum of odd numbers =", sum)



#sum of even nos upto n
print("sum of even nos")
n = int(input("Enter the value of n: "))
i = 2
sum = 0
while i <= n:
    sum += i
    i += 2
print("Sum of even numbers =", sum)


#natural nos upto n in reverse order
print("natural nos upto n reverse")
n = int(input("Enter the value of n: "))
while n >= 1:
    print(n)
    n -= 1

#fibonacci series upto n
print("fibonacci series")
n = int(input("Enter number of terms: "))
a, b = 0, 1
i = 1
while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i += 1


#factorial of no
print("Factorial of no")
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial =", fact)

