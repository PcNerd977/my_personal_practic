import os
# I want to write a code to determine the highest bidder

print("Let's make a bid for this valuable object:\n")


# I can actually define a function here, which will perform all the functions
# The function will take the input and add to a dictionary 
highest_bidder = 0
user_dictionary = {}
def user_bids(user, amount,):
    
    user_dictionary[name] = amount
    bid_amount = user_dictionary[name]
    return bid_amount
    
def clear():
    """
    This is a clear fuctnion, you can use it to clear the console
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Then create a while loop, which will have the condition, that will end the loop if user input is no
# Then clear the console.
# when the user enter no, then the program should return the highest bidder "This is where the changes occur"
end_game = 'y'
while end_game == 'y':
    name = input("Enter you name: \n")
    bid_amount = int(input("Enter you bid amount:\n$ "))
    continue_biding = input("Are there any other bidders? 'y' or 'n':\n ")

    user_amount = user_bids(user = name, amount = bid_amount)
    if user_amount > highest_bidder:
        user_with_the_highest_bidder = name
        highest_bidder = user_amount
    if continue_biding == 'n':
        end_game = 'n'
    elif continue_biding == 'y':
        clear()


print(f"The winner of the bid is {user_with_the_highest_bidder} with ${highest_bidder}")
# how do i want to select the user with the highest bid_amount

