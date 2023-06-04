from tkinter import *
from tkinter.ttk import Button
from ctkutils import Tk, Toplevel
from PIL import Image,ImageTk
from os import getcwd, getenv
import winsound

systemroot = getenv("SYSTEMROOT") + "\\System32\\"

def modulemessagebox(title,message,cilck,command,font,icon,more = False,itransient = True):
	"Messagebox's Module"
	master = Tk()
	master.withdraw()
	messagebox = Toplevel() # set window
	messagebox.title(title) # set title
	messagebox.minsize(375,150) # set height&weight
	#messagebox["background"] = "white"
	if itransient:
		messagebox.transient(master)
	else:
		messagebox.resizable(width = False,height = False) # set resizeable # New in transient
	
	try:
		messagebox.iconphoto(False,PhotoImage(file=icon)) # set icon
	except:
		pass
	
	if font:
		pass
	else:
		font = ("Consolas", 10, "normal") # set font
		
	load = Image.open(icon)   # open image
	load = load.resize((55, 55)) # resize the image
	image = ImageTk.PhotoImage(load)  # read opened image
	
	# set picture
	Picture = Label(messagebox,image=image,\
		highlightthickness = 0, borderwidth = 0,\
		)
	Picture.pack(side = LEFT,fill = X,padx = 25,pady = 10)
	if more:
		textframe = Frame(messagebox)
		scrollbarx = Scrollbar(textframe)
		Moretext = Text(textframe,yscrollcommand = scrollbarx.set,wrap = "none",relief = "flat")
		Moretext.configure(font=("Consolas", 10, "normal"))
		Moretext.config(tabs=("1c","2c"))
		Moretext.insert(INSERT,message)
		Moretext["state"] = "disable"
		scrollbarx.config(command = Moretext.yview)
		scrollbarx.pack(side = RIGHT, fill = Y)
		Moretext.pack(fill = BOTH, expand = True)
		textframe.pack(fill = Y, expand = True)
	else:	
		# set message
		Message = Label(messagebox,text = message,\
			highlightthickness = 0, borderwidth = 0,\
			font = font)
			
		Message.pack(side = LEFT,fill = X,padx = 50,pady = 10) # create 
															# message
		
	if command:
		pass
	else:
		command = messagebox.destroy # set command
			
	Show = Frame(messagebox) # set frame
	Cilck = Button(Show,text = cilck,command = command) # set button
	Cilck.pack(side = BOTTOM,fill = X) # create button	
	Show.pack(side = BOTTOM,fill = X) # create frame
	messagebox.mainloop() # create window

def showinfo(title,message,font = '',more = False,itransient = True):
	"Show Info"
	icon = systemroot + "SecurityAndMaintenance.png"
	winsound.MessageBeep(eval("winsound.MB_ICONASTERISK"))
	modulemessagebox(message = message,title = title,cilck = 'Ok',command = '',font = font,icon = icon,more = more,itransient = itransient)

def showalert(title,message,font = '',more = False,itransient = True):
	"Show alert"
	icon = systemroot + "SecurityAndMaintenance_Alert.png"
	winsound.MessageBeep(eval("winsound.MB_ICONHAND"))
	modulemessagebox(message = message,title = title,cilck = 'Ok',command = '',font = font,icon = icon,more = more,itransient = itransient)

def showerror(title,message,font = '',more = False,itransient = True):
	"Show error"
	icon = systemroot + "SecurityAndMaintenance_Error.png"
	winsound.MessageBeep(eval("winsound.MB_ICONHAND"))
	modulemessagebox(message = message,title = title,cilck = 'Ok',command = '',font = font,icon = icon,more = more,itransient = itransient)

def askyesorno():
	pass
