import sys
import matplotlib.pyplot as plt
import numpy as np
import bmi_functions as bmif

#Survey about individuals parameters and defining variables

gender = bmif.gender()
age = bmif.age()
height = bmif.height()
weight = bmif.weight()

#Results
height_in_meters = bmif.height_in_meters(height)
bmi = bmif.bmi(weight, height_in_meters)
body_parameters = bmif.body_parameters(height_in_meters)
kcal_calc = bmif.kcal_calc(weight,height,age,gender)

print(f"\nYour BMI is {bmi[1]}")
print("Correct BMI should be between 18.5 and 24.9")
print(f"Correct weight should be between {body_parameters[0]} kg and {body_parameters[1]} kg.")

if bmi[1] > 24.9:
    print(f"\nYou are a little bit overweight, try healthier diet and excercising! \
    \n\nFor healthy weight reduction you should start eating about {kcal_calc} kcal a day,")
    print("\n then gradually increase that number so you are always on kcal surplus.")

elif bmi[1] < 24.9 and bmi[1] >= 18.5:
    print("\nYour weight is ok, congratulations!")

else:
    print(f"\nYou are underweight, try gaining some kilograms! \
    \n\nFor healthy weight gain you should start eating about {kcal_calc} kcal a day,")
    print("\n then gradually reduce that number so you are always on deficit")

if bmi[1] > 24.9:
    correct_weight = weight - body_parameters[1] # kg over correct weight
    rng = round(correct_weight / body_parameters[2]) # days needed to accomplish correct weight
    dayx_axis = np.arange(0, rng, 1) #definition of "days" axis
    weight_axis = weight - dayx_axis * 0.043 #definition of "weight" axis
    print(f"Following this rule you will reach correct weight in about {rng} days.")

elif bmi[1] < 18.5:
    correct_weight = body_parameters[0] - weight # kg under correct weight
    rng = round(correct_weight / body_parameters[2]) # days needed to accomplish correct weight
    dayx_axis = np.arange(0, rng, 1) # definition of "days" axis
    weight_axis = weight + dayx_axis * 0.043 # definition of "weight" axis
    print(f"Following this rule you will reach correct weight in about {rng} days.")

else: sys.exit("Thank you!")

print("\nGraph showing this path in simplified way:")
# plotting the points
plt.plot(dayx_axis, weight_axis)
plt.xlabel("Days")
plt.ylabel("Weight")
# function to show the plot
plt.show()
