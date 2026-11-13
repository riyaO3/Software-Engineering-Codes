import math #imports math to use floor

bps = int(input("How many bytes were downloaded in the past second? "))
btg = int(input("How many bytes to go? "))

total = btg/bps #gives us the answer when dividing both

answer = math.floor(total) #floor rounds DOWN to the nearest second

if answer == 1: #this is so we can use 'second' if the total is 1 and 'seconds' if the total is more than 1
    print(f"The download will take approximately {answer} second.")
else:
    print(f"The download will take approximately {answer} seconds.")
