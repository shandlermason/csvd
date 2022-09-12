import re

options = '''
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD−2 license
USAGE: lua seen.lua [OPTIONS]

OPTIONS:
−e −−eg start−up example = nothing
−d −−dump on test failure, exit with stack dump = false
−f −−file file with csv data = ../data/auto93.csv
−h −−help show help = false
−n −−nums number of nums to keep = 512
−s −−seed random number seed = 10019
S −−seperator field seperator = ,]]

−− Function argument conventions:
−− 1. two blanks denote optionas, four blanls denote locals:
−− 2. prefix n,s,is,fun denotes number,string,bool,function;
−− 3. suffix s means list of thing (so names is list of strings)
−− 4. c is a column index (usually)
'''


# Transforms data type to actual, real data type
def coerce(s):
    return type(s)
    """
    def fun(s1):
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1

    return int(s) or float(s) or fun(re.match("^%s*(.-)%s*$", s))  # regex not right
    """

the = {}
m = re.findall(r"[−][−]([\w]+)|((?<= = ).*)", options)
# 'k' is word after the 2 dashes
# 'x' is what is after equal sign
for k, x in m:  # or just m.group()
    the[k] = coerce(x)  # coerce is transforming 'x' to correct data type


