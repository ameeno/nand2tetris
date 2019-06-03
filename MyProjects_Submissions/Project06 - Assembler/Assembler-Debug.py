## Main Driving force app.


import sys, os
#1: Open text file
#2: scan line
#increment line (i)
#break @ Newline
#break at //


#why not do <Newline symbol || "//"

## symbol table
symbol_table={'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'R0':0,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15,'SCREEN':16384,'KBD':24576}
custom_table={}


#1: #1: Open text file
asm_lines=[]
linenumbers=0

##Parser#1 -- Strip Slashes/White space
filename=os.path.splitext(sys.argv[1])[0]
with open(sys.argv[1],'r') as file_asm:
    for line in file_asm:
        line, sep, tail= line.partition('//')
        line=line.strip('\n').replace(" ","")
        if line:
            asm_lines.append(line)
            linenumbers=linenumbers+1

    print (asm_lines)
    print("Line Numbers: "+str(linenumbers-1))
file_asm.close()
# Printing for test
#file_temp=open("NAME.tmp","w")
## write asm2 for testing
with open(filename+".nowhite",'w') as file_asm2:
    for line in asm_lines:    
        file_asm2.write(str(line)+"\n")
file_asm2.close()

## scan strings to make symbols and dump to tmp file


##Code
label_removed=[]
tmp_lines=[]
hack_i=0
custom_var=15
labelnumber=0
## Parser2, convert built in symbols to numbers, scan the ( locations) + populate custom dict, make a next pass.
with open(filename+".labrem",'w') as file_labrem:
    for line in asm_lines:
        if line[0]=='(':
            custom_table[str(line[1:-1])]=str(hack_i-labelnumber)
            line=None
            labelnumber=labelnumber+1
        hack_i=hack_i+1
        if line:
            label_removed.append(line)
            file_labrem.write(str(line)+"\n")
file_labrem.close()

for line in label_removed:
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
                custom_var=custom_var+1
                custom_table[str(line[1:])]=str(custom_var)
                line='@'+str(custom_table[line[1:]])
    elif line[0]=='(':
        line=None
    if line:
        tmp_lines.append(line)

                

 #       else:
 #           line, sep, tail = line.partition('=')

 ## Write out tmp file for debugging
with open(filename+".tmp",'w') as file_tmp:
    for line in tmp_lines:    
        file_tmp.write(str(line)+"\n")
file_tmp.close()


##finally make a hack file
hack_lines=[]
## dicts for binary creation
dest_table={'null':'000', 'M':'001', 'D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'}
#Merged A + comp in single command, its a bit hacky but should work.
comp_table={'0':'0101010','1':'0111111','-1':'0111010','D':'0001100','A':'0110000','M':'1110000','!D':'0001101','!A':'0110001','!M':'1110001','-D':'0001111','-A':'0110011','-M':'1110011','D+1':'0011111','A+1':'0110111','M+1':'1110111','D-1':'0001110','A-1':'0110010','M-1':'1110010','D+A':'0000010','D+M':'1000010','D-A':'0010011','D-M':'1010011','A-D':'0000111','M-D':'1000111','D&A':'0000000','D&M':'1000000','D|A':'0010101','D|M':'1010101'}
jump_table={'null':'000','JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}
## End binary dicts

    #hack_i=0
    #ACommand="000000000000000"
with open(filename+".hack",'w') as file_hack:     
    for line in tmp_lines:
        #hack_i=hack_i+1
        if line[0]=="@":
            address=line[1:]
            val='0'+'{0:015b}'.format(int(address))
            #file_hack.write(str(val)+"\n")
        else:
            dest=''
            comp=''
            jump=''
            comp=line
            if ';' in comp:
                comp,sep,jump = comp.partition(';')
            if '=' in comp:
                dest,sep,comp = comp.partition('=')
            #dest='null'
    # , jump, comp=''
            #jump='null'
    #           comp='0'
            if jump == '':
                jump='null'
            if dest=='':
                dest='null'
            #if ';' in linestring:
            #    comp, sep, jump = linestring.partition(';')
            #dest, sep, comp = prejump.partition('=')
            dest=dest_table[dest]
            comp=comp_table[comp]
            jump=jump_table[jump]
            ##Logic if not @
            ## binary syntax
    #1 1 1 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3 
    #dest = comp ; jump
            val='111'+comp+dest+jump
        ## Write val to array
        hack_lines.append(str(val))
        file_hack.write(str(val)+"\n")
file_hack.close()
## Write out Hack file


with open(filename+".debug",'w') as file_debug:
   # debug=asm_lines+tmp_lines+hack_lines+custom_table
    file_debug.write("Debug for"+filename+"\n\nAsm Lines:\n")   
    for line in asm_lines:
        file_debug.write(line+"\n")
    file_debug.write("\n\nLabel Removed Lines:\n")
    for line in label_removed:
        file_debug.write(line+"\n")
    file_debug.write("\n\nTMP Lines:\n")
    for line in tmp_lines:
        file_debug.write(line+"\n")
    file_debug.write("\n\nHack Lines:\n")
    for line in hack_lines:
        file_debug.write(line+"\n")
    file_debug.write("\n\nCustom Table Lines:\n")
    for line in custom_table:
        file_debug.write(line+":"+str(custom_table[line])+"\n")
    file_debug.write("\n\nLine Numbers: "+str(linenumbers-1))
file_debug.close()




#with open(filename+".tmp",'r') as file_hack:

