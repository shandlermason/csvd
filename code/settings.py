import re
import gsub

help = """
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

"""


# What does this do??
def coerce(s, fun):
    def fun(s1):
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1

    return int(s) or fun(re.match("^%s*(.-)%s*$", s))


# Create 'the' variables
the = {}


def unnamed(k, x):
    the[k] = coerce(x)


gsub("\n [−][%S]+[%s]+[−][−]([%S]+)[^\n]+= ([%S]+)", unnamed(), help)  # line 34-36


# 'o' generates string from a nested table
def o(t, show, u):
    if type(t) != "table":
        str(t)

    def show(k, v):
        if not str(k):
            re.findall("^_")
            v = o(v)
            return len(t) == 0 and str.format(":%s %s", k, v) or str(v)
        u = {}
        for k, v in t:
            u[1 + len(u)] = show(k, v)
        if len(t) == 0:
            u.sort()

    return {"..table.concat(u," ").."}  # what does this do??


# prints the string from 'o'
def oo(t):
    print(o(t))
    return t
