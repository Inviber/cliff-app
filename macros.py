def calculateMifflin_StJeorEquation(gender, weight, height, age):
    if gender == "m":
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        return (10 * weight) + (6.25 * height) - (5 * age) - 161

def calculateKatch_McArdleFormula(bf, weight):
    return 370 + 21.6(1-bf) * weight

def convertHeight(heightFeet, heightInches):
    return (heightFeet * 30.48) + (heightInches * 2.54)

def convertWeight(weight):
    return weight / 2.205

def activityMultiplier(activity):
    match activity:
        case "1":
            return 1.2
        case "2":
            return 1.375
        case "3":
            return 1.55
        case "4":
            return 1.725
        case "5":
            return 1.9

def calculateGoalCalories(calories, goal):
    if goal == "2":
        return calories - 500
    elif goal == "3":
        return calories + 500
    