#This code is a game that prints all the timestables


counter = 0
num = 0
num = int(input("What times tables would you like? "))
limit = 0
limit = int(input("Up to what number of times tables you would like? "))

while counter != limit: #This will print up to the limit
    counter += 1
    print(f"{num} x {counter} = {num * counter}")

