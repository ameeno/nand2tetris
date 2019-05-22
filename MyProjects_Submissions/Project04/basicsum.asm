// Basic hack program.

// Adds up the value of memory units 2 + 3 into register 4.
// Adds up two numbers.
// RAM [4] = RAM[2] + RAM[3]
// Put the Numbers you want into RAM[2] and RAM[3]



@4785      // A = NUM1       // FIRST NUMBER


D=A       // Data = A (NUM1)
@2       // A = 2
M=D       // M[2] = NUM1 (D)


@7324       // A= NUM2       // SECOND NUMBER 
D=A       // Data = A (NUM2)
@3       // A = 3
M=D       // RAM[3] = D(NUM2)



@2 	      // Select A2
D=M       // Data = Value of M[2] (15)
@3       // select A3
D=D+M       // data = value of D + M[3]  22 (D = sum)
@4       // select A[4]
M=D       // Write to M[4] the present value of D (Which is sum of 2 & 3)