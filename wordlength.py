total = 0
word = ""

word = input("What's the word? ")
total = len(word)

print(f'{word} has {total} characters.')

if total == 0:
    print("Please enter something into the program next time")
else:
    print(f'{word} has {total} characters.')

    
