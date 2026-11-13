#this program will return whether a integer is odd or even based on the user's input
 
#Test 1:
#Input: 5
#Output: This integer is odd.

#Test 2:
#Input: 10
#Output: This integer is even.

#Test 3:
#Input: 0
#Output: This integer is even.

#Test 4:
#Input: 1.2
#Output: This is not an integer, try again.

number = 0
number = int(input("Enter an integer: "))

if number % 2 == 1:
    print("This is an odd number")
elif number % 2 == 0:
    print("This is an even number")
else:
    print("This is no an integer, try again!")

