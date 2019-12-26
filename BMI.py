#   This program takes a person's weight and height 
#   and returns their Body Mass Index score.
#   Author: Joseph Prostko
#   Project: Assignment 2: Python; Question 2
#   Version: October 2019
def main():
    # The user is prompted to enter their weight in pounds.
    weightString = input("Enter your weight(in pounds):")

    # The user is prompted to enter their height in inches.
    heightString = input("Enter your height(in inches):")
    
    # The user's weight is saved as an integer.
    weight = int(weightString)

    # The user's height is saved as an integer.
    height = int(heightString)
    
    # The user's bmi is calculated with the appropriate formula.
    bmi = (weight * 720) / (height * height)

    # The user's BMI is printed.
    print("Your BMI is " + str(bmi))
    
    # The if statement below determines if the BMI is too low.
    if bmi < 19.0:

        # If so, it is printed to the screen.
        print("That's on the low side.")

    # The if statement below determines if the BMI is too high.
    if bmi > 25.0:

        # If so, it is printed to the screen.
        print("That's on the high side.")

    # The else statement below is called if the BMI is okay.
    else:

        # If so, it is printed to the screen.
        print("That's okay.")

# The main method is called.
main()