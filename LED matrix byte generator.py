from tkinter import *

root = Tk()
root.title("byte array generator")

r1,r2,r3,r4,r5,r6,r7,r8 = ([0,0,0,0,0,0,0,0] for i in range(8))
button = [r1,r2,r3,r4,r5,r6,r7,r8]

br1,br2,br3,br4,br5,br6,br7,br8 = ([0,0,0,0,0,0,0,0] for i in range(8))
bOA = [br1,br2,br3,br4,br5,br6,br7,br8]

def printGrid():
	for row in button:
		print(row, "\n")

def click(r,c):
	bOA[r][c].destroy()
	button[r][c] = 1

	bOA[r][c] = Button(root, text=str(r+1)+","+str(c+1), command= lambda r=r, c=c: unclick(r,c), bg="red", relief=SUNKEN)
	bOA[r][c].grid(row=r,column=c)

def unclick(r,c):
	bOA[r][c].destroy()
	button[r][c] = 0

	bOA[r][c] = Button(root, text=str(r+1)+","+str(c+1), command= lambda r=r, c=c: click(r,c))
	bOA[r][c].grid(row=r,column=c)

def setup():
	for r in range(0,8):
		for c in range(0,8):
			bOA[r][c] = Button(root, text=str(r+1)+","+str(c+1), command= lambda r=r, c=c: click(r,c))
			bOA[r][c].grid(row=r,column=c)
def clear():
	for r in range(0,8):
		for c in range(0,8):
			unclick(r, c)
def generate():
	root.clipboard_clear()
	output = '{'
	for r in range(0,8):
		output += 'B'
		for c in range(0,8):
			output += str(button[r][c])
		output += ',\n'
	output = output[:-2]
	output += '}'
	root.clipboard_append(output)
	print(output)
	print("Copied to clipboard!")

setup()

Button(root, text="generate", command=generate).grid(row=9, column=0, columnspan=4, pady=10, sticky=N+E+S+W)
Button(root, text="clear", command=clear).grid(row=9, column=4, columnspan=4, pady=10, sticky=N+E+S+W)

root.mainloop()