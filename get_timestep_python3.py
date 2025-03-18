#!/usr/bin/env python3

"""
Given two values, looks in a 3-column file (output of sham.pl)
to find the time frame that matches closest.
"""

import sys

USAGE = "USAGE: get_timestamp.py -f <sham output> -1 <value 1> -2 <value 2>\n"

# Parse arguments
read_input, read_value1, read_value2 = False, False, False
input_file, value1, value2 = None, None, None
for arg in sys.argv[1:]:
    if read_input:
        read_input = False
        input_file = arg
    elif read_value1:
        read_value1 = False
        value1 = float(arg)
    elif read_value2:
        read_value2 = False
        value2 = float(arg)
    if arg[0] == "-":
        if arg == "-f":
            read_input = True
            continue
        elif arg == "-1":
            read_value1 = True
            continue
        elif arg == "-2":
            read_value2 = True
        else:
            print(USAGE)
            sys.stderr.write(f'ERROR: Option not recognized: {arg}\n')
            sys.exit(1)

if not input_file:
    print(USAGE)
    sys.stderr.write('ERROR: You forgot to provide an input file.\n')
    sys.exit(1)

# Open sham output
x_values, y_values, time_values = [], [], []
with open(input_file) as fhandle:
    for line in fhandle:
        if line[0] != "#" and len(line.split()) == 3:
            t, x, y = line.split()
            x_values.append(float(x))
            y_values.append(float(y))
            time_values.append(float(t))

def find_common_frame(min_x, min_y):
    for xval in min_x:
        xframe = xval[0]
        for yval in min_y:
            yframe = yval[0]
            if xframe == yframe:
                return (xframe, xval[1], yval[1])
    return (None, None, None)

# If you cannot find anything, try increasing the nval variable  1000000ps = 1us
nval = 1000000
min_x = sorted(enumerate(x_values), key=lambda x: abs(x[1] - value1))[:nval]
min_y = sorted(enumerate(y_values), key=lambda x: abs(x[1] - value2))[:nval]

frame, x, y = find_common_frame(min_x, min_y)

if not frame:
    print("No timestamp found..")
    sys.exit(0)

print(f"## T = {time_values[frame]} ({x}, {y})")
