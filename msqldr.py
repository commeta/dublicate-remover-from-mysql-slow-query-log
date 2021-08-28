#!/usr/bin/env python3
#
# Usage:
#   msqldr.py /var/log/mysql/slow-queries.log > filtered-slow-queries.log
#
# Parse MySQL log slow queries and print filtered unique queries
#
# Copyright 2021 commeta <dcs-spb@ya.ru>
#

import sys
import os.path

if __name__ == '__main__':
    selects = {}
    line_num = 0
    PATH = sys.argv[1]

    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        # Open file from command line argument 
        lines = tuple(open(PATH, 'r'))
        for i in range(len(lines)):
            # Iterate
            str = lines[i].strip()

            if str.lower().find("set timestamp") != -1:
                # Start query secton
                check = True
                result_str = ""

                for number in range(len(lines)-i-1):
                    # Find end query section
                    if lines[i+number+1].find("#") != -1:
                        break

                    result_str += lines[i+number+1]

                if not result_str:
                    continue

                # Search first 50 symbols
                cropped_str = result_str[:50].lower()
                for key, value in list(selects.items()):
                    # Dublicate detector
                    if value.lower().find(cropped_str) != -1:
                        check = False
                        break

                if check:
                    count_dub = 0

                    for ii in range(len(lines)):
                        str_search = lines[ii].strip()
                        if str_search.lower().find(cropped_str) != -1:
                            count_dub += 1

                    # Remove tabs & new line
                    result_str = result_str.replace("\t", " ")
                    result_str = result_str.replace("\n", " ")

                    # Add Query_time string
                    if lines[i-1].find("#") != -1:
                        selects[line_num] = lines[i-1] + result_str
                    else:
                        if lines[i-2].find("#") != -1:
                            selects[line_num] = lines[i-2] + result_str
                        else:
                            selects[line_num] = result_str

                    print("# Count %d\n%s\n" % (count_dub, selects[line_num]))
                    line_num+=1
    else:
        # Error!
        print("File not found: ", PATH)
