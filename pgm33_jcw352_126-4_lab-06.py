'''
Lab 6 - Banners
Jeffrey Williamson and Parker Marschel
jcw352 & pgm33
10/20/17 Section 4
'''

# Create the function listed in the directions


def print_banner(word, direction):
    # Use the .lower() method to get rid of case sensitivity for parameters
    word = word.lower()
    direction = direction.lower()
    # Create a dictionary for every letter in the alphabet
    letters = {"a": ["  #  ", " # # ", " ### ", " # # ", "#   #"],
               "b": ["#   ", "#   ", "####", "#  #", "####", ],
               "c": [" ####", "#    ", "#    ", "#    ", " ####"],
               "d": ["    #", "    #", "#####", "#   #", "#####"],
               "e": ["####", "#   ", "### ", "#   ", "####"],
               "f": ["####", "#   ", "### ", "#   ", "#   "],
               "g": ["#####", "#    ", "#  ##", "#   #", "#####"],
               "h": ["#  #", "#  #", "####", "#  #", "#  #"],
               "i": ["#####", "  #  ", "  #  ", "  #  ", "#####"],
               "j": ["#####", "  #  ", "  # ", "# #  ", " #   "],
               "k": ["#  #", "# # ", "##  ", "# # ", "#  #"],
               "l": ["#   ", "#   ", "#   ", "#   ", "#####"],
               "m": ["#   #", "## ##", "# # #", "#   #", "#   #"],
               "n": ["#   #", "##  #", "# # #", "#  ##", "#   #"],
               "o": [" ### ", "#   #", "#   #", "#   #", " ### "],
               "p": ["#####", "#   #", "#####", "#    ", "#   "],
               "q": ["#### ", "#  # ", "#  # ", "#### ", "    #"],
               "r": ["###", "# #", "###", "## ", "# #"],
               "s": ["#####", "#   ", "#####", "    #", "#####"],
               "t": ["#####", "  #  ", "  #  ", "  #  ", "  #  "],
               "u": ["#   #", "#   #", "#   #", "#   #", " ### "],
               "v": ["#       #", " #     # ", "  #   #  ", "   # #   ",
                     "    #    "],
               "w": ["#   #", "#   #", "# # #", "## ##", "#   #"],
               "x": ["#   #", " # # ", "  #  ", " # # ", "#   #"],
               "y": ["#   #", " # # ", "  #  ", " #   ", "#    "],
               "z": ["#####", "   # ", "  #  ", " #   ", "#####"]}
    # Use conditional if statement for the direction passed in
    if direction == "horizontal":
        # Create a place holder for each line
        allLines = ["", "", "", "", ""]
        # For loop iterates through every element of the parameter word
        for letter in word:
            # Nested loop iterates through every line at a range of 5 lines
            for line in range(5):
                # Add the list values from letters to the list allLines
                allLines[line] += letters[letter][line] + "\t"
        # Print each line indexed through the place holder allLines
        # Use /n to create a new line specific for the horizontal direction
        print("", allLines[0], "\n", allLines[1], "\n", allLines[2], "\n",
              allLines[3], "\n", allLines[4])
    # Use elif for the other direction passed into the parameter
    elif direction == "vertical":
        # Create place holder for each line
        # For loop iterates through every element of the parameter word
        verticalLines  = "" + "\n"
        for letter in word:
            # Nested loop iterates through every line at a range of 5 lines
            for line in range(5):
                # Add the list values from letters to the String verticalLine
                #  /n is used for a line break between each.
                verticalLines += letters[letter][line] + "\n"
        print(verticalLines)
            # /n gives space between each letter
         # Print the line
    # USe else statement to state an invalid direction has been made
    else:
        print("This is not a valid direction")
# Call the function with arguments
word = input("Enter a word: ")
direction = input("Enter a direction (Vertical or Horizontal): ")

print_banner(word, direction)
