import sys
import os
# 1: Open text file
# 2: scan line
# increment line (i)
# break @ Newline
# break at //

# why not do <Newline symbol || "//"

# symbol table
symbol_table = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6,
                'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15, 'SCREEN': 16384, 'KBD': 24576}
custom_table = {}


# 1: #1: Open text file
asm_lines = []
assembly_line = 0
number_of_labels = 0

# Parser#1 -- Strip Slashes/White space / scan labels and add labels
filename = os.path.splitext(sys.argv[1])[0]
with open(sys.argv[1], 'r') as file_asm:  # Open File
    for line in file_asm:
        # Split away everything after double slash
        line, sep, tail = line.partition('//')
        # and replace all white spaces and \n
        line = line.strip('\n').replace(" ", "")
        if line:  # if not null do:
            if line[0] == '(':  # Labels go to custom table, line gets nulled (Increment still)
                custom_table[str(line[1:-1])
                             ] = str(assembly_line-number_of_labels)
                line = None
                number_of_labels = number_of_labels+1  # keep numbers of labels in mind
            if line:
                asm_lines.append(line)
            assembly_line = assembly_line+1
file_asm.close()


# Parser 2 Takes Labels into values
tmp_lines = []
custom_var = 15

# Parser2, convert built in symbols to numbers, scan the ( locations) + populate custom dict, make a next pass.

for line in asm_lines:
    if line[0] == "@":
        if str(line[1:]).isdigit():
            line = line

        elif str(line[1:]) in symbol_table.keys():
            line = '@'+str(symbol_table[line[1:]])

        elif str(line[1:]) in custom_table.keys():
            line = '@'+str(custom_table[line[1:]])
        else:
            custom_var = custom_var+1
            custom_table[str(line[1:])] = str(custom_var)
            line = '@'+str(custom_table[line[1:]])

    if line:
        tmp_lines.append(line)


# finally make a hack file

# dicts for binary creation
dest_table = {'null': '000', 'M': '001', 'D': '010', 'MD': '011',
              'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'}
# Merged A + comp in single command, its a bit hacky but should work.
comp_table = {'0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 'A': '0110000', 'M': '1110000', '!D': '0001101', '!A': '0110001', '!M': '1110001', '-D': '0001111', '-A': '0110011', '-M': '1110011', 'D+1': '0011111', 'A+1': '0110111',
              'M+1': '1110111', 'D-1': '0001110', 'A-1': '0110010', 'M-1': '1110010', 'D+A': '0000010', 'D+M': '1000010', 'D-A': '0010011', 'D-M': '1010011', 'A-D': '0000111', 'M-D': '1000111', 'D&A': '0000000', 'D&M': '1000000', 'D|A': '0010101', 'D|M': '1010101'}
jump_table = {'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
              'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}
# End binary dicts


# Create a hack file to write and convert to binary
with open(filename+".hack", 'w') as file_hack:
    for line in tmp_lines:

        if line[0] == "@":
            address = line[1:]
            # A Commands get leading 0 and 15 padded binary val
            val = '0'+'{0:015b}'.format(int(address))

        else:
            dest = 'null'
            jump = 'null'
            # Default line is always a comp, we use splitting to decide if
            comp = line
            if ';' in comp:                 # There are other values we should store
                comp, sep, jump = comp.partition(';')  # Jump
            if '=' in comp:
                dest, sep, comp = comp.partition('=')  # Dest

            # Using dictionary lookup here instead of switch
            dest = dest_table[dest]
            comp = comp_table[comp]
            jump = jump_table[jump]

            val = '111'+comp+dest+jump  # comp command val is populated here
        # Write val to array
        file_hack.write(str(val)+"\n")  # write to file.
file_hack.close()
