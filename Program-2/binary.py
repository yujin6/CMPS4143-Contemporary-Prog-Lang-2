# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 01:09:25 2019

@author: Yujin Yoshimura
CMPS 4143 Contemporary Programming Language: Java-Python
Dr. Tina Johnson
Program 1

This program calls a recursive function to display a binary equivalent of the
decimal number. Only positive integers are considered.
When a sentinel value of -1 is entered, this program ends the loop.

The name of the input file is "input.txt", and the output file is "output.txt".
Those files are placed on the same directory of this code.
"""


"""
binary
@param: int
@return: str
Converts from a decimal number to a binary equivalent recursively.
"""
def binary(dec):
    if dec == 1:
        return '1'
    else:
        return binary(dec // 2) + str(dec % 2)

"""
main
@param: void
@return: void
Main function.
"""
def main():
    with open("input.txt", "r") as inf, open("output.txt", "w") as outf:
        for line in inf:
            if int(line) > -1:
                outf.write(binary(int(line)) + '\n')

if __name__ == '__main__':
    main()