import sys
import matplotlib.pyplot as plt
import numpy as np
import BMIFuncions as bmif


# Survey about individuals parameters and defining variables

gender = bmif.gender()
age = bmif.age()
height = bmif.height()
weight = bmif.weight()


# Results 
heightInMeters = bmif.heightInMeters(height)
bmi = bmif.bmi(weight, heightInMeters)
body_parameters = bmif.body_parameters(heightInMeters)
kcal_calc = bmif.kcal_calc(weight,height,age,gender)

print(f"\nYour BMI is {bmi[1]}")
print("Correct BMI should be between 18.5 and 24.9")
print(f"Correct weight should be between {body_parameters[0]} kg and {body_parameters[1]} kg.")

if bmi[1] > 24.9:
    print(f"\nYou are a little bit overweight, try healthier diet and excercising!\n\nFor healthy weight reduction you should start eating about {kcal_calc} kcal a day,")
    print(f"\n then gradually increase that number so you are always on kcal surplus.")
          
elif bmi[1] < 24.9 and bmi[1] >= 18.5:
    print("\nYour weight is ok, congratulations!")

else:
    print(f"\nYou are underweight, try gaining some kilograms!\n\nFor healthy weight gain you should start eating about {kcal_calc} kcal a day,")
    print(f"\n then gradually reduce that number so you are always on deficit")


if bmi[1] > 24.9: 
    correctWeight = weight - body_parameters[1] # Number of kg over correct weight
    rng = round(correctWeight / body_parameters[2]) # Number of days needed to accomplish correct weight
    daysAxis = np.arange(0, rng, 1) # Definition of "days" axis
    weightAxis = weight - daysAxis * 0.043 # Definition of "weight" axis
    print(f"Following this rule you will reach correct weight in about {rng} days.")

elif bmi[1] < 18.5: 
    correctWeight = body_parameters[0] - weight # Number of kg under correct weight
    rng = round(correctWeight / body_parameters[2]) # Number of days needed to accomplish correct weight
    daysAxis = np.arange(0, rng, 1) # Definition of "days" axis
    weightAxis = weight + daysAxis * 0.043 # Definition of "weight" axis
    print(f"Following this rule you will reach correct weight in about {rng} days.")
   
else: sys.exit("Thank you!")

print("\nGraph showing this path in simplified way:")
# Plotting the points
plt.plot(daysAxis, weightAxis)
plt.xlabel("Days")
plt.ylabel("Weight")
 
# Function to show the plot
plt.show()
