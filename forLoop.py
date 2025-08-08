#print natural nos upto n
print("NATURAL NOS")
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)
    
    
#print even nos upto n  
print("EVEN NOS")  
n = int(input("Enter a number: "))
for i in range(2, n + 1, 2):
    print(i)
    
#print odd nos upto n
print("ODD NOS")
n = int(input("Enter a number: "))
for i in range(1, n + 1, 2):
    print(i)
    
#print powers of 2 upto n
print("POWER OF 2 UPTO n")
n = int(input("Enter a number: "))
i = 1
while i <= n ** 2:
    print(i)
    i *= 2
    
#Sum the sequence 1 + 1/1! + 1/2! + ... + 1/n!
print("SUM OF SEQ.1 + 1/1! + 1/2! + ... + 1/n! ")
import math

n = int(input("Enter n: "))
sum_series = 0
for i in range(n + 1):
    sum_series += 1 / math.factorial(i)
print("Sum of the sequence:", sum_series) 


#Cosine series: cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ..
print("Cosine series cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ..")
import math

x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms: "))
cos_x = 0

for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    cos_x += term

print("Cos(x):", cos_x)



#chech if square root of no is prime
print("CHECK SQUARE ROOT OF NO ->PRIME OR NOT")
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
sqrt_n = int(math.sqrt(n))

if is_prime(sqrt_n):
    print(f"Square root of {n} is {sqrt_n}, which is prime.")
else:
    print(f"Square root of {n} is {sqrt_n}, which is NOT prime.")
    
    
  #print following design
  #A B C
  #A B C
  #A B C 
for _ in range(3):
    for ch in ['A', 'B', 'C']:
        print(ch, end=' ')
    print()
    
    
   #producing design 
    n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=' ')
    print()

#producing design
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=' ')
    print()


#producing pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


#producing pattern
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=' ')
    print()

