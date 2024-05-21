from repformulas import epleyCalculation, brzyckiCalculation, landerCalculation

def main():
    weight = input("What is your weight? (lbs only) : ")
    reps = input("What is the number of reps for the exercise? \n(Lower the reps the more accurate it would be) : ")
    print(f"Your weight is {weight} lbs")
    print(f"The number of reps reported is {reps}")

main()