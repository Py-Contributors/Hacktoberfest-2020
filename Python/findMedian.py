# In order to find the median of a list with an even number of elements, you're going to need to find the indices of the middle two elements.
# You can find the middle two elements by halving the length of the array to find the index of the first element, and subtracting one from the first index to find the second index.




def median(number_list):
    sorted_list = sorted(number_list) # sort the numbers in order
    list_length = len(sorted_list)
    if list_length % 2 != 0: # if there are an odd number of elements
        median_index = list_length / 2 # if there were 5 elements, this would be 2 (2.5 rounded down), which is the index of the third number
        list_median = sorted_list[median_index]
    else: # if there are an even number of elements
        median_index1 = list_length / 2 - 1
        median_index2 = list_length / 2
        list_median = (sorted_list[median_index1] + sorted_list[median_index2]) / 2.0 # use a float to ensure we get the actual average
    return list_median

print median([7, 3, 1, 4]) # returns 3.5