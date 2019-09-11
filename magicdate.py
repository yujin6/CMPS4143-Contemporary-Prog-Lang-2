# -*- coding: utf-8 -*-
"""
Created on Tue Sep 8 18:53:43 2019

@author: Yujin Yoshimura
CMPS 4143 Contemporary Programming Language: Java-Python
Dr. Tina Johnson
Program 1

This program asks the user to enter a month, day, and two-digit year all in
numeric format. Then, it checks to see if the month times the day is equal to
the year. If so, it displays a message stating that the date is magic.
Otherwise, it displays a message stating that the date is not magic.
"""

"""
ask_int
@param: int, int, string
@return: int
Asks user to enter an integer within the range between min and max.
Returns the integer that user has entered.
"""
def ask_int(min, max, str):
    num = -1
    while num <= -1:
        try:
            num = int(input(str))
        except ValueError:
            print("Please enter an integer!")
            num = -1
        if num > max or num < min:
            print("Please enter a valid date!")
            num = -1
    return(num)
        
"""
str_date
@param: int, string, int, string, int
@return: string
Formats the date into a string with the form of mm/dd/yy.
"""
def str_date(mm, str1, dd, str2, yy):
    date = str(mm).zfill(2) + str1 + str(dd).zfill(2) + str2 + str(yy).zfill(2)
    return(date)

"""
check_magic
@param: int, int, int
@return: void
Checks whether the given date is magic or not, then prints a message.
"""
def check_magic(mm, dd, yy):
    date = str_date(mm, "/", dd, "/", yy)
    if mm*dd == yy:
        equation = str_date(mm, " * ", dd, " = ", yy)
        print(date + " is magic because " + equation + ".")
    else:
        equation = str_date(mm, " * ", dd, " ≠ ", yy)
        print(date + " is not magic because " + equation + ".")

"""
main
@param: void
@return: void
Main function.
"""
def main():
    # lists of months with 31 days or 30 days.
    big_month_list = [1, 3, 5, 7, 8, 10, 12]
    small_month_list = [4, 6, 9, 11]
    
    # checks the February 29 issue.
    check = False 
    while not check:
        mm = ask_int(1, 12, "Enter a month (mm): ")
        if mm in big_month_list:
            check = True
            dd = ask_int(1, 31, "Enter a day (dd): ")
        elif mm in small_month_list:
            check = True
            dd = ask_int(1, 30, "Enter a day (dd): ")
        else:
            dd = ask_int(1, 29, "Enter a day (dd): ")
            if dd < 29:
                check = True
        yy = ask_int(0, 99, "Enter a year (yy): ")
        if yy%4 == 0:
            check = True
        else:
            print("Feb. 29 does not exist on year " +  str(yy).zfill(2) + "!")
    
    print("The date you entered is " + str_date(mm, "/", dd, "/", yy) + ".")
    check_magic(mm, dd, yy)

if __name__ == '__main__':
    main()
