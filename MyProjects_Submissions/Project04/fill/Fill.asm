// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


@8192 // count 8192 and store in count.
D=A
@count 
M=D 

(LOOP)
	@index
	M=0 // i = 0 used when counter full.

(SCANNER) // monitor kbd
	@KBD
	D=M
	@FILL
	D;JNE // jump to fill if pressed button

(CLEAR) // clear if not pressed

 	@SCREEN
 	D=A
 	@index
 	D=D+M
 	A=D
 	M=0

	@END // jump to counter
	0;JEQ

(FILL) // Fill with increment

 	@SCREEN
 	D=A
 	@index
 	D=D+M
 	A=D
 	M=-1

(END)

// increment index
	@index
	MD=M+1

 	@count
 	D=D-M
 	
 	@LOOP
 	D;JGE
	
	@SCANNER
	0;JEQ