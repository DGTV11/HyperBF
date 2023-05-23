class RefrenceError(Exception):
    pass

def compiler(prog=str()):
    ref = str()
    code = str()

    prog_x = prog.split("\n")
    for item in prog_x:
        if "INCLUDE" in item: # Handler for module calls
            item_x = item.split()
            if ref == str():
                ref = item_x[1]
            else:
                raise RefrenceError("Multiple module refrences!")
        elif " &" in item: # Handler for comments
            item_x = item.split(" &")
            code += item_x[0]
        else: # Handler for code-only lines
            code += item
    
    return [ref, code.replace(" ", "")]

