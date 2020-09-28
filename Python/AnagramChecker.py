def areAnagrams(str1, str2): 
	len1 = len(str1) 
	len2 = len(str2)

	if len1 != len2: 
		return 0

	str1 = sorted(str1) 
	str2 = sorted(str2) 

	for i in range(0, len1): 
		if str1[i] != str2[i]: 
			return 0

	return 1


print('Enter first string:')
str1 = str(input())

print('Enter second string:')
str2 = str(input())

if areAnagrams(str1, str2): 
	print ("The two strings are anagrams of each other.") 
else: 
	print ("The two strings are NOT anagrams of each other.") 