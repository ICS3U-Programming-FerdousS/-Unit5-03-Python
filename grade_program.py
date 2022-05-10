#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: May, 9, 2022
# This program asks the user for their grade level
# then calcuate the middle percentage.


# function for calculating the level percentage
def calc_mark(level):
    if level == "4+":
        percentage = ((95 + 100) / 2)
        return  percentage        
    elif level == "4":
        percentage = ((87 + 94) / 2)
        return percentage
    elif level == "4-":
        percentage = ((80 + 86) / 2)
        return percentage
    elif level == "3+":
        percentage = ((77 + 79) / 2)
        return percentage
    elif level == "3":
        percentage = ((73 + 76) / 2)
        return percentage
    elif level == "3-":
        percentage = ((70 + 72) / 2)
        return percentage
    elif level == "2+":
        percentage = ((67 + 69) / 2)
        return percentage
    elif level == "2":
        percentage = ((63 + 66) / 2)
        return percentage
    elif level == "2-":
        percentage = ((60 + 62) / 2)
        return percentage
    elif level == "1+":
        percentage = ((57 + 59) / 2)
        return percentage
    elif level == "1":
        percentage = ((53 + 56) / 2)
        return percentage
    elif level == "1-":
        percentage = ((50 + 52) / 2)
        return percentage
    elif level == "R":
        return "Below 50"
    # display invalid input for none level input
    else:
       return "-1"
def main():
    # ask for user grade level
    level = input("Enter your level: ")

    # calling the function
    print("Level", level, "has the percentage of ", calc_mark(level),"%")


if __name__ == "__main__":
    main()
