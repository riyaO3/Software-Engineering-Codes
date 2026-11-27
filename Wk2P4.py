#This code will try to identify the odd one out of the three sentences

line1 = input("Whats your first sentence? ") #gets the three phrases from use
line2 = input("Whats your second sentence? ")
line3 = input("Whats your third sentence? ")

if line1 == line2: #these check with eachother to see which one is true
    print(line3)
if line2 == line3:
    print(line1)
if line3 == line1:
    print(line2)

