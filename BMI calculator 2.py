import sys
import matplotlib.pyplot as plt
import numpy as np

#Survey about individuals parameters

gender = input("What is your gender?(M/F) ")
age = input("How old are you? ")
height = input("What is your height?(in cm) ")
weight = input("What is your weight?(in kg) ")

#Defining variables

a = float(age)
x = float(weight)
y1 = float(height)
y = float(height) / 100
z1 = x / (y ** 2)
z = round(z1,2)
cw1 = round(18.5 * y ** 2,1) #Correct min weight
cw2 = round(24.9 * y ** 2,1) #Correct max weight
kgpday = 300/7000            #Weight loss/gain with 300 calories deficit/surplus

#Defining correct kcal intake based on Harris-Benedict equatation

if gender == "M":
    kcal = round((1.3 * (66 + (13.7 * x) + (5  * y1) - (6.76 * a))) - 300,0)
else:
    kcal = round((1.3 * (655 + (9.6 * x) + (1.8 * y1) - (4.7 * a))) - 300,0)


#Results 

print("\nYour BMI is {}" .format(z))
print("Correct BMI should be between 18.5 and 24.9")
print("Correct weight should be between {}kg and {}kg".format(cw1,cw2))

if z > 24.9:
    print("\nYou are a little bit overweight, try healthier diet and excercising!\n\nFor healthy weight reduction you should start eating about {} kcal a day" .format(kcal))
          
elif z <24.9 and z >= 18.5:
    print("\nYour weight is ok, congratulations!")

else:
    print("\nYou are underweight, try gaining some kilograms!\n\nFor healthy weight gain you should start eating about {} kcal a day" .format(kcal))


if z > 24.9: 
    nd = x - cw2 #number of kg over correct weight
    rng = round(nd / kgpday) #number of days needed to accomplish correct weight
    o1 = np.arange(0, rng, 1) #definition of "days" axis
    o2 = x - o1 * 0.043 #definition of "weight" axis
    print("Following this rule you will reach correct weight in about {} days.".format(rng))

elif z < 18.5: 
    ndw = cw1 - x #number of kg under correct weight
    rng = round(ndw / kgpday) #number of days needed to accomplish correct weight
    o1 = np.arange(0, rng, 1) #definition of "days" axis
    o2 = x + o1 * 0.043 #definition of "weight" axis
    print("Following this rule you will reach correct weight in about {} days.".format(rng))
   
else: sys.exit("The End")

print("\nGraph showing this path in simplified way:")
# plotting the points
plt.plot(o1, o2)
plt.xlabel("Days")
plt.ylabel("Weight")
 
# function to show the plot
plt.show()
 
