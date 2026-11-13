#get the word

word = input('Enter in a word: ') #user inputs a word

num = len(word) #variable stores the number of letters in the word

if num <= 3:
    print("Yar") # prints yar only for every number equal or lower than the length 3
else:
    print("Yar" + (num - 3) * "r") # prints every other word + the r's



