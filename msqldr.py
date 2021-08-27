#!/usr/bin/env python3
#
# Usage:
#   msqldr.py /var/log/mysql/slow-queries.log > filtered-slow-queries.log
#
# Parse MySQL log slow queries and print filtered unique queries
#
#
#

import sys
import os.path

if __name__ == '__main__':
    selects = {}
    line_num = 0
    PATH = sys.argv[1]

    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        lines = tuple(open(PATH, 'r'))
        for i in range(len(lines)):
            str = lines[i].strip()

            if str.lower().find("set timestamp") != -1:
                check = True
                result_str = ""

                for number in range(15):
                    if i+number+1 >= len(lines):
                        break

                    if lines[i+number+1].lower().find("#") != -1:
                        break

                    result_str += lines[i+number+1]


                for key, value in list(selects.items()):
                    if value.lower().find(result_str[:40].lower()) != -1:
                        check = False
                        break
                            
                if check:
                    result_str = result_str.replace("\t", "")
                    result_str = result_str.replace("\n", "")

                    if lines[i-1].lower().find("#") != -1:
                        selects[line_num] = lines[i-1] + result_str
                    else:
                        if lines[i-2].lower().find("#") != -1:
                            selects[line_num] = lines[i-2] + result_str
                        else:
                            selects[line_num] = result_str

                    print(selects[line_num])
                    line_num+=1

                    print("\n")
    else:
        print("File not found: ", sys.argv[1])
