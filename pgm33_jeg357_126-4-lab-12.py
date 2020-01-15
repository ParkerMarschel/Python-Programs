'''
Lab 12 Blackjack
Parker Marschel and Josh Garcia
pgm33 and Jeg357
12/15/17
Section 4
'''


# Import two classes from lab 10 using import
from lab10_Answer_Key_MV import ChipBank
from lab10_Answer_Key_MV import Card
# Import random
import random

# Create the BlackjackHand class


class BlackjackHand:
    # Initialize with no parameters
    def __init__(self):
        # Create a card list as an instance variable
        self.card_list = []
    # Create the add_card method that takes in a new card as a parameter

    def add_card(self, new_card):
        # Append the new card to the card list
        self.card_list.append(new_card)
    # Create the get value method

    def get_value(self):
        # Create a local variable as a place holder for the hand total
        cards_total = 0
        # Use a for loop to iterate through the card list
        for card in self.card_list:
            # Add the value of each card to the cards_total place holder
            cards_total += Card(card).get_value()
        # Use if statement if the total is greater than 21
        if cards_total > 21:
            # Use for loop to iterate through the car list again
            for card in self.card_list:
                # Use if statement to check if one of the cards is an Ace
                if Card(card).get_rank() == "Ace":
                    # Subtract 10 away from the total of the hand
                    cards_total -= 10
        # Return the total
        return cards_total
    # Create the string method

    def __str__(self):
        # Create a place holder for the string
        user_hand = ""
        # Use a for loop to iterate through the card list
        for card in self.card_list:
            # Add the string message for each card to the place holder
            user_hand += Card(card).get_rank() + " " + "of" + \
                         " " + Card(card).get_suit()
            user_hand += ", "
        # Return the final message
        return user_hand

# Create the Blackjack class


class Blackjack:
    def __init__(self, starting_dollars):
        # Initialize the deck
        self.deck = []
        # Use for loop to append cards to the deck
        for i in range(52):
            self.deck.append(i)
        # Use random and shuffle method to shuffle the deck
        random.shuffle(self.deck)
        # Initialize the starting dollars
        self.money = starting_dollars
        #  Create an instance variable that stores the imported ChipBank
        self.bank = ChipBank(starting_dollars)
        # Create instance variable for the wager to remember for later
        # Create an instance variable for the users hand by using the...
        # ...BlackjackHand class
        self.user_hand = BlackjackHand()
        self.dealer_hand = BlackjackHand()
        # Create an instance variable for a drawn card
        self.drawn_card = 0
        self.wager = 0
        # Set self.active to False for the method game_active()
        self.active = False

    # Create the start_hand method from the requirements

    def start_hand(self, wager):
        # Set the local variable wager to the instance variable
        self.wager = wager
        # Adds a card to the users deck by using...
        # ...the BlackjackHand class
        self.user_hand.add_card(self.draw())
        self.user_hand.add_card(self.draw())
        # Adds a card to the users deck by using the...
        # ...BlackjackHand class
        self.dealer_hand.add_card(self.draw())
        self.dealer_hand.add_card(self.draw())
        # Use the withdraw method from the ChipBank class to subtract wager
        self.bank.withdraw(wager)
        # Use print function to print the users and dealers current hand
        print("Your starting hand: " + str(self.user_hand))
        print("The dealers starting hand is: " + str(self.dealer_hand))
        # Use if conditional to check the value of the cards
        if self.user_hand.get_value() == 21:
            # If the user has a 21 check to see if the dealer does as well
            if self.dealer_hand.get_value() == 21:
                # If the dealer does then pass in push...
                # ...for the end_hand method
                self.end_hand("push")
            # Use else only if the player has 21
            else:
                self.end_hand("win")
        # Set self.active equal to the Boolean True
        self.active = True

    # Create the draw() method

    def draw(self):
        # Use if conditional to check if the deck is empty
        if self.deck is False:
            # Use the same for loop to append cards into the deck
            for i in range(52):
                self.deck.append(i)
            # Shuffle the deck after rebuilding it
            random.shuffle(self.deck)
        # Draw a card from the deck and store it into the instance variable
        self.drawn_card = self.deck[0]
        # Use the pop method to remove the card from the deck
        self.deck.pop(0)
        # return the drawn card
        return self.drawn_card

    # Create the hit method

    def hit(self):
        # Use if conditional to check if the game is active
        if self.active is True:
            # Draw another card and add it to the users deck
            self.user_hand.add_card(self.draw())
            # Use if statement to check if the user exceeds 21
            if self.user_hand.get_value() > 21:
                # If true then pass in lose to the end_hand method
                self.end_hand("lose")
            # Use elif if the user has a value of 21
            elif self.user_hand.get_value() == 21:
                # If true then pass in win to the end_hand method
                self.stand("win")

    # Create the stand() method

    def stand(self):
        # Use if statement to check if the game is active
        if self.active is True:
            # Use while loop to run if the dealer has a 16 or less
            while self.dealer_hand.get_value() <= 16:
                # Draw another card
                self.dealer_hand.add_card(self.draw())
                # Print the dealers card
                print("The dealer draws a" + " " + str(self.dealer_hand[-1]))
                # Print the dealers hand
                print("The dealers hand is now" + " " +
                      str(self.dealer_hand))
            # Use else statement if the dealers hand value is > 16
            else:
                # Use if statement for the user having a higher hand value
                if self.user_hand.get_value() > self.dealer_hand.get_value():
                    self.end_hand("win")
                # Use elif if the user and the dealer are tied
                elif self.user_hand.get_value() == \
                        self.dealer_hand.get_value():
                    self.end_hand("push")
                # Use else if the users hand value is less than the dealers
                else:
                    self.end_hand("lose")

    # Create the game_active() method

    def game_active(self):
        # Use if statement to check if self.active is True
        if self.active is True:
            return True
        # Use else statement to return False
        else:
            return False

    # Create the end_hand() method that takes in an outcome as a parameter

    def end_hand(self, outcome):
        # Use if statement to check if the user won
        if outcome == "win":
            # Double the wager put in an add it to the balance
            self.money += self.wager * 2
        # Use elif to check if the outcome is push
        elif outcome == "push":
            # Return the wager to the users balance
            self.money += self.wager
            # Set everything back to their starting values
            self.user_hand = []
            self.dealer_hand = []
            self.wager = 0
            self.active = False

# Test code


if __name__ == "__main__":
    blackjack = Blackjack(250)
    while blackjack.bank.get_balance() > 0:
        print("Your remaining chips: " + str(blackjack.bank))
        wager = int(input("How much would you like to wager? "))
        blackjack.start_hand(wager)
        while blackjack.game_active():
            choice = input("STAND or HIT: ").upper()
            if choice == "STAND":
                blackjack.stand()
            elif choice == "HIT":
                blackjack.hit()
        print()
    print("Out of money! The casino wins!")
