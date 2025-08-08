#while loop

#check no is prime or not
print("PRIME NO Or NOT")
a=int(input("Enter no:"))
if a<2:
    print(a," is not prime no")
else:
    i=2
    is_prime=True
    while i<=a // 2:
     if a % i==0:
         is_prime=False
         break
     i+=1
    if is_prime:
        print(a,"is prime Number ")
    else:
        print(a," is not a Prime Number")
        
        
#Sum of digit of no
print("Sum of digit of no")
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10
print("Sum of digits:", sum_digits)

#check no is palindrome
print("PALINDROME")
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")
    

#Reverse the no
print("REVERSE NO")
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)


#Multiplication table
print("MULTIPLICATION TABLE")
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)


#print largest on n numbers
print("LARGEST NO")
n = int(input("Enter how many numbers: "))
count = 1
largest = None
while count <= n:
    num = int(input(f"Enter number {count}: "))
    if largest is None or num > largest:
        largest = num
    count += 1
print("Largest number is:", largest)


#print smallest of n no
print("SMALLEST NO")
n = int(input("Enter how many numbers: "))
count = 1
smallest = None
while count <= n:
    num = int(input(f"Enter number {count}: "))
    if smallest is None or num < smallest:
        smallest = num
    count += 1
print("Smallest number is:", smallest)
