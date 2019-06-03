import sys

# symbol / custom tables
symbol_table = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6,
                'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15, 'SCREEN': 16384, 'KBD': 24576}
custom_table = {}

# dicts for binary creation
dest_table = {'null': '000', 'M': '001', 'D': '010', 'MD': '011',
              'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'}
# Merged A + comp in single command, its a bit hacky but should work.
comp_table = {'0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 'A': '0110000', 'M': '1110000', '!D': '0001101', '!A': '0110001', '!M': '1110001', '-D': '0001111', '-A': '0110011', '-M': '1110011', 'D+1': '0011111', 'A+1': '0110111',
              'M+1': '1110111', 'D-1': '0001110', 'A-1': '0110010', 'M-1': '1110010', 'D+A': '0000010', 'D+M': '1000010', 'D-A': '0010011', 'D-M': '1010011', 'A-D': '0000111', 'M-D': '1000111', 'D&A': '0000000', 'D&M': '1000000', 'D|A': '0010101', 'D|M': '1010101'}
jump_table = {'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
              'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}
# End binary dicts

# 1: #1: Open text file
asm_lines = []
line_number = 0
number_of_labels = 0

# Parser#1 -- Strip Slashes/White space / scan labels and add labels
filename = sys.argv[1].strip(".asm")
with open(sys.argv[1], 'r') as file_asm:  # Open File
    for line in file_asm:
        # Split away everything after double slash
        line, sep, tail = line.partition('//')
        # and replace all white spaces and \n
        line = line.strip('\n').replace(" ", "")
        if line:  # if line not null:
            if line[0] == '(':  # Labels go to custom table, line gets nulled (Increment still)
                custom_table[str(line[1:-1])
                             ] = str(line_number-number_of_labels)
                number_of_labels = number_of_labels+1  # keep numbers of labels in mind
            else:
                asm_lines.append(line)  # Add the line to asm_lines
            line_number = line_number+1

# Parser 2 Takes Labels into values
tmp_lines = []
custom_var = 15

# Parser2, convert built in symbols to numbers (custom is aleardy in dict, new variables are incrementally assigned)
for line in asm_lines:
    if line[0] == "@":  # See whats after the A and make a decision:
        if str(line[1:]).isdigit():
            pass
        elif str(line[1:]) in symbol_table.keys():
            line = '@'+str(symbol_table[line[1:]])

        elif str(line[1:]) in custom_table.keys():
            line = '@'+str(custom_table[line[1:]])
        else:
            # This ads an incrementing value to the custom_var on first instance.
            custom_var = custom_var+1
            # Logic dictates, the next time it appears,
            custom_table[str(line[1:])] = str(custom_var)
            # we will use the elif above!
            line = '@'+str(custom_table[line[1:]])

    if line:
        tmp_lines.append(line)  # Temp list from asm list


# Finally Create a hack file to write and convert to binary
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

            # Using dictionary lookup here like a java switch/case
            dest = dest_table[dest]
            comp = comp_table[comp]
            jump = jump_table[jump]

            val = '111'+comp+dest+jump  # comp command val is populated here

        # write val to file, whether A or C command.
        file_hack.write(str(val)+"\n")