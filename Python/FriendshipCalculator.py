alphabet = 'bcghjklmpqtvwxyz'
score = 0
name = input("Enter first name and second name with space in between:-")
for character in name:
    if character in 'aeiou':
        score+=5
    if character in 'friends':
        score+=10
    if character in alphabet:
        score+=alphabet.find(character)
    else:
        score+=0
if score>100:
        print('Your friendship score is :', score)
        print('Congratulations! you both are best friends')
else:
        print('Your friendship score is', score)
