import sys, os
#1: Open text file
#2: scan line
#increment line (i)
#break @ Newline
#break at //


#why not do <Newline symbol || "//"

## symbol table
symbol_table={'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,
'R0':0,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,
'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,
'R15':15,'SCREEN':16384,'KBD':24576}
custom_table={}

## binary syntax
#1 1 1 ac1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3 


#1: #1: Open text file
asm_lines=[]
linenumbers=0
filename=os.path.splitext(sys.argv[1])[0]
with open(sys.argv[1],'r') as file_asm:
    for line in file_asm:
        line, sep, tail= line.partition('//')
        line=line.strip().replace(" ","")
        if line:
            asm_lines.append(line)
            linenumbers=linenumbers+1

    print (asm_lines)
    print("Line Numbers: "+str(linenumbers-1))

# Printing for test
#file_temp=open("NAME.tmp","w")

## scan strings to make symbols and dump to tmp file

hack_lines=[]
tmp_lines=[]
hack_i=0
custom_var=15
##finally make a hack file
with open(filename+".tmp",'w') as file_tmp:
    for line in asm_lines:
        hack_i=hack_i+1
        if str(line[0])=="(":
            custom_table[str(line[1:-1])]=hack_i-1
            asm_lines.pop(hack_i-1)
    for line in asm_lines:
        if line[0]=="@":
            if str(line[1:]).isdigit():
                line=line
                #hack_lines.append('000'+bin(int(line[1:])))
            elif str(line[1:]) in symbol_table.keys():
                #line[1:]=symbol_table[line[1:]]
                line='@'+str(symbol_table[line[1:]])
                    #hack_lines.append('000'+bin(symbol_table(line[1:])))
            elif str(line[1:]) in custom_table.keys():
                    #custom_table[line[1:]]=hack_i-1
                   # line[1:]=custom_table[line[1:]]
                    line='@'+str(custom_table[line[1:]])
            else:
                    custom_table[str(line[1:])]=custom_var+1
                    line='@'+str(custom_table[line[1:]])
                    custom_var=custom_var+1

 #       else:
 #           line, sep, tail = line.partition('=')
            
        if line:
            file_tmp.write(line+"\n")
            tmp_lines.append(line)
hack_i=0
        for line in tmp_lines:
            if line[0]=="@":
                hack_lines.a="000"+bin(int(line[:1]))
        hack_i=hack_i+1
    print(asm_lines)
    print (hack_lines)
    print("Line Numbers: "+str(linenumbers-1))




#with open(filename+".tmp",'r') as file_hack:

