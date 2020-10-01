#Program to check whether two strings are permutations of each other

#Function to check whether the two strings are pernmutations of each other
def arePermutation(str1,str2):
    n1=len(str1)
    n2=len(str2)
    if(n1!=n2):
        return False

    a=sorted(str1)
    b=sorted(str2)


    for i in range (0,n1):
        if(a[i]!=b[i]):
            return False

    return True

if __name__=='__main__':
    str1='test'
    str2='etst'
    if(arePermutation(str1,str2)):
        print('Yes')
    else:
        print('No')
