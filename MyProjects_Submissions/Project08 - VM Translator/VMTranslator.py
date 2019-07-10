import os
import sys
from sys import platform

from CodeWriter import CodeWriter
from Parser import Parser


# Hard coding filename partition of Multiple OS usability.
osSlash = "/"
if "win" in platform.lower():
    osSlash = "\\"

# Translator calls parser and stars
_vm_parser_outputs = []
_input_arg = sys.argv[1]
initSwitch = False

try:
    if sys.argv[2] == "noswitch" or sys.argv[2] == "-n":
        initSwitch = True
except:
    pass

_number_of_files_to_parse = 1
_filenames_to_parse = []

translator = Parser()

if ".vm" in _input_arg:
    _filenames_to_parse.append(_input_arg)
else:
    if _input_arg.endswith(osSlash):
        _input_arg = _input_arg[:-1]
    for root, dirs, files in os.walk(_input_arg):
        for file in files:
            if file.endswith(".vm"):
                _number_of_files_to_parse = _number_of_files_to_parse + 1
                _filenames_to_parse.append(file)

for file in _filenames_to_parse:
    if _number_of_files_to_parse > 1:
        file = _input_arg + osSlash + file
    _vm_parser_outputs.append(translator.parse(file))

if os.path.isdir(_input_arg):
    filename = os.path.basename(_input_arg)
    CodeW = CodeWriter(_input_arg+osSlash+filename)
else:
    CodeW = CodeWriter(_input_arg)

if initSwitch:
    pass
else:
    CodeW.writeInit()

for file in _vm_parser_outputs:
    for line in file:
        # print(line)
        line = line.split(" ")
        if line[0] == "$$NEW_FILE$$":  # changing filename
            CodeW.set_filename(os.path.basename(line[1]))
        elif line[0] == "goto" or line[0] == "label" or line[0] == "if-goto":
            # print("Label "+line)
            CodeW.write_label(line[0], line[1])

        elif line[0] == "function":
            CodeW.write_function(line[1], line[2])

        elif line[0] == "call":
            CodeW.write_call(line[1], line[2])

        elif line[0] == "return":
            CodeW.write_return()

        elif line[0] == "push" or line[0] == "pop":
            # print("PushPop "+line)
            CodeW.write_push_pop(line[0], line[1], line[2])

        else:
            # print("Arithmetic "+line)
            CodeW.write_arithmetic(line[0])
CodeW.close()
