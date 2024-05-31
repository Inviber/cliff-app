from repformulas import oneRepCalculation
from macros import calculateKatch_McArdleFormula, calculateMifflin_StJeorEquation, convertHeight, convertWeight, activityMultiplier, calculateGoalCalories

def generateWelcomeMessage():
    print(r"""     
   __   __    __  ____
 ,'_/  / /   / / / __/
/ /_  / /_  / / / _/  
|__/ /___/ /_/ /_/    
                      
""")

def menu():
    print("\nThis Fitness application is responsible for accomplishing: ")
    print("\t1. Generating One Rep Max (Best for Reps 10 and under)")
    print("\t2. Macro Calculations per individual")
    print("\t3. Generating a basic workout program")
    print("\t4. Exit the application")
    choice = input("\nWhat would you like to do? (1-4) : ")
    return choice

def menuChoices(choice):
    match choice:
        case "1":
            print("Generating One Rep Max...")
            weight = float(input("\nWhat is your weight? (lbs only) : "))
            reps = int(input("\nWhat is the number of reps for the exercise? \n(Lower the reps the more accurate it would be) : "))
            print(int(oneRepCalculation(weight, reps)))
        case "2":
            age = int(input("\nWhat is your age: "))
            gender = input("What is your gender (m/f) : ")
            heightFeet = int(input("What is your height (FEET) : "))
            heightInches = int(input("What is your height (inches) : "))
            weight = float(input("What is your weight? (lbs only) : "))
            goal = input("What is your Goal?\n\t1. Maintain\n\t2. Lose\n\t3. Gain\nChoice? : ")
            activity = input("What is your activity level?\n\t1. Little or no exercise\n\t2. Light 3-5 days a week\n\t3. Moderate 3-5 days a week\n\t4. Hard 6-7 days a week\n\t5. Hard 6-7 days a week and physical job\nChoice? : ")
            knowBF = input("Do you know your body fat percentage? (y/n):")
            height = convertHeight(heightFeet, heightInches)
            weight = convertWeight(weight)
            if knowBF == 'y':
                bf = input("What is your body fat percentage? : ")
                calories = int(calculateKatch_McArdleFormula(bf, weight) * activityMultiplier(activity))
            else:
                calories = int(calculateMifflin_StJeorEquation(gender, weight, height, age) * activityMultiplier(activity))
            print("\nCalories based on calculation: ", calories)
            print("\nCalories to meet goal (maintain / lose 1lb / gain 1lb) : ", calculateGoalCalories(calories, goal))
        case "3":
            print("Start survey to generate workout program...")

def main():
    generateWelcomeMessage()
    choice = ""
    
    while choice != "4":
        choice = menu()
        menuChoices(choice)

main()