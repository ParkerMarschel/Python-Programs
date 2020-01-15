'''
Lab 10 - Casino Night
Parker Marschel & Casper Johnson
pgm33 & cpj33
Section 4
11/26/17
'''

# Create a class called Card
import random


class Card:
    # Create a list of the order the cards will be in
    card_list = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    # Create just a face card list

    face_card_list = ["Jack", "Queen", "King"]
    # Create the init method

    def __init__(self, card_num):
        # Make sure cards a face - down by default
        self.faceDown = True
        self.card_num = card_num
        # Use an if statment for the first 13 cards
        if self.card_num >= 0 and self.card_num < 13:
            # Set the suit of these first 13 to be Spades
            self.suit = "Spades"
            index_value = self.card_num
            # Index the card list to get the rank by using the variable above
            self.rank = Card.card_list[index_value]
            # Use if conditional if the card in an Ace
            if self.rank == "Ace":
                # Card has a special value of 11
                self.value = 11
            # Use elif conditional if the card is a face card
            elif self.rank in Card.face_card_list:
                # Face cards have special values of 10
                self.value = 10
            # For other cards not Aces or face cards use their given values
            else:
                self.value = self.rank
        # Use elif for 2nd suit
        elif self.card_num >= 13 and self.card_num < 26:
            # Set the suit to Hearts
            self.suit = "Hearts"
            index_value = self.card_num - 13
            # Get rank by indexing as done before
            self.rank = Card.card_list[index_value]
            # Repeat previous steps for this suit
            if self.rank == "Ace":
                self.value = 11
            elif self.rank in Card.face_card_list:
                self.value = 10
            else:
                self.value = self.rank
        # Create third conditonal for 3rd suit
        elif self.card_num >= 26 and self.card_num < 39:
            # Set this suit to be Clubs
            self.suit = "Clubs"
            index_value = self.card_num - 26
            # Get rank by indexing the card list
            self.rank = Card.card_list[index_value]
            # Repeat previous steps for this suit
            if self.rank == "Ace":
                self.value = 11
            elif self.rank in Card.face_card_list:
                self.value = 10
            else:
                self.value = self.rank
        # Last conditional created for 4th suit
        elif self.card_num >= 39 and self.card_num < 52:
            # Set this suit to Diamonds
            self.suit = "Diamonds"
            index_value = self.card_num - 39
            # Get rank by indexing
            self.rank = Card.card_list[index_value]
            # Repeat previous steps for this suit
            if self.rank == "Ace":
                self.value = 11
            elif self.rank in Card.face_card_list:
                self.value = 10
            else:
                self.value = self.rank

    # Create the string class
    def __str__(self):
        # Use conditionals for face - down/ face - up cards
        if self.faceDown is True:
            # Return the string "Face down if the card is not face - up
            return "Face Down"
        else:
            # Return the required message if the card is flipped to face - up
            return (str(self.rank) + " " + "of" + " " + str(self.suit))
    # Create the face_down method from the requirements

    def face_down(self):
        # Set to Boolean value True
        self. faceDown = True
    # Create the face_up method from the requirements

    def face_up(self):
        # Set self.faceDown to Boolean False
        self.faceDown = False
    # Create method to return the suit of the card

    def get_suit(self):
        return self.suit
    # Creat a method to return the rank of the card

    def get_rank(self):
        return self.rank
    # Create a method to return the value of the card

    def get_value(self):
        return self.value

# Create instance variables (Test code for Card class)
if __name__ == "__main__":
    deck = []
    for i in range(52):
        my_card = Card(i)
        deck.append(my_card)
        my_card.face_up()
        print(my_card)
    print(random.choice(deck))
    card = Card(37)
    print(card)
    print(card.get_value())
    print(card.get_suit())
    print(card.get_rank())
    card.face_down()
    print(card)
    card.face_up()
    print(card)


# Create the ChipBank class
class ChipBank:
    # Create the initialize method and pass in paramenter: value
    def __init__(self, value):
        # Create bank balance variable
        self.balance = value
    # Create the withdraw method, pass in amount as an integer

    def withdraw(self, amount):
        # Use if statement if for greater amount than balance in the account
        if amount > self.balance:
            # Create a local variable for max amount that can be taken
            amount_taken = self.balance
            # Set the new balance to 0
            self.balance = 0
            # Return the max amount the user was allowed to take
            return amount_taken
        # Use 2nd conditional for normal withdraw
        else:
            # Create new balance
            self.balance = self.balance - amount
            # Return the amount taken
            return amount

    # Create deopsit method, takes in amount as integer
    def deposit(self, amount):
        # Create new balance
        self.balance = self.balance + amount

    # Create the get_balance method
    def get_balance(self):
        # Return the balance
        return self.balance

    # Create the string method
    def __str__(self):
        # Create variable set to the balance
        chip_val = self.balance
        # Use integer division to get number of chips for each color
        self.black_chip = chip_val // 100
        # Set the new value to the variable being used for each chip
        chip_val %= 100
        self.green_chip = chip_val // 25
        chip_val %= 25
        self.red_chip = chip_val // 5
        chip_val %= 5
        self.blue_chip = chip_val // 1
        # Return the required string
        # Set the chip numbers to strings in order to concatenate
        return str(self.black_chip) + " " + "Black chip(s)," + " " + \
            str(self.green_chip) + " " + "Green chip(s)," + " " + \
            str(self.red_chip) + " " + "Red chip(s)," + " " + \
            str(self.blue_chip) + " " + "Blue chip(s) - " + \
            "Totaling" + " " + "$" + str(self.balance)

# Create instance variables (Test code for ChipBank)
cs = ChipBank(149)
print(cs)
cs.deposit(7)
print(cs.get_balance())
print(cs)
print(cs.withdraw(84))
print(cs)
cs.deposit(120)
print(cs)
print(cs.withdraw(300))
