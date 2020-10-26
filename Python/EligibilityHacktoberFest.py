a = int(input('Enter your number of pull requests '))

if int(a)>=4:
    print('Congratulations!! You are eligible for HacktoberFest')

elif 0<=int(a)<4:
    print('Your have to make {} more pull requests to become eligible for HacktoberFest'.format(4-a))
else:
    print('Please enter a  valid input!!')
