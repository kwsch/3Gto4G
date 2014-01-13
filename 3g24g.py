from __future__ import with_statement
import os,sys
from gba2nds import makends

def main(inputpk):
	if True == True:
		newpkm = os.path.splitext(inputpk)[0] + " - Transferred.pkm"
		with open(inputpk,'rb') as f:
			with open(newpkm,'wb') as g:
				g.write(makends(f.read()))
	print newpkm
				

def printspacer():
	print "\n/*------------------*/\n"


# Process Drag&Drop
del sys.argv[0]
for item in sys.argv:
	printspacer()
	print "Converting Drag&Drop File:\n%s" % (item)
	main(item)
	
# Process Manual Input
go=1
while go==1:
	printspacer()
	inputpk = raw_input("Instructions: Drag & Drop PKM File into the window, then press Enter.\nFile: ").replace('"', '')
	print ""
	main(inputpk)
	print ""
	if raw_input("Process another? (y/n): ") != "y":
		go=0
		print ""
		raw_input("Press Enter to Exit.")
		break


