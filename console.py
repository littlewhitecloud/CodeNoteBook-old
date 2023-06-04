# An easy console support cmd(Command).exe all function
# Summary :
# 	Support all cmd(Command).exe function
#	Can add own function
#   Support UWP blur and acrylic
#   Smooth move~~~ (Doge
#   Blur:
#      Add Custom hex color
#      Use better blur
# For CodeNoteBook Console
# Add console functions
# Add run file functions

# Import
from os import system, getcwd

# Variable
__version__ = "1.0.6"
__author__ = "Xiao_Bai_Yun"
__name__ = "Console"
__about__ = "%s %s %s" % (__author__, __name__, __version__)
__blur__ = False
__acrylic__ = True
__accent__ = 3
__info__ = """
%s
# An easy console support cmd(Command).exe all function
# Summary :
# 	Support all cmd(Command).exe function
#	Can add own function
""" % (__about__)
__help__ = """
help CodeNoteBook's help && Console's help && Command's help
about Console's about
info Console's info
exit Exit Console

function.py -- CodeNoteBook's MainLoop
console.py -- CodeNoteBook's Console
settings.py -- CodeNoteBook's Settings
language.py -- CodeNoteBook's Language
"""
_init = True
_exit = False

if __blur__:
	from ctypes import windll
	from windowblur import blur
	hwnd = windll.user32.GetForegroundWindow()
	blur(hwnd = hwnd,Acrylic = __acrylic__, AccentState = __accent__) #Custom AccentState
# Init
if _init:
	system("cls")
	system("title Console")
	print(__about__)
	
# MainLoop
while not _exit:
	op = input("PS" + ' ' +  getcwd() + '>')
	if op == "exit": # Replace cmd exit
		_exit = True
	elif op == "info": # Add own function
		print(__info__)
	elif op == "about": # Add own function
		print(__about__)
	elif op == "help":
		print(__help__)
		system(op)
	else:
		try:
			system(op)
		except KeyboardInterrupt:
			pass
		except EOFError:
			pass
