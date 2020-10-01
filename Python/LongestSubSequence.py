def SubSeq(str1,str2):
    m = len(str1)
    n = len(str2)

    i,j=0,0
    while(i<n and j < m):
        if(str1[j]==str2[i]):
            j+=1
        i+=1

    return (j==m)

def longeststring(words,s):
    ans = ""
    length = 0
    for word in words:
        if length < len(word) and SubSeq(word,s):
            ans = word
            length = len(word)


    return ans
s = str(input("Enter String:"))
words = ["able", "ale", "apple", "bale", "kangaroo"]
print("ANS : {}".format(longeststring(words,s)))
