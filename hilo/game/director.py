from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """

        self.keep_playing = True
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_card()
            self.update_score()
            self.show_outputs()
            self.play_again()

    def get_card(self):
        """Draw a new card at the beginning of each round.
        
        Args:
            self (Director): An instance of Director.
        """
        if self.dealer.new_card == 0:
            self.dealer.draw_card()
            print(f'The card is: {self.dealer.current_card}')
        else:
            print(f'The card is: {self.dealer.current_card}')

    def update_score(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """

        user_guess = self.dealer.get_guess()
        points = self.dealer.calculate_points(user_guess)
        self.dealer.score += points
        
    def show_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the new card for comparisson and the score. 

        Args:
            self (Director): An instance of Director.
        """

        print(f"The new card is: {self.dealer.new_card}")
        print(f"Your score is: {self.dealer.score}")

    def play_again(self):
        """Verify if the users can play again and if they want to do it.

        Args:
            self (Director): An instance of Director.
        """

        if self.dealer.can_play():
            choice = input("Do you want to keep playing? [y/n]: ")
            self.keep_playing = (choice.lower() == 'y')
            if self.keep_playing is not True:
                print("Thanks for playing with us.")
                print(f"Your final score is: {self.dealer.score}")
                self.keep_playing = False
        else:
            print(f"Your final score is: {self.score}")
            self.keep_playing = False