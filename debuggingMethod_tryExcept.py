try:
    age = int(input("Enter age: "))
except:
    print("You have typed in an invalid input. Please try again with a numerical input like 12")
    age = int(input("Enter age: "))

"""the block of code present under the 'except' block is only executed if invalid input
has been entered by user
Otherwise not executed at all. SIMILAR TO ASSERT, but this one is used to reduce bugs in code
You are expecting an integer input here, but user enters number
in english language which is not favourable"""