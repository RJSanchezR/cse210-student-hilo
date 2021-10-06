# TODO: Add entry point code here

import random

'''
    Dealer
    player
    keep track of score
    changes score
    can tell between bigger and smaller (check)
    generate random number
    play again (y/n)
    game over at 0
'''
def main():

    card = random.randint(1,13)

    def player_score():
        player_score = 300



    def player_guess(card, player_score):
        print(f"The card is: {card}")
        guess = int(input("Higher or lower? [h/l] "))
        new_card = random.randint(1, 13)
        if guess.lower() == "h":
            
            if new_card > card:
                score += 100
                print(score)
            elif new_card < card:
                score -= 75
                print(score)
            else:
                print("your card was the same, try again")
        elif guess.lower() == "l":
            if
        
        



    def play_again():
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() == "y":
            player_guess(card, player_score)
        elif play_again.lower() == "n":
            quit()
        else:
            print("error, please type either 'y' or 'n' ")

main()











