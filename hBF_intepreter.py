from pickle import *

class FunctionError(Exception):
    pass

def codify(path):
    code = str()
    with open(path, "rb") as f:
        x = load(f)
    if x[0] != str():
        code += codify(x[0])
    code += x[1]
    return code

def intepreter(code):
    try:
        array = [0]
        second_array = [0]
        third_array = [0]

        sb_1 = 0
        sb_2 = 0

        pointerLocation = 0
        second_pointerLocation = 0
        third_pointerLocation = 0
        funcs = 0
        ftgt = 1
        i = 0
        prev_i = list()

        if "S" in code:
            f = "S"
            for char in code:
                if char == f:
                    if f == "S":
                        f = "E"
                    elif f == "E":
                        f = "S"
                        funcs += 1
            if f == "E":
                raise FunctionError("Mismatched function characters!")


        while i < len(code):
            if code[i] == '<':
                if pointerLocation > 0:
                    pointerLocation -= 1
            elif code[i] == '>':
                pointerLocation += 1
                if len(array) <= pointerLocation:
                    array.append(0)
            elif code[i] == '+':
                array[pointerLocation] += 1
                if array[pointerLocation] > 255:
                    array[pointerLocation] = 0
            elif code[i] == '-':
                array[pointerLocation] -= 1
                if array[pointerLocation] < 0:
                    array[pointerLocation] = 255
            elif code[i] == '.':
                print(chr(array[pointerLocation]), end="")
            elif code[i] == ',':
                x = ord(input("Input ASCII char: "))
                array[pointerLocation] = x
            elif code[i] == '[':
                if array[pointerLocation] == 0:
                    while code[i] != ']':
                        i += 1
            elif code[i] == ']':
                if array[pointerLocation] != 0:
                    while code[i] != '[':
                        i -= 1
            elif code[i] == '^':
                second_pointerLocation += 1
                if len(second_array) <= second_pointerLocation:
                    second_array.append(0)
            elif code[i] == 'v':
                if second_pointerLocation > 0:
                    second_pointerLocation -= 1
            elif code[i] == '\'':
                second_array[second_pointerLocation] += 1
                if second_array[second_pointerLocation] > 255:
                    second_array[second_pointerLocation] = 0
            elif code[i] == ';':
                second_array[second_pointerLocation] -= 1
                if second_array[second_pointerLocation] < 0:
                    second_array[second_pointerLocation] = 255
            elif code[i] == '*':
                print(chr(second_array[second_pointerLocation]), end="")
            elif code[i] == '~':
                x = array[pointerLocation]
                y = second_array[second_pointerLocation]
                array[pointerLocation] = y
                second_array[second_pointerLocation] = x
            elif code[i] == '}':
                third_pointerLocation += 1
                if len(third_array) <= third_pointerLocation:
                    third_array.append(0)
            elif code[i] == '{':
                if third_pointerLocation > 0:
                    third_pointerLocation -= 1
            elif code[i] == '`':
                third_array[third_pointerLocation] += 1
                if third_array[third_pointerLocation] > 255:
                    third_array[third_pointerLocation] = 0
            elif code[i] == '_':
                third_array[third_pointerLocation] -= 1
                if third_array[third_pointerLocation] < 0:
                    third_array[third_pointerLocation] = 255
            elif code[i] == '@':
                print(chr(third_array[third_pointerLocation]), end="")
            elif code[i] == '|':
                x = second_array[second_pointerLocation]
                y = third_array[third_pointerLocation]
                second_array[second_pointerLocation] = y
                third_array[third_pointerLocation] = x
            elif code[i] == '/':
                x = third_array[third_pointerLocation]
                y = array[pointerLocation]
                third_array[third_pointerLocation] = y
                array[pointerLocation] = x
            elif code[i] == ':':
                x = sb_1
                y = array[pointerLocation]
                sb_1 = y
                array[pointerLocation] = x
                x = sb_2
                y = third_array[third_pointerLocation]
                sb_2 = y
                third_array[third_pointerLocation] = x
            elif code[i] == '=':
                x = sb_1
                y = sb_2
                sb_1 = y
                sb_2 = x
            elif (code[i] == '!') and (sb_1 != sb_2):
                x = sb_1
                y = second_array[second_pointerLocation]
                sb_1 = y
                second_array[second_pointerLocation] = x
            elif (code[i] == '$') and (sb_1 != sb_2):
                x = sb_2
                y = second_array[second_pointerLocation]
                sb_2 = y
                second_array[second_pointerLocation] = x
            elif (code[i] == '#') and (sb_1 == sb_2):
                x = sb_1
                y = sb_2
                z = second_array[second_pointerLocation]
                sb_2 = x
                second_array[second_pointerLocation] = y
                sb_1 = z
            elif (code[i] == '%') and (sb_1 == sb_2):
                x = sb_1
                y = sb_2
                z = second_array[second_pointerLocation]
                second_array[second_pointerLocation] = x
                sb_2 = z
                sb_1 = y
            elif code[i] == '(':
                if array[pointerLocation] == sb_1:
                    while code[i] != ')':
                        i += 1
            elif code[i] == ')':
                if array[pointerLocation] != sb_2:
                    while code[i] != '(':
                        i -= 1
            elif code[i] == 'a':
                x = sb_1 + sb_2
                while x > 255:
                    x -= 255
                second_array[second_pointerLocation] = x
            elif code[i] == 's':
                x = sb_1 - sb_2
                while x < 0:
                    x = 255 - abs(x)
                second_array[second_pointerLocation] = x
            elif code[i] == 'm':
                x = sb_1 * sb_2
                while x > 255:
                    x -= 255
                second_array[second_pointerLocation] = x
            elif code[i] == 'd':
                x = sb_1 // sb_2
                second_array[second_pointerLocation] = x
            elif code[i] == 'i':
                x = int(input("Input number: "))
                if x > 255:
                    while x > 255:
                        x -= 255
                elif x < 0:
                    while x < 0:
                        x = 255 - abs(x)
                array[pointerLocation] = x
            elif code[i] == 'o':
                print(array[pointerLocation], end="")
            elif code[i] == 'U':
                ftgt += 1
                if funcs == 0:
                    raise FunctionError("No functions present!")
                elif ftgt > funcs:
                    ftgt = 1
            elif code[i] == 'D':
                ftgt -= 1
                if funcs == 0:
                    raise FunctionError("No functions present!")
                elif ftgt < 1:
                    ftgt = funcs
            elif code[i] == 'S':
                while code[i] != 'E':
                    i += 1
            elif code[i] == 'E':
                i = prev_i[-1]
                prev_i.pop()
            elif code[i] == 'G':
                if funcs == 0:
                    raise FunctionError("No functions present!")
                prev_i.append(i)
                x = 0
                for char_i in range(len(code)):
                    if code[char_i] == "S":
                        x += 1
                        if x == ftgt:
                            i = x
                            break


            i += 1
    except Exception as e:
        print(f"PROGRAM ENDED EARLIER THAN EXPECTED DUE TO: {e}")
