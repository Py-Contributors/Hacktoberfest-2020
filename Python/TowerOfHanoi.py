# Implement Code to Solve Tower of Hanoi Problem (Issue #38)
# https://github.com/Py-Contributors/Hacktoberfest-2020/issues/38
# Contributed by @tauseefmohammed2 : https://github.com/tauseefmohammed2

def TowerOfHanoi(numDisks, source, intermediate, destination):  
    if(numDisks == 1):  
        print("Move Disk 1 From Pole {} to Pole {}".format(source, destination))  
        return   
    TowerOfHanoi(numDisks - 1, source, destination, intermediate)  
    print("Move Disk {} From Pole {} to Pole {}".format(numDisks, source, destination))  
    TowerOfHanoi(numDisks - 1, intermediate, source, destination)  
  
numDisks = int(input("Enter Number of Disks: "))

# Source : A, Intermediate : B, Destination : C  
TowerOfHanoi(numDisks, 'A', 'B', 'C')

# Input : 3
# Output :
# Enter Number of Disks: 3                                                                                              
# Move Disk 1 From Pole A to Pole C                                                                                     
# Move Disk 2 From Pole A to Pole B                                                                                     
# Move Disk 1 From Pole C to Pole B                                                                                     
# Move Disk 3 From Pole A to Pole C                                                                                     
# Move Disk 1 From Pole B to Pole A                                                                                     
# Move Disk 2 From Pole B to Pole C                                                                                     
# Move Disk 1 From Pole A to Pole C

# Input : 2
# Output :
# Enter Number of Disks: 2                                                                                              
# Move Disk 1 From Pole A to Pole B                                                                                     
# Move Disk 2 From Pole A to Pole C                                                                                     
# Move Disk 1 From Pole B to Pole C
