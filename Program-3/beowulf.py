# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 01:32:51 2019

@author: Yujin Yoshimura
CMPS 4143 Contemporary Programming Language: Java-Python
Dr. Tina Johnson
Program 3

This program replaces a set of given words in a poem "Beowulf".
The words to be replaced are: from "bairn" to "child", from "bight" to "bay",
from "float" to "ship", from "carle" to "hero".
Note that "bairns" is replaced to "children", while "floater" "floated" are
not replaced. It also counts the number of replacements made.
"""

import re

"""
header
@param: file
@return: void
Writes header into the output file.
"""
def header(outf):
    name = 'Yujin Yoshimura'
    course = 'CMPS 4143 Contemporary Programming Language: Java-Python'
    instructor = 'Dr. Tina Johnson'
    iteration = 'Program 3'
    description = 'This program replaces a set of given words in a poem "Beowulf".\n'
    description += 'The words to be replaced are: from "bairn" to "child", from "bight" to "bay",\n'
    description += 'from "float" to "ship", from "carle" to "hero".\n'
    description += 'Note that "bairns" is replaced to "children", while "floater" "floated" are\n'
    description += 'not replaced. It also counts the number of replacements made.\n'

    
    outf.write(name + '\n')
    outf.write(course + '\n')
    outf.write(instructor + '\n')
    outf.write(iteration + '\n')
    outf.write('\n')
    outf.write(description + '\n')
    outf.write('\n')

"""
replace
@param: string, dictionary, dictionary
@return: string
Replaces the words in the string according to the dictionary,
and counts the number of replacements made.
"""
def replace(line, r_dict, r_count):
    prefix = '\s'
    suffix = '(s)?[;,.!?\\- \n]'
    
    for keys in r_dict:
        #replaces when the initial character is not capitalized:
        if len(re.findall(prefix + keys + suffix, line)) > 0:
            result = re.subn(keys, r_dict[keys], line)
            line = result[0]
            r_count[keys] += result[1]
        #replaces when the initial character is capitalized:        
        if len(re.findall(prefix + capitalize(keys) + suffix, line)) > 0:
            result = re.subn(capitalize(keys), capitalize(r_dict[keys]), line)
            line = result[0]
            r_count[keys] += result[1]
        
    #replaces to the correct plural form:
    line = re.sub('childs', 'children', line)
    return line

"""
capitalize
@param: string
@return: string
Capitalizes the initial character of the string.
"""
def capitalize(str):
    return str[0].upper() + str[1:]

"""
print_count
@param: file, dictionary, dictionary
@return: void
Writes the number of replacements into the output file.
"""
def print_count(outf, r_dict, r_count):
    for keys in r_count:
        outf.write(capitalize(keys) + " has been replaced to " + r_dict[keys])
        outf.write(" for " + str(r_count[keys]) + " times.\n")
    outf.write('\n\n')

"""
main
@param: void
@return: void
Main function.
"""
def main():
    is_poem = False
    poem = ''
    r_dict = {
        "bairn": "child",
        "bight": "bay",
        "float": "ship",
        "carle": "hero"
        }
    r_count = {
        "bairn": 0,
        "bight": 0,
        "float": 0,
        "carle": 0
        }
    
    with open("beowulf.txt", "r", encoding = "utf8") as inf, open("Beowulf2.txt", "w", encoding = "utf8") as outf:
        header(outf)
        for line in inf:
            if len(re.findall('^BEOWULF.\n', line)) > 0:
                is_poem = True
            if is_poem:
                line = replace(line, r_dict, r_count)
                poem += line
        print_count(outf, r_dict, r_count)
        outf.write(poem)

if __name__ == '__main__':
    main()