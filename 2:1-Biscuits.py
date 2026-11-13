cost1 = float(input("Cost of packet 1? "))
num1 = int(input("Biscuits in packet 1? "))

cost2 = float(input("Cost of packet 2? "))
num2 = int(input("Biscuits in packet 2? "))

pack1 = cost1/num1
pack2 = cost2/num2

if pack1 > pack2:
    print("packet 1")
if pack2 < pack1:
    print("packet 2")
if pack1 == pack2:
    print("packet 1 or 2")
