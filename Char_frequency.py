# Character frequency program

text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:")
for key, value in freq.items():
    print(key, ":", value)
