# getting input from the user and assigning it to user

height = float(input("Enter height in Meters: "))
weight = float(input("Enter weight in KG: "))

# the formula for calculating bmi

bmi = weight/(height**2)
# ** is the power of operator i.e height*height in this case

print("Your BMI Is:- {0} And You Are :- ".format(bmi), end='')

# conditions
if (bmi < 16):
    print("You Are Severely UnderWeight")

elif (bmi >= 16 and bmi < 18.5):
    print("UnderWeight")

elif (bmi >= 18.5 and bmi < 25):
    print("Healthy")

elif (bmi >= 25 and bmi < 30):
    print("OverWeight")

elif (bmi >= 30):
    print("Severely OverWeight")
