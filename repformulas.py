def epleyCalculation(weight, reps):
    return (weight / (1 - 0.0333 * reps))

def brzyckiCalculation(weight, reps):
    return (weight / (1.0278 - (0.0278 * reps)))

def landerCalculation(weight, reps):
    return ((100 * weight) / (101.3 - 2.67123 * reps))