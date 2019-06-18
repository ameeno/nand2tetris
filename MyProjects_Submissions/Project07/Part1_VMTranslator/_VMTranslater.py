import os
import sys

from _CodeWriter import CodeWriter
from _Parser import Parser

# Translator calls parser and stars
my_parsed_vm_code = []
my_input_arg = sys.argv[1]

my_number_of_files = 1
my_unparsed_vm_code = []
my_filenames = []

translator = Parser()
if ".vm" in my_input_arg:
    my_filenames.append(my_input_arg)
else:
    if my_input_arg.endswith("/") or my_input_arg.endswith("\\"):
        my_input_arg = my_input_arg[:-1]
    for root, dirs, files in os.walk(my_input_arg):
        for file in files:
            if file.endswith(".vm"):
                my_number_of_files = my_number_of_files + 1
                my_filenames.append(file)

for file in my_filenames:
    if my_number_of_files > 1:
        file = my_input_arg + "\\" + file
    my_parsed_vm_code.append(translator.parse(file))

my_writer = CodeWriter(my_input_arg)
for file in my_parsed_vm_code:
    for line in file:
        if "goto" in line or "label" in line:
            # print("Label "+line)
            line = line.split(" ")
            my_writer.write_label(line[0], line[1])
            pass
        elif " " in line:
            # print("PushPop "+line)
            line = line.split(" ")
            my_writer.write_push_pop(line[0], line[1], line[2])

        else:
            # print("Arithmetic "+line)
            my_writer.write_arithmetic(str(line))
my_writer.close()
