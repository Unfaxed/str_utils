
def isArgFlag(arg: str):
    return isArg2Flag(arg) or (arg.startswith("-") and len(arg) > 1 and ' ' not in arg)

def isArg2Flag(arg: str):
    return (arg.startswith("--") and len(arg) > 2 and not ' ' in arg)

def getArgFlag(arg: str):
    return arg[2:] if arg.startswith('--') else arg[1:]

def getFlags(args):
    flags = set()
    vals = {}
    mainArgs = []

    prevWasArg = False
    for i, arg in enumerate(args):
        if (isArgFlag(arg)):
            arg_orig = arg
            arg = getArgFlag(arg)
            flags.add(arg)

            if (i < len(args)-1) and not isArgFlag(args[i+1]):
                vals[arg] = args[i+1]
            prevWasArg = isArg2Flag(arg_orig)
        else: 
            if (not prevWasArg): mainArgs.append(arg)
            prevWasArg = False

    return flags, vals, mainArgs