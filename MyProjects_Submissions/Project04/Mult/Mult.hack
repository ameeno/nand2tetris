// Basic hack program.

// Mult.asm, Multiplies two numbers using just Add.
// 
// RAM [2] = RAM[0] * RAM[1]
// Put the Numbers you want into RAM[0] and RAM[1]

// Output will be in RAM[2]


(LOOP)
	@R1 // Address i
	D=M // I into memory
	@i // Load r1 address
	D=D-M // Data = data - R1
	@STOP // Stop if greater than 0 (I += R1)
	D;JLT

	@sum // sum initially 0
	D=M 
	@R0     // r0
	D=D+M // add r0's value to current data
	@sum  
	M=D // write this value (old + R0  into data)
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