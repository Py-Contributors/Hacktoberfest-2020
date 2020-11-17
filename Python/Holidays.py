from datetime import date 
import holidays 

in_holidays = holidays.HolidayBase() 

# Let's check our republic day 
print('26-01-2019' in in_holidays) 

# Add Holiday without description 
in_holidays.append('26-01-2019') 

# Let's verify 
print('26-01-2019' in in_holidays) # True 

# Let's Check Description 
print(in_holidays.get('26-01-2019')) 

# Add Holiday with description 
in_holidays.append({'26-01-2019':'Republic Day India'}) 
print(in_holidays.get('26-01-2019')) 


# Add list of Dates Together 
in_holidays.append(['02-10-2018', '15-08-2018']) 
print('15-08-2018' in in_holidays) # True 
print('02-10-2018' in in_holidays) # True 

# a single date item 
in_holidays.append(date(2018, 12, 25)) 
print('25-12-2018' in in_holidays) # True 
