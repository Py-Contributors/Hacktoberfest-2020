def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap


y = 2020
print(y, "is a leap year") if is_leap(y) else print(y, "is not a leap year")
y = 2011
print(y, "is a leap year") if is_leap(y) else print(y, "is not a leap year")

# output
# 2020 is a leap year
# 2011 is not a leap year
