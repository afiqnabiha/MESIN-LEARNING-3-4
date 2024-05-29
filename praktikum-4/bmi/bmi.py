import math

def meter_square(unit):
    return math.floor(unit * 10**-4)

def men_women_ratio(men, women):
    print(f"len of men element: {len(men)}")
    print(f"len of women element: {len(women)}")
    if len(women) > len(men):
        return len(women) / len(men)
    
    return len(men)/len(women)