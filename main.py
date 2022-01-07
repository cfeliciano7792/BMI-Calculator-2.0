# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#calculates BMI
bmi = round((weight / (height**2)))

#If/else statements to determine which condition is true

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
    
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
