def printSpiralMatrix(matrix):
	ans=[]
	row= len(matrix)
	toprow=0
	bottomrow= row-1
	leftcol= 0
	rightcol= len(matrix[0])-1


	if row==0:
		return ans

	while(toprow<=bottomrow and leftcol<= rightcol):
		for i in range(leftcol, rightcol +1):
			ans.append(matrix[toprow][i])
        toprow+=1

        for i in range(toprow, bottomrow+1):
        	ans.append(matrix[i][rightcol])
        rightcol-=1

        if toprow<=bottomrow:
          for i in range(rightcol, leftcol-1,-1):
             ans.append(matrix[bottomrow][i])
        bottomrow-=1
          
        if leftcol<= rightcol:
          for i in range(bottomrow, toprow-1,-1):
             ans.append(matrix[i][leftcol])
         leftcol+=1   


    return ans          	
