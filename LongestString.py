#desk check was done before and mistakes were fixed here

#My First Solution 
a = input("first string? ") #variables are made
b = input("second string? ")
c = input("third string? ")

longest = "" #"Longest" is empty as we are setting it to zero to hold other valuables

if len(a) >= len(longest): #put into separate if statements so the computer checks them all
    longest = a
if len(b) > len(longest):
    longest = b
if len(c) > len(longest):
    longest = c

print(f"The longest line was {longest}!") #at the end it prints out the longest line and works!



# can be trunkated (worked together in class)
a = input("first string? ") 
b = input("second string? ")
c = input("third string? ")
longest = a #assume first word is longest

if len(b) > len(longest):
    longest = b
if len(c) > len(longest):
    longest = c
print("The longest line was", longest)
