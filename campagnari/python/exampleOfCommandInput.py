#!/usr/bin/env python3
#
# This is an example of how to setup options and
# parameters.
#
# try typing "./exampleOfCommandInput -h"      or
#            "./exampleOfCommandInput --help" 
#
#
# This "imports" the package for parsing commands
import argparse

# The ArgumentParser object will hold the information
# necessary to parse the command line into python data types
parser =  argparse.ArgumentParser(description="Example parser",
                                           add_help=True)

# this is a definition of an "optional argument" which is a string
parser.add_argument('-n', '--name', help="Your name.  Default=Bob",
                    required=False, type=str, default='Bob')

# this is a definition of an "optional argument" which is an int
parser.add_argument('-i', '--intNum', help="An integer number  Default=0",
                    required=False, type=int, default=0)

# this is a definition of an "optional argument" which is a float
# note that this optional argument is actually required (!) 
parser.add_argument('-f', '--floatNum', help="A float",
                   required=True, type=float)

# this is the definition of a boolean
# If you do not specify, it will be False
# If you add "-b" to the command line, it will be True
parser.add_argument('-b', '--boolean', help='A boolean. Default=False',
                    action='store_true')

# this is the definition of the positional arguments
parser.add_argument('someStuff', nargs="+", help="input stuff")


# this is a dictionary contining the optional arguments
args = vars(parser.parse_args())



# Extract the optional arguments into variables
#  CAREFUL.  THESE ARE STRINGS
theName    = args['name']
theInteger = args['intNum']
theFloat   = args['floatNum']
theBool    = args['boolean']
theStuff  = args['someStuff']  

print(type(theFloat))
print(type(theBool))

# print the arguments
print("name =   ",   theName)
print("intNum = ",   theInteger)
print("floatNum = ", theFloat)
print("boolean  = ", theBool)
print("theStuff = ", theStuff)


