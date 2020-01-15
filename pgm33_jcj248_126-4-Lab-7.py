'''___Lab 07 - Game show___
___Parker Marschel & Jace Jenkins___
___pgm33 & jcj248___
___Section 4___
___10/27/17___
'''
# Use import random to use the random shuffle() method
import random

# Call a main function


def main():
    # Use the print function for the menu
    print("Welcome to the sports game show!!!" + "\t")
    print("1.) Play the game" + "\n" + "2.) Exit" + "\n" +
          "3.) View credits" + "\n")
    # Take user input to determine what they want to do
    Menu_choice = input("Select 1, 2, or 3: " + "\n")
    # Use print for a gap between lines
    print()
    # Use conditional if statments to do what the user chose
    if Menu_choice == "1":
        # If user wants to play then call the game function
        return game()
    elif Menu_choice == "2":
        # Use print statments if the user wants to exit
        print("Thanks for stopping by!!!")
        print()
        # Take the user back to the main menu
        return main()
    # Call the credits function to show credits
    elif Menu_choice == "3":
        return credits()

# Create the game in a function called game


def game():
    # Create a variable that store the total number of questions
    total = 0
    # Create a variable that stores the users score based on questions correct
    score = 0
    # Create a list containing multiple dictionaries
    questions = [{"Question": "What other sport did Michael Jordan play?",
                  "Answers": ["Basketball?", "Soccer?", "Baseball?",
                              "Football?"],
                  "Correct": "2", "Wrong": ["1", "3", "4"]},
                 {"Question": "Which NBA player has the most rings of "
                              "all time?",
                  "Answers": ["Bill Russel", "Michael Jordan",
                              "Magic Johnson"],
                  "Correct": "2", "Wrong": ["1", "3"]},
                 {"Question": "What sport does Christiono Ronaldo play?",
                  "Answers": ["Tennis", "Hockey", "Baseball",
                              "Track & Field", "Soccer"],
                  "Correct": "5", "Wrong": ["1", "2", "3", "4"]},
                 {"Question": "What hockey team does Vladimir Tarasenko "
                              "play on?",
                  "Answers": ["Penguins", "Blackhawks", "Blues", "Astros",
                              "Kings", "Knights"],
                  "Correct": "3", "Wrong": ["1", "2", "4", "5", "6"]},
                 {"Question": "What is the most popular sport in the World?",
                  "Answers": ["Soccer", "Football", "Basketball", "Cricket"],
                  "Correct": "1", "Wrong": ["2", "3", "4"]},
                 {"Question": "Who won the World Series in 2011?",
                  "Answers": ["A's", "Red Sox", "Diamondbacks",
                              "Cardinals", "Angels"],
                  "Correct": "4", "Wrong": ["1", "2", "3", "5"]},
                 {"Question": "What is Mohamed Ali's birth name?",
                  "Answers": ["Johnny Clay", "Jonathan Ali", "Cassius Clay"],
                  "Correct": "3", "Wrong": ["1", "2"]},
                 {"Question": "How many holes are in a full round of golf?",
                  "Answers": ["12", "18", "24", "36"],
                  "Correct": "2", "Wrong": ["1", "3", "4"]},
                 {"Question": "Who was the first African-American baseball "
                              "player?",
                  "Answers": ["Jackie Robinson", "Josh Gibson",
                              "Satchel Paige", "Monte Irvin", "Babe Ruth"],
                  "Correct": "1", "Wrong": ["2", "3", "4", "5"]},
                 {"Question": "What city held the 2012 Olympic Games?",
                  "Answers": ["Beijing", "London"], "Correct": "2",
                  "Wrong": ["1"]}]
    # Use the random shuffle method the dictionaries in the list around
    random.shuffle(questions)
    # For loop iterates through all the elements in the list
    for question in questions:
        # Prints the first question
        print(question["Question"])
        # Iterates through the answer choices
        # Enumerate turns the list in the key to a tuple
        for i, choice in enumerate(question["Answers"]):
            # Prints the answers in a specific format (1. example)
            print(str(i + 1) + ". " + choice)
        # Prints a space between lines
        print()
        # Prompts the user with choices based on number of choices possible
        print("Choose an answer 1 -", str(len(question["Answers"])))
        # Takes user input on the answer chosen
        answer = input("Answer: ")
        # Prints space between lines
        print()
        # Use conditional if statement for correct answers
        if answer == question["Correct"]:
            # Add 1 to the total questions asked
            total += 1
            # Add one to the users score
            score += 1
            # Tell the user they got the question right
            print("Correct")
            # Tell the user their current score
            print("Your current score is", score, "out of", total)
            # Prints space between lines
            print()
        # Use elif conditional for a wrong answer inputed
        elif answer in question["Wrong"]:
            # Only add 1 to the total. Not to the score
            total += 1
            # Tell they chose the wrong answer
            print("Wrong!!!!! Better luck next time")
            # Tell the user their current score
            print("Your current score is", score, "out of", total)
            # Prints space between lines
            print()
        # Use 2nd elif for invalid answers
        elif answer != question["Correct"] and answer != question["Wrong"]:
            # Use while loop to repeat the question until the user...
            # ...inputs a valid answer
            while answer != question["Correct"] and \
                            answer != question["Wrong"]:
                # Add one to the total only
                total += 1
                # Tell the user their answer was invalid
                # Tell the user to enter a valid answer
                print("Invalid answer, please choose an answer 1 - ",
                      str(len(question["Answers"])))
                # Tell the user their current score
                print("Your current score is a", score, "out of", total)
                # Take input for a revised answer
                retryAns = input("Choose answer based on requirements: ")
                # Use conditonal if statment for a correct revised answer
                if retryAns == question["Correct"]:
                    # Add one to the total
                    total += 1
                    # Add one to the score
                    score += 1
                    # Tell them they entered a valid answer
                    # Tell them the answer is right
                    print("You finally chose a valid answer and it is "
                          "actually correct.")
                    # Tell the user their current score
                    print("Your current score is", score, "out of", total)
                    # Use break to stop the loop
                    break
                # Use elif statement if the revised answer is wrong
                elif retryAns in question["Wrong"]:
                    # Add one to the total only
                    total += 1
                    # Tell the user they entered a valid answer
                    # Tell the user their answer was incorrect
                    print("You got it wrong but at least you choose a "
                          "valid answer.")
                    # Tell the user their current score
                    print("Your current score is a", score, "out of", total)
                    # Use break to end the loop
                    break
    # Print the users score out of the total questions asked
    print("Your got", score, "right out of", total)
    # Print an ending message
    print("Thanks for playing the sports game show")
    # Adds a space between lines
    print()
    # Use return to take the user back to the main menu
    return main()

# Create a function for the credits of the game


def credits():
    # Use a print statement to show the creators of the game
    print("Excutive designers: Parker Marschel and Jace Jenkins")
    # Adds spaces between lines
    print()
    print()
    # Use return to take the user back to the main menu
    return main()
# Call the main function
main()
