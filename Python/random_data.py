# Import the random Library
import random 

# function that return a random element
def random_data (data_list):
  return ("Random element =>",random.choice(data_list))

# select a dataset or make one, example an array of elements
data_list = ['apple', 'kiwi', 'banana', 'orange', 'mango', 'strawberry', 'watermelon', 'pear']

# example of use:
random_data (data_list)