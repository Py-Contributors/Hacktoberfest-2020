''' 
Python Programe To Check if  a String is Palindrome or Not
'''

for i in range(1,3):
    check1 = input("Choose Your Input For Check Palindrome\n For Integer Type --> i \n For Word Type   -->s\n").lower()
    if check1 == 's':
        x = input("Enter Your Word Here :\n").lower()
    elif check1 == 'i':
        x = input("Enter Your Number Here :\n")
    else:
        print("Please Enter I or S only")
        break
    reverse = "" # Empty String to save Reverse value in it.

    #Construct the reverse value/string 
    for i in x:
        reverse = i + reverse   
    #Compare the string and its reverse 
    if (x==reverse):
        print("Yes")
    else:
        print("No")