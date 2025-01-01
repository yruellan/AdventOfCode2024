from typing import List, Tuple
from time import time
from lib import memoize

# f = open("data.txt")
# data = f.read().splitlines()
A = 0
B = 0
C = 0
instructions = [2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0]
# instructions = [0,3,5,4,3,0]
# instructions = data[4].split("Program: ")[1].split(",")
# instructions = list(map(int, instructions))
# f.close()

@memoize
def run_rec(A,B,C,IP):

    if IP >= len(instructions):
        return []

    opcode = instructions[IP]
    operand = instructions[IP+1]

    combo_op = operand

    if operand == 4: combo_op = A
    elif operand == 5: combo_op = B
    elif operand == 6: combo_op = C
    elif operand == 7: raise ValueError("Invalid operand")

    if opcode == 0:
        A = A // (2**combo_op)
    elif opcode == 1:
        B = B ^ operand
    elif opcode == 2:
        B = combo_op % 8
    elif opcode == 3:
        if A != 0 :
            IP = operand - 2
    elif opcode == 4:
        B = B ^ C
    elif opcode == 5:
        return [combo_op % 8] + run_rec(A,B,C,IP+2)
        # if out == []:
        #     return []
        # out.append(combo_op % 8)
        # if out[-1] != instructions[len(out)-1]:
        #     return []
        # return out
    elif opcode == 6:
        B = A // (2**combo_op)
    elif opcode == 7:
        C = A // (2**combo_op)

    return run_rec(A,B,C,IP+2)

def run_op(A,B,C,instructions):
    
    out = []
    IP = 0

    while IP < len(instructions):
        opcode = instructions[IP]
        operand = instructions[IP+1]


        combo_op = operand

        if operand == 4: combo_op = A
        elif operand == 5: combo_op = B
        elif operand == 6: combo_op = C
        elif operand == 7: raise ValueError("Invalid operand")

        if opcode == 0:
            A = A // (2**combo_op)
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = combo_op % 8
        elif opcode == 3:
            if A != 0 :
                IP = operand - 2
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            out.append(combo_op % 8)
            # if out[-1] != instructions[len(out)-1]:
            #     return []
        elif opcode == 6:
            B = A // (2**combo_op)
        elif opcode == 7:
            C = A // (2**combo_op)

        IP += 2
    return out



    
def main():
    t0 = time()
    i = 0
    while True:
        
        r = run_op(i,B,C,instructions)
        # r = run_rec(i,B,C,0)
        if instructions == r:
            print(f"Found : {i=}  { r = }  {1 ^(i // 2) ^4}")
            break

        if i <= 25:
            print(f"{i=} {r=}")
        else : break

        if i % 1_00_000 == 0:
            print(f"i = { format(i, '_d') } {time()-t0:.2f}")

        i += 1

if __name__ == "__main__":
    main()