'''Lab 04 Grade Calculator'''
'''Parker Marschel and Micah Griffin'''
'''pgm33 and mag765'''
'''section 4'''
'''10/06/17'''
# Create a main function where variables will be called


def main():
    # Variables storing lists for points in each category
    homeworkMax = [40, 40, 40, 40, 40, 5]
    homeworkEarned = [39, 40, 29, 40, 0, 5]
    quizMax = [10, 10, 10, 10, 10, 10, 10]
    quizEarned = [10, 10, 9, 2, 10, 10, 10]
    testMax = [300, 300, 300]
    testEarned = [293, 284, 300]
    # Variables store wieght perccentage of each category
    homeworkWeight = .2
    quizWeight = .2
    examWeight = .6
    # Variables store called functions
    homeworkPercent = average_grade(homeworkEarned, homeworkMax)
    quizPercent = average_grade(quizEarned, quizMax)
    testPercent = average_grade(testEarned, testMax)
    hwletterGrade = letter_grade(homeworkPercent)
    qzletterGrade = letter_grade(quizPercent)
    tstletterGrade = letter_grade(testPercent)
    hwWeighted = average_weighted(homeworkEarned, homeworkMax, homeworkWeight)
    qzWeighted = average_weighted(quizEarned, quizMax, quizWeight)
    tstWeighted = average_weighted(testEarned, testMax, examWeight)
    finalScore = hwWeighted + qzWeighted + tstWeighted
    # finalScore adds each weighted grade to get the final grade
    # final letter grade is found after the final wieghted percent
    fletterGrade = letter_grade(finalScore)
    # Print the variables storing functions to give grades and final grade
    print("Home work grade:", homeworkPercent, "(", hwletterGrade, ")")
    print("Quiz grade:", quizPercent, "(", qzletterGrade, ")")
    print("Test grade:", testPercent, "(", tstletterGrade, ")")
    print("Final score:", finalScore, "(", fletterGrade, ")")


# Function 2, calculates the average grade and returns the value
def average_grade(score_list, max_list):
    scoreSum = sum(score_list)
    maxSum = sum(max_list)
    grade = scoreSum / maxSum
    grade = (grade * 100) // 1
    return grade
# Function 3, calcualtes the letter grade based off percent from funciton 2
# Returns a letter


def letter_grade(percent):
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

# Function 3, calcuates the average weighted grade


def average_weighted(score_list, max_list, weight):
    averageGrade = round(((sum(score_list)) / (sum(max_list))), 2)
    weightedGrade = (((averageGrade * 100) // 1) * weight) // 1
    return weightedGrade
# Calls the main function
main()
