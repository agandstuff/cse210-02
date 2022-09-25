import random

# Card class listing definition and attributes
class Card:
    """Cards which will be represented to the user as numbers 1-13.
    The responsibility of Card is to keep track of the current card number facing up and generating values.
    Attributes:
            value (int): The value of the card.
    """

# Class constructor, with value attribute
    def __init__(self):
        """Constructs a new instance of Card with a value attribute.
        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

# 3) drawCard(self) method. This method generates a new random value.

    def drawCard(self):
        """Generates a new random value.    
        Args:
            self (Card): An instance of Card.
        """
        return (random.randrange(1,13))
