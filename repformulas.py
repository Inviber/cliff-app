def epleyCalculation(weight, reps):
    return (weight / (1 - 0.0333 * reps))

def brzyckiCalculation(weight, reps):
    return (weight / (1.0278 - (0.0278 * reps)))

def landerCalculation(weight, reps):
    return ((100 * weight) / (101.3 - 2.67123 * reps))

def oneRepCalculation(weight, reps):
    if reps >= 1 and reps < 6:
        return epleyCalculation(weight, reps)
    elif reps >= 6 and reps < 10:
        return brzyckiCalculation(weight, reps)
    else:
        print("\nAny reps higher than 10 produces inaccurate results. You could do higher or lower amount.\nBest to do within the rep range of 3-10 for accurate results")
        return landerCalculation(weight, reps)