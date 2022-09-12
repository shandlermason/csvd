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
    t = type(s)
    return t(s)


def push(t, u):
    t[1 + len(t)] = u
    return u


the = {}
group1 = re.findall(r"[−][−]([\w]+)", options)  # word after the 2 dashes
group2 = re.findall(r"((?<= = ).*)", options)  # what is after equal sign
print(group1)
for k in group1:
    for x in group2:
        the[k] = coerce(x)
        group2.remove(x)
        break

