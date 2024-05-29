from repformulas import oneRepCalculation
from macros import generateMacros

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
    choice = input("\nWhat would you like to do? (1-3) : ")
    return choice

def main():
    generateWelcomeMessage()
    choice = menu()
    #print(f"Your weight is {weight} lbs")
    #print(f"The number of reps reported is {reps}")
    
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
            return
        case "3":
            return

main()