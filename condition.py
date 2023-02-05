# write a program to the determine the price of a piza ordered
print("Welcome to DOMINION PIZA!")
email = input("Input your email address: ")
size = input("What size of piza do you want?\nS: for small \nM: for Medium \nL: for large \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
price = 0

if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2
    
elif size == "M":
    price = 20
    if add_pepperoni == "Y":
        price += 3
else:
    size == "L"
    price = 25
    if add_pepperoni == "Y":
        price += 3


# for extra cheese
if extra_cheese == "Y":
    price += 1

print(f"your price for your preferable choice is ${price} \nTHANKS FOR YOUR PRATRONAGE!")
# This is a git practices. This is one that i want 