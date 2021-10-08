import random


def main():
    play_again = 'y'
    score = 300
    first_card = random.randint(1, 13)
    while play_again.lower() != 'n':
        print()
        print(f"Number: {first_card}")
        print(f"Your score: {score}")
        h_l = input("Do you think the next card is high or low(h/l): ")
        returned = check_guess(h_l, first_card, score)
        first_card = returned[1]
        score = returned[0]
        print()
        if score > 0:
            play_again = input("Do you want guess again (y/n): ")
        else:
            print(f"Your score is {score}, you have lost.")
            exit()


def check_guess(h_l, first_card, score):

    second_card = random.randint(1, 13)
    print(second_card)
    if h_l.lower() == "h":
        if second_card > first_card:
            print()
            print("Correct!")
            score += 100
            print(f"Your current score is {score}")
            print()
        elif second_card < first_card:
            print()
            print("Wrong!")
            score -= 75
            print(f"Your current score is {score}")
            print()
        elif second_card == first_card:
            print()
            print("They are equal")
            print()
    elif h_l.lower() == "l":
        if second_card < first_card:
            print()
            print("Correct!")
            score += 100
            print(f"Your current score is {score}")
            print()
        elif second_card > first_card:
            print()
            print("Wrong!")
            score -= 75
            print(f"Your current score is {score}")
            print()
        elif second_card == first_card:
            print()
            print("They are equal")
            print()
    elif h_l != "h" or h_l != "l":
        print()
        print("Something went wrong...")
        print()
    first_card = second_card
    return score, first_card


== == == =
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

    card = random.randint(1, 13)

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
