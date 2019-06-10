// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

//Initialise vars to zero
@R2
M=0
@sum
M=0
@n
M=0



// Jump to end if 0 or less
@R1
D=M
@END
D;JLE


@n
M=D
(LOOP)
@R0
D=M
@sum
M=M+D
@n
M=M-1
D=M
@LOOP
D;JGT
(STOP)
@sum
D=M
@R2
M=D
(END)
@END
0;JMP

// write the loop
