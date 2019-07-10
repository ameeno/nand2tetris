class Parser:

    def parse(self, input_file_vm):
        self.vm_commands = []
        self.vm_commands.append("$$NEW_FILE$$ "+str(input_file_vm))
        with open(input_file_vm, 'r') as file_VM:
            for line in file_VM:
                # Split away everything after double slash
                line, sep, tail = line.partition('//')
                # strip NewLine
                line = line.strip().replace('\n', "").replace("\t", "")
                if line == "":
                    pass
                else:
                    self.vm_commands.append(str(line))
        return self.vm_commands
