import sys
import matplotlib.pyplot as plt
import numpy as np

#Survey about individuals parameters

gender = input("What is your gender?(M/F) ")
age = input("How old are you? ")
height = input("What is your height?(in cm) ")
weight = input("What is your weight?(in kg) ")

#Defining variables

age = float(age)
weight = float(weight)
height = float(height)
heightDevided = float(height) / 100
BMI = weight / (heightDevided ** 2)
roundedBMI = round(BMI,2)
minWeight = round(18.5 * heightDevided ** 2,1) #Correct min weight
maxWeight = round(24.9 * heightDevided ** 2,1) #Correct max weight
kgPday = 300/7000            #Weight loss/gain with 300 calories deficit/surplus

#Defining correct kcal intake based on Harris-Benedict equatation

if gender == "M":
    kcal = round((1.3 * (66 + (13.7 * weight) + (5  * height) - (6.76 * age))) - 300,0)
else:
    kcal = round((1.3 * (655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))) - 300,0)


#Results 

print("\nYour BMI is {}" .format(roundedBMI))
print("Correct BMI should be between 18.5 and 24.9")
print("Correct weight should be between {}kg and {}kg".format(minWeight,maxWeight))

if roundedBMI > 24.9:
    print("\nYou are a little bit overweight, try healthier diet and excercising!\n\nFor healthy weight reduction you should start eating about {} kcal a day" .format(kcal))
          
elif roundedBMI < 24.9 and roundedBMI >= 18.5:
    print("\nYour weight is ok, congratulations!")

else:
    print("\nYou are underweight, try gaining some kilograms!\n\nFor healthy weight gain you should start eating about {} kcal a day" .format(kcal))


if roundedBMI > 24.9: 
    correctWeight = weight - maxWeight #number of kg over correct weight
    rng = round(correctWeight / kgPday) #number of days needed to accomplish correct weight
    daysAxis = np.arange(0, rng, 1) #definition of "days" axis
    weightAxis = weight - daysAxis * 0.043 #definition of "weight" axis
    print("Following this rule you will reach correct weight in about {} days.".format(rng))

elif roundedBMI < 18.5: 
    correctWeight = minWeight - weight #number of kg under correct weight
    rng = round(correctWeight / kgPday) #number of days needed to accomplish correct weight
    daysAxis = np.arange(0, rng, 1) #definition of "days" axis
    weightAxis = weight + daysAxis * 0.043 #definition of "weight" axis
    print("Following this rule you will reach correct weight in about {} days.".format(rng))
   
else: sys.exit("The End")

print("\nGraph showing this path in simplified way:")
# plotting the points
plt.plot(daysAxis, weightAxis)
plt.xlabel("Days")
plt.ylabel("Weight")
 
# function to show the plot
plt.show()
