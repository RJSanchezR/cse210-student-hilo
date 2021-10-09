import random

class Dealer:
    """A code template for the Dealer. The responsability of this class
    of objects is to draw the cards, ask the users input, the score and
    if users want/can keep playing or not.
    """
    
    def __init__(self):
        """The class constructor.

        Args:
            Self (Dealer): An instance of Dealer.
        """
        self.score = 300
        self.new_card = random.randint(1,13)
        # The current card will always be the new card before it changes
        self.current_card = self.new_card

    
    def draw_card(self):
        """Assign a random card (number) to the new card
        
        Args:
            Self (Dealer): An instance of Dealer.
        """

        self.new_card = random.randint(1, 13)

    
    def get_guess(self):
        """Determines if the user can throw again. Returns True or False.

        Args:
            Self (Dealer): An instance of Dealer.

        Returns:
            string: The user guess for lower or higher.
        """
        user_guess = input("Do you think the next card will be higher or lower? [h/l]: ")

        return user_guess
    

    def calculate_points(self, guess):
        """Calculates the number of points after the guess. 100 points 
            if correct, -75 points if incorrect. Returns an integer.

        Args:
            Self(Dealer): An instance of Dealer.

        Return:
            number: The points earn after guess.
        """
        if guess == "h":
            if self.new_card > self.current_card:
                return 100
            elif self.new_card == self.current_card:
                print("The cards changed, the score will stay the same.")
            else:
                return (-75)
        
        elif guess == "l":
            if self.new_card < self.current_card:
                return 100
            elif self.new_card == self.current_card:
                print("The cards changed, the score will stay the same.")
            else:
                return (-75)

    
    def can_play(self):
        """Determines whether or not the Dealer can draw a card according
        to the rules.
        
        Args:
            Self (Dealer): An instance of Dealer.
        
        Returns:
            boolean: True if the player has more than 0 points;
            false otherwise.
        """
        return (self.score > 0)