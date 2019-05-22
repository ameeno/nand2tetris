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



(LOOP)
	@SCREEN
	D=A
	@index
	M=D //Index is the first location of the screen

(SCANNER) // monitor kbd
	@KBD
	D=M
	@FILL
	D;JNE // jump to fill if pressed button

(CLEAR) // clear if not pressed

 	@index
 	A=M // Current index to address
 	M=0      
	@END 
	0;JEQ     // jump past the fill function.

(FILL) // Fill with increment

 	@index
 	A=M      // current index
 	M=-1     // fill with -1 representing 11111111

(END)

// increment index
	@index
	MD=M+1

 	@KBD  // grab the address of KBD Which is exactly 8192 ABove SCREEN in our HACK computer.
 	D=A-D // Data is KBD Address - Current Index Value.

 	@LOOP
 	D;JLE // If pixels remain, back to scanner, else loop again.
	
	@SCANNER
	0;JEQ