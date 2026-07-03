#This is day five of my learning to code journey. Today, I will be creating a Word Frequency Counter. :)

text = input("enter a sentence: ")
words = text.lower().split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1
print("\nWord counts:")
for word, count in frequency.items():
    print(f" {word}: {count}")
most_common = max(frequency, key=frequency.get)
print(f"\nMost used word: '{most_common}' ({frequency[most_common]} times)")