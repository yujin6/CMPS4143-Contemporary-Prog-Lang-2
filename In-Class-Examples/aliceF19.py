# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:49:52 2019
@author: Yujin Yoshimura
    
This program will read from the file alice.txt (Alice in Wonderland)
and will print a list of chapters with the chapter titles to a new file.
"""

import re

with open("alice.txt", "r") as inf, open("alice2.txt", "w") as outf:
    for line in inf:
        y = re.findall('^CHAPTER.*\n', line)
        for text in y:
            outf.write(text)
        