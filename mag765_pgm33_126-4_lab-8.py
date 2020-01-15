'''
___lab 8, Grade Calculator II___
___Micah Griffin & Parker Marschel___
___mag765 & pgm33___
___10/27/2017___
___126L-4___
'''

# Call a main function


def main():
    # Create a dictionary that will be passed in to html function
    final_dictionary = {}
    # Open the file for reading
    file = open("input.txt", "r")
    # Call the read data function
    data_structure = read_grade_data(file)
    # store values for each cateory from every function
    hw_weight = data_structure["Homework"][0]
    hw_earned = data_structure["Homework"][1]
    hw_total = data_structure["Homework"][2]
    qz_weight = data_structure["Quizzes"][0]
    qz_earned = data_structure["Quizzes"][1]
    qz_total = data_structure["Quizzes"][2]
    test_weight = data_structure["Tests"][0]
    test_earned = data_structure["Tests"][1]
    test_total = data_structure["Tests"][2]
    projects_weight = data_structure["Projects"][0]
    projects_earned = data_structure["Projects"][1]
    projects_total = data_structure["Projects"][2]
    final_weight = data_structure["Final"][0]
    final_earned = data_structure["Final"][1]
    final_total = data_structure["Final"][2]
    # Store each return value from each function into variables
    avg_hw = average_grade(hw_earned, hw_total)
    avg_qz = average_grade(qz_earned, qz_total)
    avg_test = average_grade(test_earned, test_total)
    avg_project = average_grade(projects_earned, projects_total)
    avg_final = average_grade(final_earned, final_total)
    hw_letter = letter_grade(avg_hw)
    qz_letter = letter_grade(avg_qz)
    test_letter = letter_grade(avg_test)
    project_letter = letter_grade(avg_project)
    final_letter = letter_grade(avg_final)
    hw_avg_weighted = average_weighted(hw_earned, hw_total, hw_weight)
    qz_avg_weighted = average_weighted(qz_earned, qz_total, qz_weight)
    test_avg_weighted = average_weighted(test_earned, test_total, test_weight)
    final_avg_weighted = average_weighted(final_earned,
                                          final_total, final_weight)
    projects_avg_weighted = average_weighted(projects_earned,
                                             projects_total, projects_weight)
    final_score = hw_avg_weighted + qz_avg_weighted + final_avg_weighted + \
        projects_avg_weighted
    final_letter = letter_grade(final_score)
    hw_cont = overall_cont(avg_hw, hw_weight)
    qz_cont = overall_cont(avg_qz, qz_weight)
    test_cont = overall_cont(avg_test, test_weight)
    project_cont = overall_cont(avg_project, projects_weight)
    final_cont = overall_cont(avg_final, final_weight)
    cumlative_grade = culmative(hw_cont, qz_cont, test_cont,
                                project_cont, final_cont)
    # Put each piece into the dictionary at the beginning of the function
    final_dictionary["Homework Statistics"] = [avg_hw, hw_letter,
                                               hw_cont, hw_weight]
    final_dictionary["Quizzes Statitics"] = [avg_qz, qz_letter,
                                             qz_cont, qz_weight]
    final_dictionary["Test Statistics"] = [avg_test, test_letter,
                                           test_cont, test_weight]
    final_dictionary["Project Statistics"] = [avg_project, project_letter,
                                              project_cont, projects_weight]
    final_dictionary["Final Statistics"] = [avg_final, final_letter,
                                            final_cont, final_weight]
    final_dictionary["Cumulative Grade"] = [cumlative_grade]
    # Call the function that writes the HTML file and pass in the...
    # ...correct dictionary
    write_data(final_dictionary)

# Call the read_grade_data function from the requirements of the lab


def read_grade_data(file_handle):
    # Create a dictionary place holder
    grade_dict = {}
    # Use the .readlines function to make a list for each line
    fileList = file_handle.readlines()
    # Iterate through each line
    for line in fileList:
        # Strip the line of excess white space at beginning and end
        line = line.strip()
        # Split the line at spaces only for the first 2 spaces
        split_line = line.split(" ", 2)
        # Index the new list to access the category
        category = split_line[0]
        # Index the new list to access the weight of the category
        category_weight = int((split_line[1]).replace("%", ""))
        # Index the new list to access the grades and join them together
        grades = split_line[2].replace(" ", "")
        # Create list place holders
        scored_earned = []
        score_total = []
        # Split the grades into a new list
        seperated_grades_list = grades.split(",")
        # Index the grades list
        for grade in seperated_grades_list:
            # Split the list at the slash
            grade_list = grade.split("/")
            # Append each number to the correct place holder
            scored_earned.append(int(grade_list[0]))
            score_total.append(int(grade_list[1]))
        # Add each key and values to the dictionary
        grade_dict[category] = [category_weight, scored_earned, score_total]
    # Return the dictionary
    return grade_dict

# Call the average grade function
# Calculates the average grade from lab 04


def average_grade(score_list, max_list):
    scoresum = 0
    for i in score_list:
        scoresum += i
    maxsum = 0
    for i in max_list:
        maxsum += i
    grade = scoresum / maxsum
    grade = (grade * 100) // 1
    return grade

# Call a function to get the letter grade for each category from lab 04


def letter_grade(percent):
    # Use if, elif, else conditionals
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    else:
        return "F"

# Call a funciton to calculate the average weighted grade from lab 04


def average_weighted(score_list, max_list, weight):
    integer_score_list = []
    integer_max_list = []
    for score in score_list:
        integer_score_list.append(int(score))
    for score in max_list:
        integer_max_list.append(int(score))
    averageGrade = round(((sum(integer_score_list)) /
                          (sum(integer_max_list))), 2)
    weightedGrade = ((((averageGrade * 100) // 1) * weight) // 1)/10
    return weightedGrade

# Call a function to calculate the overall grade contribution for each category
# Takes in percent and weight


def overall_cont(percent, weight):
    # Turn percent and weight in to decimals
    percent = percent/100
    weight = weight/100
    # Multiply percent and weight together to get the contribution
    cont = percent * weight
    # Round the answer to the appropriate place
    cont = round(cont, 3)
    # Return the answer
    return cont

# Call a function that calculates the cumulative grade
# Function takes in the weighted grade for each category


def culmative(wGraded1, wGrade2, wGrade3, wGrade4, wGrade5):
    # Add all the weighted grades together
    cum = wGraded1 + wGrade2 + wGrade3 + wGrade4 + wGrade5
    # Round to the appropriate decimal place
    cum = round(cum, 2)
    # Return the answer
    return cum

# Create a function to write an HTML file
# The final dictioanry gets passed in


def write_data(data):
    # Open the HTML file to write
    file = open("example.html", "w")
    # Write html tag & body
    file.write("<html>\n")
    file.write("<body>\n")
    # Iterate through the dictionary that was passed in
    for key in data.keys():
        # Access the category
        category = key
        # Access the weight in the dictionary and convert to a string
        weight = str(data[key][3])
        # Access the average grade from the dictionary
        avggrade = str(data[key][0])
        # Access the letter grade in the dictionary
        lttr_grade = data[key][1]
        # Access the cumulative grade in the dictionary
        cuml_grade = str(data[key][2])

        # Use the .write to write into the HTML file
        # Write the head which will be the category and weight
        file.write("<h1>" + category + " " + "(" + weight + ")" + "</h1>\n")
        # Write an unorganized list
        file.write("<ul>")
        # Write average grade into the file as a list
        file.write("<li>" + avggrade + "</li>\n")
        # Write the letter grade in to the list
        file.write("<li>" + lttr_grade + "</li>\n")
        # Write the cumulative grade into the file
        file.write("<li>" + cuml_grade + "</li>\n")
        # Close the list
        file.write("</ul>\n")
# Call the main function
main()
