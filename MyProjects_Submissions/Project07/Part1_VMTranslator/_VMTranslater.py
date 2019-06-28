import os
import sys

from _CodeWriter import CodeWriter
from _Parser import Parser

# Translator calls parser and stars
_vm_parser_outputs = []
_input_arg = sys.argv[1]

_number_of_files_to_parse = 1
_filenames_to_parse = []

translator = Parser()
if ".vm" in _input_arg:
    _filenames_to_parse.append(_input_arg)
else:
    if _input_arg.endswith("/") or _input_arg.endswith("\\"):
        _input_arg = _input_arg[:-1]
    for root, dirs, files in os.walk(_input_arg):
        for file in files:
            if file.endswith(".vm"):
                _number_of_files_to_parse = _number_of_files_to_parse + 1
                _filenames_to_parse.append(file)

for file in _filenames_to_parse:
    if _number_of_files_to_parse > 1:
        file = _input_arg + "\\" + file
    _vm_parser_outputs.append(translator.parse(file))

vm_to_assembly_writer = CodeWriter(_input_arg)
for file in _vm_parser_outputs:
    for line in file:
        if "goto" in line or "label" in line:
            # print("Label "+line)
            line = line.split(" ")
            vm_to_assembly_writer.write_label(line[0], line[1])
            pass
        elif " " in line:
            # print("PushPop "+line)
            line = line.split(" ")
            vm_to_assembly_writer.write_push_pop(line[0], line[1], line[2])

        else:
            # print("Arithmetic "+line)
            vm_to_assembly_writer.write_arithmetic(str(line))
vm_to_assembly_writer.close()
