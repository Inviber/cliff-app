from repformulas import epleyCalculation, brzyckiCalculation, landerCalculation

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
    print(choice)
    weight = input("\nWhat is your weight? (lbs only) : ")
    reps = input("\nWhat is the number of reps for the exercise? \n(Lower the reps the more accurate it would be) : ")
    print(f"Your weight is {weight} lbs")
    print(f"The number of reps reported is {reps}")

main()