// Basic hack program.

// Mult.asm, Multiplies two numbers using just Add.
// 
// RAM [2] = RAM[0] * RAM[1]
// Put the Numbers you want into RAM[0] and RAM[1]

// Output will be in RAM[2]


@i
M=0
@sum
M=0


(LOOP)
	@i // Address i
	D=M // I into memory
	@R1 // Load r1 address
	D=D-M // Data = data - R1
	@STOP // Stop if greater than 0 (I += R1)
	D;JGE 

	@sum // sum initially 0
	D=M 
	@R0     // r1
	D=D+M // add r1's value to current data
	@sum  
	M=D // write this value (old + R1  into data)
	@i 
	M=M+1 // increment i
	@LOOP
	0;JMP

(STOP)
	@sum
	D=M
	@R2 // write value into R2
	M=D

(END)
	@END
	0;JMP