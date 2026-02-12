# Program to count vowels and consonants

text = input("Enter a string: ")

vowels = 0
consonants = 0

for char in text.lower():
    if char.isalpha():        # check only letters
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
