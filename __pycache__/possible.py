# sets={}
# length=int(input("Enter length :"))
# for i in range (length):
#   number=int(input(f"Enter {length} digits numbers :"))
#   words=str(input(f"Enter {length} words :"))
#   sets.add(number)
#   sets.add(words)
#   sets.sorted(number)
#   sets.sorted(words)
#   sorted_sets=number+words
#   print(sorted_sets)
# Initialize empty sets for numbers and words
numbers = set()
words = set()

# Ask for the length of inputs
length = int(input("Enter length: "))

# Loop to collect inputs
for i in range(length):
    number = int(input(f"Enter {length} digits number: "))  # Input a number
    word = input(f"Enter {length} words: ")  # Input a word
    numbers.add(number)  # Add the number to the numbers set
    words.add(word)  # Add the word to the words set

# Sort the numbers and words separately
sorted_numbers = sorted(numbers)
sorted_words = sorted(words)

# Combine the sorted results
sorted_result = sorted_numbers + sorted_words

# Print the sorted result
print(sorted_result)