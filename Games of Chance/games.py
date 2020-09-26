import random

money = 100


# Write your game of chance functions here

def start_coin():
    # Starting game logic
    print("Heads or Tails!\n")
    # Take the bet from the user
    bet = int(input("How much money do you want to bet?  You currently have " + str(money) + " dollars.\n"))
    # Make sure the bet is valid
    checked = bet_check(bet, money)
    # If the bet isn't valid, restart the start_coin() function
    if checked:
        print("You don't have that much try again\n")
        start_coin()
    # If the be is valid, continue on
    elif not checked:
        # Take input on heads or tails for the coin and save it to choice
        choice = int(input("Heads (1) or Tails (2) ?"))
        # check to make sure that the user input is valid with coin_game_valid function
        coin_game_valid(choice, bet)
        # make sure we have more than 0 dollars and check if we want to play again
        if money > 0:
            another = input("Do you want to play again? (yes or no) ")
            # take choice and pass to the play again function
            coin_play_again(another)
        else:
            print("Go home your broke")
    else:
        print("Confused")


# lets make sure that we arent betting more than we have
def bet_check(bet, money):
    if bet > money:
        return True
    else:
        return False


def coin_flip(choice, bet):
    # using global money to save the values later
    global money
    # randomize a choice between 1 and 2 and save as result
    result = random.randint(1, 2)
    # if we win
    if choice == result:
        money += bet
        if result == 1:
            return "You win " + str(bet) + " dollars! It's Heads! You have have " + str(money) + " dollars total!"
        else:
            return "You win " + str(bet) + " dollars! It's Tails! You have have " + str(money) + " dollars total!"
    # if we don't win
    elif choice != result:
        money -= bet
        if result == 1:
            return "You lose " + str(bet) + " dollars! It's Heads! You have have " + str(money) + " dollars total!"
        else:
            return "You lose " + str(bet) + " dollars! It's Tails! You have have " + str(money) + " dollars total!"
    # if things get strange
    else:
        return "Not a valid input, try again"


def coin_game_valid(check, bet):
    # error check if not 1 or 2
    if check >= 3:
        print("Not a valid option")
        choice = int(input("Heads (1) or Tails (2) ?"))
        # re-run the check with new choice
        coin_game_valid(choice, bet)
    # otherwise run the coin flip
    else:
        # run the coin flip function normally
        print(coin_flip(check, bet))


def coin_play_again(maybe):
    if money > 0:
        if "y" in maybe:
            start_coin()
        elif "n" in maybe:
            print("Have a good day! You left with " + str(money) + " dollars")
    else:
        print("Go home your broke")


# Call your game of chance functions here

start_coin()
