import random

money = 100


# Write your game of chance functions here

def start_coin():
    print("Heads or Tails!\n")
    bet = int(input("How much money do you want to bet?  You currently have " + str(money) + " dollars."))
    choice = int(input("Heads (1) or Tails (2) ?"))
    coin_game(choice, bet)
    another = input("Do you want to play again? (yes or no) ")
    coin_play_again(another)


def coin_flip(input2, bet):
    global money
    result = random.randint(1, 2)
    if input2 == result:
        money += bet
        if result == 1:
            return "You win " + str(bet) + " dollars! It's Heads! You have have " + str(money) + " dollars total!"
        else:
            return "You win " + str(bet) + " dollars! It's Tails! You have have " + str(money) + " dollars total!"
    elif input2 != result:
        money -= bet
        if result == 1:
            return "You lose " + str(bet) + " dollars! It's Heads! You have have " + str(money) + " dollars total!"
        else:
            return "You lose " + str(bet) + " dollars! It's Tails! You have have " + str(money) + " dollars total!"
    else:
        return "Not a valid input, try again"


def coin_game(check, bet):
    # error check if not 1 or 2
    if check >= 3:
        print("Not a valid option")
        choice1 = int(input("Heads (1) or Tails (2) ?"))
        coin_game(choice1, bet)
    # otherwise run the coin flip
    else:
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
