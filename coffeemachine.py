import sys
import time

menu = """1.latte         :Rp.12000
2.luwak         :Rp.16000
3.cappucino     :Rp.7000
4.black coffee  :Rp.3500"""
    
print("hello welcome to canxer coffee")
name = input("what is your name?\n")
print("Hi " + name, "thanks for coming in our coffee shop\n\n")

order = int(input(name + ", what are you going to order today?\n""menu:\n" + menu + "\n\n""number order : "))

if order == 1: 
    order = 12000
elif order == 2:
    order = 16000
elif order == 3:
    order = 7000
elif order == 4:
    order = 3500
else:
    print("sorry the number you input is not in the menu T_T")
    time.sleep(1)
    sys.exit()
    



print("\n")

quantity = input("how many would you like?\n")

total = order * int(quantity) 
print("\n")

if order == 12000:
    order = "latte"
elif order == 16000:
    order = "luwak"
elif order == 7000:
    order = "cappucino"
elif order == 3500:
    order = "black coffee"



print("ok " + name + " " + str(quantity) + " cup of " + order + " will coming right up\n")
print ("the total will be Rp" + str(total))
