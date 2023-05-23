from hBFx_compiler import *
from hBF_intepreter import *
from pickle import *

ERROR = """
 _______  ______  ______  _____   ______   /
 |______ |_____/ |_____/ |     | |_____/  / 
 |______ |    \_ |    \_ |_____| |    \_ .  
                                            
"""

HELP = """
COMMANDS:
-----------------------------------------------------------------------------
>   Increment the pointer.
<   Decrement the pointer.
+   Increment the byte at the pointer.
-   Decrement the byte at the pointer.
.   Output the byte at the pointer.
,   Input a byte and store it in the byte at the pointer.
[   Jump forward past the matching ] if the byte at the pointer is zero.
]   Jump backward to the matching [ unless the byte at the pointer is zero.
-----------------------------------------------------------------------------
^   Increment the second pointer.
v   Decrement the second pointer.
'   Increment the byte at the second pointer.
;   Decrement the byte at the second pointer.
*   Output the byte at the second pointer.
~   Swap the first and second pointer's bytes.
-----------------------------------------------------------------------------
}   Increment the third pointer.
{   Decrement the third pointer.
`   Increment the byte at the third pointer.
_   Decrement the byte at the third pointer.
@   Output the byte at the third pointer.
|   Swap the second and third pointer's bytes.
/   Swap the third and first pointer's bytes.
-----------------------------------------------------------------------------
:   (byte at the pointer <-> SB_1) and (byte at the third pointer <-> SB_2).
=   (SB_1 <-> SB_2).
!   (SB_1 != SB_2) then (byte at the second pointer <-> SB_1).
$   (SB_1 != SB_2) then (byte at the second pointer <-> SB_2).
#   (SB_1 == SB_2) then (SB_1 -> SB_2 -> byte at the second pointer -> SB_1).
%   (SB_1 == SB_2) then (SB_1 -> byte at the second pointer -> SB_2 -> SB_1).
-----------------------------------------------------------------------------
(   Jump forward past the matching ) if the byte at the pointer is equal to SB_1.
)   Jump backward to the matching ( unless the byte at the pointer is equal to SB_1.
-----------------------------------------------------------------------------
a   Write SB_1 + SB_2 to the byte at the second pointer.
s   Write SB_1 - SB_2 to the byte at the second pointer.
m   Write SB_1 * SB_2 to the byte at the second pointer.
d   Write SB_1 // SB_2 to the byte at the second pointer.
r   Write SB_1 % SB_2 to the byte at the second pointer.
-----------------------------------------------------------------------------
i   Input a number and store it in the byte at the pointer.
o   Output the number at the pointer.
-----------------------------------------------------------------------------
U   Raise the ftgt number by 1.
D   Lower the ftgt number by 1.
-----------------------------------------------------------------------------
S   Begin a function.
E   End a function.
G   Run the function refrenced by the ftgt number.
-----------------------------------------------------------------------------

SPECIAL COMMANDS (ONLY USE IN hBFx FILES!!!):
-----------------------------------------------------------------------------
INCLUDE     Add modules (Order of functions are first refrence one to last main one) (CAN ONLY REFRENCE ONE MODULE (Recursion allowed!)!!!)
&           Comment (Must have space before it!!!) (Just add what you want to comment after the "&"!)
"""

print("""
 _     _ __   __  _____  _______  ______ ______  _______
 |_____|   \_/   |_____] |______ |_____/ |_____] |______
 |     |    |    |       |______ |    \_ |_____] |      
                                                                                                      
""")

while True:
    mode = int(input("""
PLEASE INPUT A MODE
1) hBFx compiler
2) hBF intepreter
3) Help
>>> """))

    if mode == 1:
        path = input("PLEASE INPUT A FILE PATH (MUST BE A .hBFx FILE): ")
        if not path.endswith(".hBFx"):
            print(ERROR, "FILE IS NOT \".hBFx\"!!!")
            continue

        print("COMPILING...")
        npath = path.replace(".hBFx", ".hBF")
        with open(path, "r") as fx:
            with open(npath, "wb") as fy:
                dump(compiler(fx.read()), fy)
        print(f"COMPILED TO \"{npath}\"!")
    elif mode == 2:
        path = input("PLEASE INPUT A FILE PATH (MUST BE A .hBF FILE): ")
        if not path.endswith(".hBF"):
            print(ERROR, "FILE IS NOT \".hBF\"!!!")
            continue
        
        print("LOADING CODE...")
        code = codify(path)
        print("INTEPRETING...\n\n")
        intepreter(code)
        print("\n\n\nFINISHED INTEPRETING!")
    elif mode == 3:
        print(HELP)