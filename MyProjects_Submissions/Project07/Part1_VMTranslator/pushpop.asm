//push temp 1
@R6
D=M
@SP
M=M+1
A=M-1
M=D
//pop temp 2
@SP
AM=M-1
D=M
@R7
M=D
//push argument 5
@5
D=A
@ARG
A=D+M
D=M
@SP
AM=M+1
A=A-1
M=D
//pop argument 7
@7
D=A
@ARG
D=D+M
@TMP
M=D
@SP
AM=M-1
D=M
@TMP
A=M
M=D
//push constant 25
@25
D=A
@SP
M=M+1
A=M-1
M=D
//pop constant 18
@18
D=A
@CONSTANT
D=D+M
@TMP
M=D
@SP
AM=M-1
D=M
@TMP
A=M
M=D
//push static 42
@pushpop.42
D=M
@SP
M=M+1
A=M-1
M=D
//pop static 12
@SP
AM=M-1
D=M
@pushpop.12
M=D
//push local 15
@15
D=A
@LCL
A=D+M
D=M
@SP
AM=M+1
A=A-1
M=D
//pop local 4
@4
D=A
@LCL
D=D+M
@TMP
M=D
@SP
AM=M-1
D=M
@TMP
A=M
M=D
//push this 7
@7
D=A
@THIS
A=D+M
D=M
@SP
AM=M+1
A=A-1
M=D
//pop that 8
@8
D=A
@THAT
D=D+M
@TMP
M=D
@SP
AM=M-1
D=M
@TMP
A=M
M=D
//push pointer 5
//pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D
//push pointer 1
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
//pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D
//push pointer 0
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
//pop pointer 2
//push pointer 7
(END)
@END
0;JMP
