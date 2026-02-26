# Before applying the O principle:
# A single function handles multiple operations

def calculate_bad(a, b, op):
    if op == "add": return a + b
    elif op == "sub": return a - b


# After applying the O principle:
# Now there are dedicated functions for each operation, so previous
# Code doesn't have to be changed to extend the whole program

def add(a, b): return a + b
def sub(a, b): return a - b


# "Interface" to access the multiple functions, easily extensible

operations = {"+": add, "-": sub}


# This function does not need to be changed to extend the program

def calculate_good(a, b, symbol):
    return operations[symbol](a, b)


# Extensibility proof:

def mul(a, b): return a * b
operations["*"] = mul
