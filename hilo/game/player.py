from game.card import Card


class Player:
    """A person who directs the game. 
    
    The responsibility of the player is to guess higher or lower to try and gain points.

    Attributes:
        Card (object): A single instance of the Card object.
        card1Value (int): Current card/value generated.
        card2Value (int): Previous card/value generated.
        playGame (boolean): Whether or not the game is being played.
        playerChoice(str): Choice of higher or lower.
        currentScore (int): The score for player.
    """

    def __init__(self):
        """Constructs a new Player with score attribute.
        
        Args:
            self (Player): an instance of Player.
        """
        self.card = Card()
        self.currentCard = self.card.drawCard()
        self.previousCard = self.card.drawCard()
        self.playGame = True
        self.playerChoice = ""
        self.currentScore = 300

    def startGame(self):
        """Function to start the game by running the main game loop.
        
        Args:
            self (Player): an instance of Player.
        """
        self.playGame = True

        while self.playGame:
            print("\nThe card is: " + str(self.previousCard))
            self.getInput()
            self.updateGame()
            self.output()
            if self.currentScore == 0:
                self.playGame = False
                break
            playAgain = input("Play again? [y/n] \u00a0")
            if playAgain == "y" or playAgain == "Y":
                continue
            elif playAgain == "n" or playAgain == "N":
                self.playGame = False
                break

    def getInput(self):
        """Ask the user if the next card will be higher or lower.

        Args:
            self (Player): An instance of Player.
        """
        validInput = False

        while validInput == False:
            self.playerChoice = input("Higher or Lower? [h/l] \u00a0")
            if self.playerChoice == "h" or self.playerChoice == "H" or self.playerChoice == "l" or self.playerChoice == "L":
                validInput = True
                return self.playerChoice
            else:
                print("Please choose either H/h or L/l to choose higher or lower.")
       
    def updateGame(self):
        """Checks input against randomly generated card, updates score according to incorrect/correct answer.

        Args:
            self (Player): An instance of Player.
        """
        self.currentCard = self.card.drawCard()

        if self.currentCard > self.previousCard and (self.playerChoice == "h" or self.playerChoice == "H"):
            self.currentScore += 100
        elif self.currentCard < self.previousCard and (self.playerChoice == "l" or self.playerChoice == "L"):
            self.currentScore += 100
        else:
            self.currentScore -= 75

        self.previousCard = self.currentCard

        if self.currentScore <= 0:
            self.currentScore = 0

    def output(self):
        """Displays current card number and current score.

        Args:
            self (Player): An instance of Player.
        """
        print("Next card was: " + str(self.previousCard))
        print("Your score is: " + str(self.currentScore))