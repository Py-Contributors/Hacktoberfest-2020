import random
list=[9,8,7,6,5,4,3,2,1]
while sorted(list) != list:
    random.shuffle(list)

print(list)
