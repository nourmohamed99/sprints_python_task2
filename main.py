def LeapYearCheck(input_year):
    if (input_year % 4) == 0:
        if (input_year % 100) == 0:
            if (input_year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

year = int(input("Enter the Year to be checked: "))
if(LeapYearCheck(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")










