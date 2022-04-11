def heightInMeters(height):
    heightInMeters = height / 100
    return heightInMeters

def bmi(weight, heightInMeters):
    bmi = weight / (heightInMeters ** 2)
    roundedBmi = round(bmi,2)
    return bmi,roundedBmi

def body_parameters(heightInMeters):
    minWeight = round(18.5 * heightInMeters ** 2,1) #Correct min weight
    maxWeight = round(24.9 * heightInMeters ** 2,1) #Correct max weight
    kgPday = 300/7000            #Weight loss/gain with 300 calories deficit/surplus
    return minWeight, maxWeight, kgPday

#Defining correct kcal intake based on Harris-Benedict equatation

def kcal_calc(weight,height,age,gender):
    if gender == "M":
        kcal = round((1.3 * (66 + (13.7 * weight) + (5  * height) - (6.76 * age))) - 300,0)
    else:
        kcal = round((1.3 * (655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))) - 300,0)
    return int(kcal)

def weight():

    while True:
        try:
            weight = int(input("What is your weight?(in kg) "))
        except:
            print("Please only provide integer")
            continue
        else:
            break   
    return weight

def height():

    while True:
        try:
            height = int(input("What is your height?(in cm) "))
        except:
            print("Please only provide integer")
            continue
        else:
            break
    return height


def gender():
    gender = "wrong"
    while gender not in ('M','F'):
        gender = input("What is your gender?(M/F) ")
        if gender not in ('M','F'):
            print("Please only provide 'M' or 'F'")
            continue
        else:
            break
    return gender

def age():

    while True:
        try:
            age = int(input("What is your age? "))
        except:
            print("Please only provide integer")
            continue
        else:
            break
    return age