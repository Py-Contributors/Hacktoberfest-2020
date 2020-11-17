print("-------------------------------------\n")

year = int(input("Enter year :- \n")

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year\n".format(year))
       else:
           print("{0} is not a leap year\n".format(year))
   else:
       print("{0} is a leap year\n".format(year))
else:
   print("{0} is not a leap year\n".format(year))
   
print("----------------------------------------\n")
