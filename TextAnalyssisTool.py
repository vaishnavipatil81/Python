
from collections import Counter

# Step 1: Get paragraph input from user
text = input("Enter a paragraph:\n")

# Step 2: Preprocess the text
# Convert to lowercase for uniformity and split into words
words = text.lower().split()

# Step 3: Count total number of words
total_words = len(words)
print(f"\nTotal number of words: {total_words}")

# Step 4: Count frequency of each word
word_freq = Counter(words)
print("\nWord Frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

# Step 5: Identify and display top 3 most frequent words
top_3 = word_freq.most_common(3)
print("\nTop 3 most frequent words:")
for word, freq in top_3:
    print(f"{word}: {freq}")

# Step 6: Count number of vowels in the entire text
vowels = "aeiou"
vowel_count = 0
for char in text.lower():
    if char in vowels:
        vowel_count += 1

print(f"\nTotal number of vowels: {vowel_count}")
