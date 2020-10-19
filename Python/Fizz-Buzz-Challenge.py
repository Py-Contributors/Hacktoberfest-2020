## This is a common interview question.
##Here you have to print FizzBuzz if the input value is devisable by 3 and 5. 
# Or if it is devisable by only 3, print Fizz. 
# If it is devisable by only 5, print Buzz


def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(3))