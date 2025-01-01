from typing import List, Tuple

f = open("data.txt")
data = f.read().splitlines()
A = int(data[0].split("Register A: ")[1])
B = int(data[1].split("Register B: ")[1])
C = int(data[2].split("Register C: ")[1])
instructions = data[4].split("Program: ")[1].split(",")
instructions = list(map(int, instructions))
f.close()

out = []
IP = 0

def run_op(opcode : int, operand : int):

    global A,B,C
    global out, IP

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
    elif opcode == 6:
        B = A // (2**combo_op)
    elif opcode == 7:
        C = A // (2**combo_op)

    IP += 2
    return

while IP < len(instructions):
    opcode = instructions[IP]
    operand = instructions[IP+1]
    run_op(opcode, operand)
print(out)
print(",".join(map(str, out)))
print(f"{A = }, {B = }, {C = }")