

# Building a number pattern generator that takes an integer input and returns a string of numbers from 1 to that integer, separated by spaces using freecodecamp's test-driven development approach.
def number_pattern(n):
    # User Story 4: Check if the input is actually an integer
    if type(n) is not int:
        return "Argument must be an integer value."

    # User Story 5: Check if the integer is 1 or greater
    if n < 1:
        return "Argument must be an integer greater than 0."

    # User Stories 2 & 3: Loop from 1 up to n, and build the string
    result = ""
    for i in range(1, n + 1):
        result += str(i) + " "

    return result
