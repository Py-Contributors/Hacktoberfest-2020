# Python code to demonstrate the use of mode() function

# mode() function a sub-set of the statistics module
# We need to import statistics module before doing any work
import statistics

# declaring a simple data-set consisting of real valued
# positive integers.
set =[1, 2, 3, 3, 4, 4, 4, 5, 5, 6]

# Printing out mode of given data-set
print("Mode of given data set is % s" % (statistics.mode(set)))
