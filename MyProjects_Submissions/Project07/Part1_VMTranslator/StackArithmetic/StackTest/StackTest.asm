//push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
//eq
@SP
AM=M-1
D=M
A=A-1
A=M
D=A-D
@$LABEL$0
D;JEQ
@SP
A=M-1
M=0
(RET$0)
//push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
//eq
@SP
AM=M-1
D=M
A=A-1
A=M
D=A-D
@$LABEL$1
D;JEQ
@SP
A=M-1
M=0
(RET$1)
//push constant 16
@16
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 17
@17
D=A
@SP
M=M+1
A=M-1
M=D
//eq
@SP
AM=M-1
D=M
A=A-1
A=M
D=A-D
@$LABEL$2
D;JEQ
@SP
A=M-1
M=0
(RET$2)
//push constant 892
@892
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D
//lt
@SP
AM=M-1
D=M
A=A-1
A=M
D=A-D
@$LABEL$3
D;JLT
@SP
A=M-1
M=0
(RET$3)
//push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 892
@892
D=A
@SP
M=M+1
A=M-1
M=D
//lt
@SP
AM=M-1
D=M
A=A-1
A=M
D=A-D
@$LABEL$4
D;JLT
@SP
A=M-1
M=0
(RET$4)
//push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 891
@891
D=A
@SP
M=M+1
A=M-1
M=D
//lt
@SP
AM=M-1
D=M
A=A-1
A=M
D=A-D
@$LABEL$5
D;JLT
@SP
A=M-1
M=0
(RET$5)
//push constant 32767
@32767
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
//gt
@SP
AM=M-1
D=M
A=A-1
A=M
D=A-D
@$LABEL$6
D;JGT
@SP
A=M-1
M=0
(RET$6)
//push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 32767
@32767
D=A
@SP
M=M+1
A=M-1
M=D
//gt
@SP
AM=M-1
D=M
A=A-1
A=M
D=A-D
@$LABEL$7
D;JGT
@SP
A=M-1
M=0
(RET$7)
//push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 32766
@32766
D=A
@SP
M=M+1
A=M-1
M=D
//gt
@SP
AM=M-1
D=M
A=A-1
A=M
D=A-D
@$LABEL$8
D;JGT
@SP
A=M-1
M=0
(RET$8)
//push constant 57
@57
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 31
@31
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 53
@53
D=A
@SP
M=M+1
A=M-1
M=D
//add
@SP
AM=M-1
D=M
A=A-1
M=M+D
//push constant 112
@112
D=A
@SP
M=M+1
A=M-1
M=D
//sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
//neg
@SP
A=M-1
D=0
M=D-M
//and
@SP
AM=M-1
D=M
A=A-1
M=D&M
//push constant 82
@82
D=A
@SP
M=M+1
A=M-1
M=D
//or
@SP
AM=M-1
D=M
A=A-1
M=D|M
//not
@SP
A=M-1
M=!M
(END)
@END
0;JMP
($LABEL$0)
@SP
A=M-1
M=-1
@RET$0
0;JMP
($LABEL$1)
@SP
A=M-1
M=-1
@RET$1
0;JMP
($LABEL$2)
@SP
A=M-1
M=-1
@RET$2
0;JMP
($LABEL$3)
@SP
A=M-1
M=-1
@RET$3
0;JMP
($LABEL$4)
@SP
A=M-1
M=-1
@RET$4
0;JMP
($LABEL$5)
@SP
A=M-1
M=-1
@RET$5
0;JMP
($LABEL$6)
@SP
A=M-1
M=-1
@RET$6
0;JMP
($LABEL$7)
@SP
A=M-1
M=-1
@RET$7
0;JMP
($LABEL$8)
@SP
A=M-1
M=-1
@RET$8
0;JMP
