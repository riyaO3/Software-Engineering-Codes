##Test Case 1:
#input: Yarr Har
#output: 1

#Test Case 2:
#input: Ahoy m'hearties
#Yo ho ho and a bottle of rrrrum
#Tharrrr be th' treature
#output: 2

##Test Case 3:
#input: hello, how are you
#output: 0

#Test Case 4:
#input:
#output: 0 

#Problem 1: Count the double r's in a line
#Problem 2: let the user put in more than 1 line until a blank line


prompt = input(" ")
counter = 0

while prompt != ' ':
    if 'rr' in prompt:
        counter += 1
    else:
        counter = counter  
    


    
