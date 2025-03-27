def is_leap_year(year):
    """takes a year as input and returns true if its a leap year"""
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True
if is_leap_year(1989):
    print("True")
else:
    print("False")

    