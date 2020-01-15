'''
Lab 09 - STARS
Parker Marschel & Micah Griffin
pgm33 $ mag765
Section 4
11/10/17
'''

# Import turtle
import turtle

# Create main function


def main():
    # Open the file to read
    inputfile = open("stars.txt", "r")
    # Access the first dictioanry to get coordinates
    coordinates_dict = read_coords(inputfile)[0]
    # Allow the loop to read through the file again
    inputfile.seek(0)
    # Access the second dictionary to get the magnitudes
    magnitudes_dict = read_coords(inputfile)[1]
    # Call the plot_by_magnitude function
    plot_by_magnitude(500, coordinates_dict, magnitudes_dict)

# Create the read_coords function


def read_coords(input_file):
    # Initializing dictionaries
    coord_dict = {}
    mag_dict = {}
    name_dict = {}
    # Initializing tuple
    final_tup = (coord_dict, mag_dict, name_dict)
    # Setting up iteration through file
    lines = input_file.readlines()
    # setting up each dictionary
    for line in lines:
        # Splitting on spaces
        line_list = line.split(" ")
        # Dictionary one based on Draper number index and coords
        coord_dict[line_list[3]] = (float(line_list[0]), float(line_list[1]))
        mag_dict[line_list[3]] = float((line_list[4]))
        # Creating third dictionary if there's a name
        if len(line_list) >= 7:
            # If there's one name that's one word
            # Puts it in the third dictionary with proper keys
            if len(line_list) == 7:
                # Strips the line so \n does not appear
                line_list[6] = line_list[6].strip()
                name_dict[line_list[6]] = line_list[3]
            # If there's either two names or two words in one name
            # Acts based on whether there's one or two names
            elif len(line_list) > 7:
                test_list = []
                test_list.append(line_list[6])
                test_list.append(line_list[7])
                # If there's two names, creates two keys with same value
                if ";" in test_list[0]:
                    replaced_name = test_list[0].replace(";", "")
                    name_dict[replaced_name] = line_list[3]
                    name_dict[test_list[1]] = line_list[3]
                # If there's one name that's two words
                # Creates one key with one value
                else:
                    concat_str = test_list[0] + " " + test_list[1]
                    name_dict[concat_str] = line_list[3]
    # Return the final_tup
    return final_tup

# Create the plot_plain_stars


def plot_plain_stars(picture_size, coordinates_dictionary):
    # Fill the background and line color
    turtle.fillcolor("white")
    turtle.bgcolor("black")
    # Create the dimesions of the picture
    turtle.setup(picture_size, picture_size)
    # Create a for loop to access the keys in the coordinates dictionary
    for star_HDN in coordinates_dictionary.keys():
        # Access the coordinates
        coordinates = coordinates_dictionary[star_HDN]
        # Scale to frame
        xcoord = coordinates[0] * (picture_size / 2)
        ycoord = coordinates[1] * (picture_size / 2)

        # Pen up, go to these coordinates
        turtle.pu()
        turtle.goto(xcoord, ycoord)
        # Pen down, draw square / fill square
        turtle.pd()
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
    turtle.exitonclick()


# Create the plot_by_magnitude function

def plot_by_magnitude(picture_size, coordinates_dictionary, mag_dict):
    # Use tracer to skip through the tracing to the final product
    # turtle.tracer(0)
    # Turn the line color and background color to the required colors
    turtle.pencolor("white")
    turtle.bgcolor("black")
    # Create the frame using the picture size passes in
    turtle.setup(picture_size, picture_size)
    # Use a for loop to access the magnitude in the magnitude dictionary
    for star_HDN in mag_dict:
        # Store the magnitudes in a variable
        star_mag = mag_dict[star_HDN]
        # Use the required equation for the magnitudes of each star
        mag = round(10.0 / (star_mag + 2))
        # Scale to frame
        coordinates = coordinates_dictionary[star_HDN]
        xcoord = coordinates[0] * (picture_size / 2)
        ycoord = coordinates[1] * (picture_size / 2)
        # Set magnitude to have a maximum value of 8
        if mag > 8:
            mag = 8
        # Pen up, go to these coordinates
        turtle.pu()
        turtle.goto(xcoord, ycoord)
        # Pen down, draw square / fill square
        turtle.pd()
        # Use the .dot() turtke method to plot the points
        turtle.dot(mag)
    # Use exitonlcik to exit
    turtle.exitonclick()
 #Call the main function
main()
