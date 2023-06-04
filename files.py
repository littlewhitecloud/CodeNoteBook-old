"Get file's attributes"
"Bug++"
# A file's attributes :
#  Name
#  Extention
#  Size
#  Path
#  More...

from tkinter import *
from tkinter.ttk import *
from ctkutils import Toplevel
from tkmessagebox import showinfo
from settings import *
from time import localtime, strftime
from math import pow, ceil
from os import getcwd, path, stat
from PIL import Image as Imageopen
from PIL import ImageTk

extentions = { # Extentions
	"py":"Python File", 
	"pyw":"Python File (no console)",
	"txt":"text file", 
	"md":"Mark Down file", 
	"cfg":"Config file",
	"json":"JavaScript Object Notation file"
}

openwith = {
	"py":"Python",
	"pyw":"Python",
	"txt":"Any Editor",
	"md":"Matk Down Reader",
	"cfg":"Code Editor",
	"json":"Code Editor"
}
	
def _init_(target):
	"Split the filename to filename.ext"
	global name, ext, filename
	filename = target
	filename = filename.split(".")
	name = filename[0]
	ext = filename[-1]

def formattime(times):
	"Format the time to %H:%M:%S"
	currenttime = times
	totalsecond = int(currenttime)
	second = totalsecond % 60
	totalminute = totalsecond // 60
	minutes = totalminute % 60
	totalhour = totalminute // 60
	hours = totalhour % 24 + 8
	if hours >= 24:
		hours -= 24
	return "%d:%d:%d" % (hours, minutes, second)

def formattime_(time):
	"Get file create time"
	ModifiedTime = localtime(time)
	mt = path.getctime(name + '.' + ext)
	
	return strftime("%Y-%m-%d, %H:%M:%S", ModifiedTime)

def filectime():
	"Get create time"
	return formattime_(path.getctime(name + '.' + ext))

def fileatime():
	"Get file last read time"
	return formattime_(path.getatime(name + '.' + ext))

def filemtime():
	"Get file last modified time"
	return formattime_(path.getmtime(name + '.' + ext))

def extention():
	"Return the file extention"
	if ext not in extentions: # Extention not in extention dict
		return "Unknow File"
	return extentions[ext], ext

def fileopenwith():
	"Return the file openwith"
	if ext not in openwith:
		return "Unknow File"
	return openwith[ext]

def changeopenwith():
	"Change the set file ext's openwith"
	showinfo("Tip", "Wait for the setting's update")
	return "Wait for the setting's update"
	
def aboutfile(filename):
	"The GUI of the program"
	if not filename:
		pass
	else:
		filepath = getcwd() + "\\asset\\"
		cfg = init("")
		Master = Tk()
		Master.withdraw()
		File = Toplevel()
		File.transient(Master)
		File.title("%s attributes" % filename)
		File.iconbitmap(filepath + "edit.ico")
		File.geometry("420x560") 
		File.resizable(False, False)
		
		Names = Frame(File)
		Opwith = Frame(File)
		
		load = Imageopen.open(filepath + "file.png") # open image
		load = load.resize((90, 90))
		image = ImageTk.PhotoImage(load)  # read opened image
		
		Picture = Label(Names, image = image)
		Name = Entry(Names, width = 35)
		Name.insert(0, filename)
		Sep = Separator(File, orient = HORIZONTAL)
		
		_init_(filename)
		
		# Type
		# Open with...
		extention_ = extention()
		extention_ = extention_[0] + "(." + extention_[1] + ")"
		openwith_ = fileopenwith()
		
		Type = Label(Opwith, text = "File extention:  " + extention_)
		Openwith = Label(Opwith, text = "Open with:  " + openwith_)
		Change = Button(Opwith, text = "Change", command = changeopenwith)
		
		Sep_ = Separator(File, orient = HORIZONTAL)
		
		# Filepath
		# Size
		# Use Size
		filepath = path.abspath(filename)
		size = path.getsize(filepath)
		kb = round(size / pow(1024, 1), 2)
		kb_ = ceil(kb)
		usesize = '(' + str(kb_ * 1024) + ' ' + "Byte" + ')'
		byte =  str(size) + ' ' + "Byte"
		size = '{:,}'.format(size)
		
		Filepath = Label(File, text = "Path :  " + filepath)
		Size = Label(File, text = "Size :  " + str(kb) + ' ' + "KB" + ' ' + '(' + byte + ')')
		UsingSize = Label(File, text = "Usesize :  " + str(kb_) + ' ' + "KB" + ' ' + usesize)
		
		Sep__ = Separator(File, orient = HORIZONTAL)
		
		# Times
		# Create
		# Modified
		# Last Change
		ct = filectime()
		at = filemtime()
		
		ctime = Label(File, text = "Create Time :  " + ct)
		atime = Label(File, text = "Last Read Time :  " + at)
		mtime = Label(File, text = "Last Modify Time :  " + at)
		
		Sep___ = Separator(File, orient = HORIZONTAL)
		
		# Attribute
		attribut_ = "Normal"
		attribut = Label(File, text = "Attribute :  " + attribut_)
		
		# Bottom
		ok = Frame(File)
		Sep____ = Separator(ok, orient = HORIZONTAL)
		Ok = Button(ok, text = "Ok", command =  File.destroy)
		Cancel = Button(ok, text = "Cancel", command = File.destroy)
		Apply = Button(ok, text = "Apply")
		Apply["state"] = "disable"
		Ok.focus_set()
		
		Picture.pack(fill = X, side = LEFT, padx = 20, pady = 10)
		Name.pack(fill = X, side = LEFT,padx = 3)
		Names.pack(fill = X, side = TOP)
		Sep.pack(fill = X, side = TOP, padx = 20, pady = 5)
		Type.pack(fill = X, side = TOP, pady = 10)
		Openwith.pack(fill = X, side = LEFT, pady = 10)
		Change.pack(fill = Y, side = TOP)
		Opwith.pack(fill = X, side = TOP, padx = 20, pady = 10)
		Sep_.pack(fill = X, side = TOP, padx = 20, pady = 5)
		Filepath.pack(fill = X, side = TOP, padx = 20, pady = 10)
		Size.pack(fill = X, side = TOP, padx = 20, pady = 10)
		UsingSize.pack(fill = X, side = TOP, padx = 20, pady = 10)
		Sep__.pack(fill = X, side = TOP, padx = 20, pady = 5)
		ctime.pack(fill = X, side = TOP, padx = 20, pady = 10)
		atime.pack(fill = X, side = TOP, padx = 20, pady = 10)
		mtime.pack(fill = X, side = TOP, padx = 20, pady = 10)
		Sep___.pack(fill = X, side = TOP, padx = 20, pady = 5)
		attribut.pack(fill = X, side = TOP, padx = 20, pady = 10)
		Sep____.pack(fill = X, side = TOP, padx = 20)
		Apply.pack(fill = X, side = RIGHT, padx = 3)
		Cancel.pack(fill = X, side = RIGHT, padx = 3)
		Ok.pack(fill = X, side = RIGHT, padx = 3)
		#Bottom.pack(fill = X, side = BOTTOM, padx = 1)
		ok.pack(fill = X, side = BOTTOM, padx = 1, pady = 5)
		File.mainloop()

if __name__ == "__main__":
	aboutfile("function.py")
