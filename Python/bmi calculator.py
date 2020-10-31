weight = float(input('Put your weight? (Kg) '))
height = float(input('Put your height? (Mtr) '))
bmi = weight/(height*height)

if bmi <= 18.5:
    print('Your BMI is', bmi, 'which means you are underweight')

elif 18.5 < bmi < 25:
    print('Your BMI is', bmi,'which means you are normal')

elif 25 < bmi < 30:
    print('your BMI is', bmi,' which means you are overweight')

elif bmi > 30:
    print('Your BMI is', bmi,'which means you are obese')