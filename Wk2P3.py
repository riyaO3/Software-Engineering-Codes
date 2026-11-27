#This code will ask for a key and message and scramble it accordingly

def scrambleit(msg,key):
    code = msg[-key:]
    out = code + msg[:len(msg) - key]
    return out

key = int(input("What's the key? "))
msg = input("What's the message? ")

messages = []

while msg != '':
    scram = scrambleit(msg, key)
    messages.append(scram)
    msg = input("What's the message? ")

for m in messages:
    print(m)
