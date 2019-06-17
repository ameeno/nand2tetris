# Importing sys to take arguments (Filename)
import sys
import os


class CodeWriter:
    def __init__(self, output_file_asm):
        self.filename = output_file_asm.strip(".vm") + ".asm"
        self.file_asm = open(self.filename, 'w')
        self.counter = 0
        self.return_tags = []

    def write_asm_output(self, asm_array):
        for line in asm_array:
            self.file_asm.write(line + "\n")

    def close(self):
        self.file_asm.write("(END)\n@END\n0;JMP\n")
        for line in self.return_tags:
            self.file_asm.write(line + "\n")
        print("All Commands Executed Successfully: Translated file is " + self.filename)

    def write_arithmetic(self, command_arithmetic):
        # for debugging write commands in file
        self.file_asm.write("//" + str(command_arithmetic) + "\n")
        command = command_arithmetic
        asm_translation = []
        # do the logic
        if command == "add":  # Add x+y
            asm_translation.append(
                "@SP\nAM=M-1\nD=M\nA=A-1\nM=M+D")
        elif command == "sub":  # Sub x-y
            asm_translation.append(
                "@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D")
        elif command == "neg":  # make y "-y"
            # asm_translation.append("@SP\nD=A\nA=M-1\nM=D-M") testing alternative
            asm_translation.append("@SP\nA=M-1\nM=0-M")

        elif command == "and":  # and(x & y )
            asm_translation.append("@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M")

        elif command == "or":  # or (x or y)
            asm_translation.append("@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M")

        elif command == "not":  # not (not y)
            asm_translation.append("@SP\nA=M-1\nM=!M")
        else:  # counter & Jump required
            asm_translation.append(
                "@SP\nAM=M-1\nD=M\nA=A-1\nA=M\nD=A-D\n@$LABEL$" + str(self.counter))

            if command == "gt":  # gt x > y
                asm_translation.append("D;JGT")
            elif command == "lt":  # LT x <y
                asm_translation.append("D;JLT")
            else:  # EQ x==0
                asm_translation.append("D;JEQ")

            asm_translation.append(
                "@SP\nA=M-1\nM=0\n(RET$" + str(self.counter) + ")")
            self.return_tags.append(
                "($LABEL$" + str(self.counter) + ")\n@SP\nA=M-1\nM=-1\n@RET$" + str(self.counter) + "\n0;JMP")
            self.counter = self.counter + 1
        self.write_asm_output(asm_translation)

    def write_push_pop(self, command_push_pop, segment, index):
        # for debugging write commands in file
        self.file_asm.write("//" + str(command_push_pop) +
                            " " + str(segment) + " " + str(index) + "\n")

        segment_table = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT",
                         "constant": "CONSTANT", "static": "STATIC", "pointer": "PTR", "temp": "TMP"}
        ptr_table = {0: "THIS", 1: "THAT"}
        command = command_push_pop
        segment = segment_table[segment]
        index = int(index)
        static_filename = os.path.basename(self.filename).strip(".asm")
        asm_translation = []
        # do the logic
        # 2 define push pops based on the at command
        if segment == "PTR":
            if index > 1:
                pass
            elif command == "pop":
                asm_translation.append(
                    "@SP\nAM=M-1\nD=M\n" + "@" + ptr_table[index] + "\nM=D")
            else:
                asm_translation.append(
                    "@" + ptr_table[index] + "\nD=M\n@SP\nM=M+1\nA=M-1\nM=D")
        elif segment == "STATIC":
            static_name = static_filename + "." + str(index)
            if command == "pop":
                asm_translation.append(
                    "@SP\nAM=M-1\nD=M\n@" + static_name + "\nM=D")
            else:
                asm_translation.append(
                    "@" + static_name + "\nD=M\n@SP\nM=M+1\nA=M-1\nM=D")
        elif segment == "TMP":
            index = index + 5
            if command == "pop":
                asm_translation.append(
                    "@SP\nAM=M-1\nD=M\n@R" + str(index) + "\nM=D")
            else:
                asm_translation.append(
                    "@R" + str(index) + "\nD=M\n@SP\nM=M+1\nA=M-1\nM=D")
        else:
            asm_translation.append("@" + str(index) + "\nD=A")
            if command == "pop":
                asm_translation.append(
                    "@" + segment + "\nD=D+M\n@TMP\nM=D\n@SP\nAM=M-1\nD=M\n@TMP\nA=M\nM=D")
            else:
                if segment == "CONSTANT":
                    asm_translation.append("@SP\nM=M+1\nA=M-1\nM=D")
                else:
                    asm_translation.append(
                        "@" + segment + "\nA=D+M\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D")
        # write translation
        self.write_asm_output(asm_translation)


class Parser:
    def __init__(self, input_file_vm):
        self.filename = input_file_vm
        self.cw = CodeWriter(input_file_vm)
        # Code Writer
        self.currentCommand = ""
        self.vm_commands = []

        with open(input_file_vm, 'r') as file_VM:
            for line in file_VM:
                # Split away everything after double slash
                line, sep, tail = line.partition('//')
                # and replace all white spaces and \n
                line = line.strip('\n')
                if line:
                    self.vm_commands.append(line)

    def start(self):
        for line in self.vm_commands:
            command_segment = None
            command_index = None
            if line.count(' ') <= 0:
                command_type = line
            else:
                line = line.split()
                command_type = line[0]
                command_segment = line[1]
                command_index = line[2]
            if command_index:
                self.cw.write_push_pop(
                    command_type, command_segment, command_index)
            else:
                self.cw.write_arithmetic(command_type)

        self.cw.close()


# Translator calls parser and stars
translator = Parser(sys.argv[1])
translator.start()
