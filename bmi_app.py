# NAME: ZULKIFLI TEMITOPE SALAMI
# DATE: 02/21/2023
# PROGRAM DESCRIPTION: A simple program to calculate the body mass index (BMI) of a person using input from the user for weight in pounds,
# height in inches. The BMI and a difference in the users BMI if they lost weight, successively in increment of 5 to a maximum of 15% 
# of their weight would be calculated and displayed. The relative category of the weight and successive increment in loss of weight would be displayed.
# PROGRAM NAME: BodyMassIndex (BMI) App
#######################################################################################################################################

 
# Initialization:
# float variable height_in_inches for input
height_in_inches = 0.0
# integer MINIMUM_HEIGHT as a constant
MINIMUM_HEIGHT = 20
# integer MAXIMUM_HEIGHT as a constant
MAXIMUM_HEIGHT = 120
# float variable weight_in_pounds for input 
weight_in_pounds = 0.0
# weight condition
need_valid_weight = True
# integer MINIMUM_WEIGHT as a constant
MINIMUM_WEIGHT = 10
# float WEIGHT_PERCENT as a constant
WEIGHT_PERCENT = 0.15
# float weight_maximum as a variable
weight_maximum = 0.0
# float variable bmi for output 
bmi = 0.0
# integer CONVERSION_FACTOR a constant 
CONVERSION_FACTOR = 703
# integer CATEGORY_ONE as a constant
CATEGORY_ONE = 16
# integer CATEGORY_TWO as a constant
CATEGORY_TWO = 18.5
# integer CATEGORY_THREE as a constant
CATEGORY_THREE = 25
# integer CATEGORY_FOUR as a constant
CATEGORY_FOUR = 30
# integer MINUIMUM_VALUE as a constant
MINUIMUM_VALUE = 0
# string variable to continue loop
new_user_valid = "yes"
# string variable to break the loop
new_user_not_valid = "no"
# new input condition
need_new_input = True
   

# Initialize a condition as True to enter a loop
need_input = True
while need_input == True:   
    need_valid_weight = True
    need_new_input = True                                                                                            
# display the message “ Please enter the person's height in inches: ” 
    try:
        height_in_inches = float(input("Please enter users height in inches: "))
    except:
        height_in_inches = MINUIMUM_VALUE - 1
# Validate input and store the user input in the variable height_in_inches 
# Display error message if input is not numeric, or input less than 20 or greater than 120.
    if height_in_inches < MINIMUM_HEIGHT or height_in_inches > MAXIMUM_HEIGHT:
        print("The user input has to be numeric and between 20 to 120 inclusive")
    else:
        print()
# display the message “ Please enter the person's weight in pounds: “ 
        while need_valid_weight == True:
            try:
                weight_in_pounds = float(input("Please enter the users weight in pounds: "))
            except:
                weight_in_pounds = MINUIMUM_VALUE - 1
            # Validate input and store the users input in the variable weight_in_pounds 
            # Display error message if input is not numeric, or input less than 10
            if weight_in_pounds < MINIMUM_WEIGHT:
                print("The user input has to be numeric and greater than or equal to 10")
            else:
                need_valid_weight = False
            # prompt the program to calculate the bmi of the user using the entered variables and in a range of weight_in_pounds to weight_maximum 
                weight_maximum = weight_in_pounds - (weight_in_pounds * WEIGHT_PERCENT)
                weight_maximum = int(weight_maximum)
                weight_in_pounds = int(weight_in_pounds)
                for count in range (weight_in_pounds,(weight_maximum),-5):
                    bmi = (count/pow(height_in_inches,2))* CONVERSION_FACTOR 
                    # round the calculated BMI showing one decimal place
                    # bmi < CATEGORY_ONE is determined as “severely underweight”
                    if bmi < CATEGORY_ONE:
                        bmi_category = str("severly underweight")
                    # bmi >= CATEGORY_ONE and < CATEGORY_TWO is determined as “underweight”
                    elif bmi >= CATEGORY_ONE and bmi < CATEGORY_TWO:
                        bmi_category = str("underweight")
                    # bmi >= CATEGORY_TWO and < CATEGORY_THREE is determined as “healthy”
                    elif bmi >= CATEGORY_TWO and bmi < CATEGORY_THREE:
                        bmi_category = str("healthy")
                    # bmi >= CATEGORY_THREE and < CATEGORY_FOUR is determined as “overweight”
                    elif bmi >= CATEGORY_THREE and bmi < CATEGORY_FOUR:
                        bmi_category = str("overweight")
                    # bmi >= CATEGORY_FOUR is determined as  “obese”
                    else:
                        bmi_category = str("obese") 
                    # print the message ('The BMI for a ',height_in_inches,' tall person who weighs’,weight_in_pounds,' is ',round(bmi, 1),
                    # which is categorized as,bmi_category)
                    print("\nThe BMI for a",height_in_inches,"inches tall person who weighs",count,"pounds is",round(bmi,1),"which is categorized as",bmi_category)
                while need_new_input == True:
                    new_input = str(input("\nWould you like to enter data for another person? (yes/no): "))
                    if new_input.isalpha():
                        need_new_input = False
                        if new_input == new_user_valid:
                            need_input = True
                        elif new_input == new_user_not_valid:
                            need_input = False
                        else:
                            print("Input has to be yes/no")
                            need_new_input = True
                    else:
                        print("The input has to be alphabetic")
# prompt user “Would you like to enter data for another person? (yes/no): “

# validate user input as alphabetic and either yes or no
# if yes, continue loop
# if no, break loop

# Input: Press Enter to end this application...
input("\nPress Enter to End the Program......")
