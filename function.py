# -*- coding:utf-8 -*-

import os
import ctypes
import threading
import py_compile
import windnd
from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image as Imageopen
from PIL import ImageTk
from sv_ttk import set_theme

from tkmessagebox import *

from idlelib.colorizer import *
from idlelib.percolator import Percolator

firstpath = os.getcwd()
filepath = os.getcwd() + "\\asset\\"
os.chdir(firstpath)

from sys import version
from language import output, changelanguage
from settings import Settings, init
from ctkutils import Tk, Toplevel
from files import aboutfile

__infomation__ = """
CodeNoteBook --Sadjok
Version 3.2.6 (Python 3.9.9 Tk 8.6)
Copyright © 2019-2022 Sadjok

CodeNoteBook 3.2.6 preview.
This program made by a six grade student
Docs Github projects Tkinter Docs Python Docs Bilibili Helps
No rights reserved.

Copyright:
Free to use:
You can download,use,share to the others. 
You can't sell to the other (not in business). 

LICENSE:
Apache License, Version 2.0, http://www.apache.org/licenses/
"""
__addtext__ = """
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
	return 0

if __name__ == "__main__":
	import sys
	sys.exit(main(sys.argv))
"""
__version__ = output("version")
__name__ = "CodeNoteBook"
"""
import logging
import time
os.chdir("workspace")
os.chdir("log")

logging.basicConfig(level = logging.DEBUG,format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("DEBUG")

formatter = logging.Formatter("%(relativeCreated)d - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(str(int(time.time()))+"DEBUG.log")
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

logger.addHandler(handler)
"""
#logger.info("Start program")
#logger.info("Module : DEBUG")
#logger.info(__version__)
#logger.info("Start load functions & tools")

def aboutlicense(give = ""):
	"Show LICENSE"
	text = ""
	LICENSE = open("LICENSE","r",encoding = "utf-8")
	for line in LICENSE:
		LICENSE.read(0)
		text = text + line
	showinfo(output("license"),text,False)

def aboutupdate(give = ""):
	"Show what update"
	text = ""
	LICENSE = open("Update.txt","r",encoding = "utf-8")
	for line in LICENSE:
		LICENSE.read(0)
		text = text + line
	showinfo(output("license"),text,False)

def aboutauthor():
	"Show author"
	__author__ = "littlewhitecloud"
	showinfo(output("Author"),str(output("Author")) + " : " + __author__)
	
def aboutversion():
	"Show version"
	showinfo(output("version"),str(output("version")) + " : " + str(output("Version")))	
	
def Aboutfile(give = ""):
	filename = lde.title()
	filename = filename.split("/")[-1]
	print(filename)
	aboutfile(filename)
	try:
		aboutfile(lde.title())
	except:
		showerror("Error", "Wrong File Path")
	
def Aboutgui(give = ""):
	"Show about gui"
	def More():
		tkinterversion = TkVersion
		icon = "asset\\edit.png"
		for i in range(101):
			Pro["value"] += 1
			Abouts.update()
		Pro["value"] = 0
		About.destroy()

		# Frame
		More = Frame(Abouts)
		About_ = Frame(More)
		Show = Frame(More)
		Bottom = Frame(More)
		
		# Picture
		Icon = Label(Show,image = image)
		
		# Label
		Name = Label(Show, text = __name__, font=("@微软雅黑", 18))
		#About = Label(More, text = "")
		PythonVersion = Message(More, text = "Python Version : " + version, width = 450)
		TkinterVersion = Label(More, text = "Tkinter Version : " + str(tkinterversion))
		
		# Button
		LICENSE = Button(About_, text = "LICENSE", command = aboutlicense)
		Author = Button(About_, text = "Author", command = aboutauthor)
		Version = Button(About_, text = "Version", command = aboutversion)
		Update = Button(Bottom, text = "Update", command = aboutupdate)
		Ok = Button(Bottom, text = "Ok", command = Abouts.destroy)
		
		# Separator
		Sep = Separator(More, orient = HORIZONTAL)
		Sep_ = Separator(More, orient = HORIZONTAL)
		Sep__ = Separator(More, orient = HORIZONTAL)
		
		Icon.pack(side = LEFT, fill = BOTH, padx = 10)
		Name.pack(side = RIGHT, fill = BOTH, padx = 10)
		Show.pack(side = TOP)
		Sep.pack(side = TOP, fill = X, padx = 30)
		PythonVersion.pack(side = TOP, fill = X, padx = 30)
		TkinterVersion.pack(side = TOP, fill = X, padx = 40)
		Sep_.pack(side = TOP, fill = X, padx = 30)
		LICENSE.pack(side = LEFT, fill = X, padx = 30)
		Author.pack(side = LEFT, fill = X, padx = 30)
		Version.pack(side = LEFT, fill = X, padx = 30)
		About_.pack(side = TOP, fill = X, pady = 10)
		Ok.pack(side = RIGHT, fill = X, padx = 30)
		Update.pack(side = RIGHT, fill = X, padx = 10)
		Bottom.pack(side = BOTTOM, fill = X, padx = 5, pady = 5)
		Sep__.pack(side = BOTTOM, fill = X, padx = 30)
		More.pack(side = BOTTOM, fill = BOTH, expand = True)
		#More.pack(side = RIGHT, fill = X)
		
	icon = "asset\\edit.png"
	Abouts = Toplevel()
	Abouts.transient(lde)
	Abouts.setup("About \"CodeNoteBook\"", "asset\\edit.ico", "485x500")
	
	# Frame
	About = Frame(Abouts)
	Show = Frame(About)
	
	# Picture
	load = Imageopen.open(icon)   # open image
	image = ImageTk.PhotoImage(load)  # read opened image
	Picture = Label(Show,image = image)
	
	# Label
	Name = Label(Show, text = __name__, font=("@微软雅黑", 18))
	Texts = Label(About, text = __infomation__, font = ("Consolas", 10))
	
	# Separator
	Sep = Separator(About, orient = HORIZONTAL)
	
	# Progressbar
	Pro = Progressbar(Abouts, orient = HORIZONTAL)
	Pro.pack(side = TOP, fill = X, padx = 0)
	
	# Button
	More = Button(About, text = "More About...", command = More)
	Ok = Button(About, text = "Ok", command = Abouts.destroy)
	
	Picture.pack(side = LEFT, fill = BOTH, padx = 10)
	Name.pack(side = RIGHT, fill = BOTH, padx = 10)
	Show.pack(side = TOP)
	Sep.pack(side = TOP, fill = X, padx = 30)
	Texts.pack(side = TOP, fill = BOTH, padx = 30)
	Sep = Separator(About, orient = HORIZONTAL)
	Sep.pack(side = TOP, fill = X, padx = 30)
	Ok.pack(side = RIGHT, fill = X, padx = 30)
	More.pack(side = RIGHT, fill = X)
	About.pack(side = BOTTOM, fill = BOTH, expand = True)
	Abouts.mainloop()

flag = True
def autoindent(event):
	"If flag then indent with types"
	global flag
	tab = "	"
	widget = event.widget
	line = widget.get("insert linestart", "insert lineend")
	if "return" in line:
		widget.insert(INSERT,"\n")
	else:
		if flag:
			match = re.match(r'^(\s+)', line)
			current_indent = len(match.group(0)) if match else 0
			new_indent = current_indent + 1
			widget.insert(INSERT,event.char)
			widget.insert(INSERT,"\n" + tab*new_indent)
		else:
			match = re.match(r'^(\s+)', line)
			current_indent = len(match.group(0)) if match else 0
			if current_indent:
				widget.insert(INSERT,event.char)
				widget.insert(INSERT,"\n" + tab*current_indent)
			else:
				widget.insert(INSERT,"\n")
		flag = False
	text.focus_set()
	return "break"

def click(active):
	"Post editmenu"
	editmenu.post(active.x_root, active.y_root)

def undo():
	"Undo"
	text["undo"] = True
	try:
		text.edit_undo()
	except:
		pass
	
def copy():
	"Copy"
	try:
		text.clipboard_clear()
		text.clipboard_append(text.selection_get())
	except:
		pass

def cut():
	"Cut"
	copy()
	try:
		text.delete(SEL_FIRST, SEL_LAST)
	except:
		pass
		
def createcompilefile(filepath = ""):
	"Complie files and output"
	try:
		py_compile.compile(filepath)
		initpath(firstpath)
		showinfo("CodeNoteBook",output("compliefile2") + " " + filepath)
	except:
		initpath(firstpath)
		showerror("CodeNoteBook",output("complieerror") + " " + filepath)

def changefontandsize(give = ""):
	"Change text's font and size"
	fonts = Toplevel()
	fonts.transient(lde)
	fonts.title("Font")
	fonts.geometry("500x50")
	fonts.iconbitmap(filepath + "fonts.ico")
	fonts.resizable(width = False, height = False)
	
	font_tuple = families()
	font_family = StringVar()
	
	font_box = Combobox(fonts, width=30,textvariable=font_family,state='readonly')
	font_box['values'] = font_tuple
	font_box.current(font_tuple.index('Arial'))
	font_box.pack(fill = "x",side = "left",padx = 3)
	
	def fontchanger():
		"Change font"
		global current_font_family
		global current_font_size
		
		current_font_family=font_family.get()
		current_font_size=size_var.get()
		text.configure(font=(current_font_family,current_font_size))
		fonts.destroy()
		
	size_var = IntVar()
	font_size =Combobox(fonts, width=15, textvariable=size_var, state='readonly')
	font_size['values'] = tuple(range(8,81))
	font_size.current(0)
	font_size.pack(fill = "x",side = "left",padx = 3)

	changefont = Button(fonts,text = "Apply",command = fontchanger)
	changefont.pack(fill = "x",side = "right",padx = 5)
	
	fonts.mainloop()
	
def changelanguages(give = ""):
	"Change CodeNoteBook's language"
	changelanguage()
	showinfo("CodeNoteBook","You have to restart CodeNoteBook")
	
def Clear_menu():
	"Clear view menu"
	filemenu.delete(4,6)
	viewfilemenu = Menu(menubar,tearoff=0)
	filemenu.add_cascade(label=output("viewfile"),menu=viewfilemenu,command=open_file())
	viewfilemenu.add_command(label=output("clear"),command=Clear_menu)
	filemenu.add_separator()
	filemenu.add_command(label=output("quit"), command=ldequit)

def checkindent(event):
	"If : in with the right word then flag = True "
	global flag
	flag = False
	words = ['class', 'def', 'for', 'while', 'if', 'elif', 'else']
	widget = event.widget
	line = widget.get("insert linestart", "insert lineend")
	value = 0
	for i in words:
		if value > len(words):
			widget.insert(INSERT,event.char)
		if words[value] not in line:
			value += 1
		else:
			flag = True
			break	
	widget.insert(INSERT,event.char)
	return "break"


def countfuncandclassandimport(give=""):
	"Count def and class and import then Update"
	total = text.get("0.0","end")
	define = total.count("def ")
	classes = total.count("class ")
	froms = total.count("from ")
	imports = total.count("import ")
	statusbar.set_label("import","Imp: %d" % (froms + imports))
	statusbar.set_label("func","Func: %d" % define)
	statusbar.set_label("class","Cls: %d" % classes)
	
def dragged_files(file):
	"Read dragged file to text"
	try:
		file = "\n".join((item.decode("utf-8") for item in file))
	except:
		file = "\n".join((item.decode("gbk") for item in file))
	else:
		open_file(file,False)

def exitsave():
	"If exit and file not save then show do you want to save"
	if lde.title() == "CodeNoteBook" or output("newfile"):
		ldequit()
	else:
		flag = askokcancel("CodeNoteBook",output("savemsg"))
		if flag == True:
			save_file()
			ldequit()
		else:
			ldequit()

def find(give = ""):
	"Find string in text if created text"
	def close():
		"Close window"
		text.tag_remove('match', '1.0',END)
		Find.destroy()
	
	def finds():
		"Find function"
		word = find_input.get()
		text.tag_remove('match', '1.0',END)
		matches = 0
		if word:
			start_pos = '1.0'
			while True:
				start_pos = text.search(word, start_pos, stopindex=END)
				if not start_pos:
					break 
				end_pos = f'{start_pos}+{len(word)}c'
				text.tag_add('match', start_pos, end_pos)
				matches += 1
				start_pos = end_pos
				text.tag_config('match', foreground='yellow', background='orange')
		
	def replace():
		word = find_input.get()
		replace_text = replace_input.get()
		content = text.get(1.0, END)
		new_content = content.replace(word,replace_text)
		text.delete(1.0, END)
		text.insert(1.0, new_content)

	Find = Toplevel()
	Find.iconbitmap(filepath + "find.ico")
	Find.transient(lde)
	Find.geometry('450x155')
	Find.title('Find')
	Find.resizable(False,False)

	find_frame = LabelFrame(Find, text='Find/Replace')
	find_frame.pack(fill = "x",side = "top",padx = 10)

	text_find_label = Label(find_frame, text='Find : ')
	text_replace_label = Label(find_frame, text= 'Replace :')
	
	find_input = Entry(find_frame, width=30)
	replace_input = Entry(find_frame, width=30)

	find_button = Button(find_frame, text='Find', command=finds)
	replace_button = Button(find_frame, text= 'Replace', command=replace)
	exit_button = Button(find_frame, text = "Exit", command=close)

	text_find_label.pack(fill = "x",side = "top",padx = 5)
	find_input.pack(fill = "x",side = "top",padx = 5)
	text_replace_label.pack(fill = "x",side = "top",padx = 5)
	replace_input.pack(fill = "x",side = "top",padx = 5)

	find_button.pack(fill = "x",side = "left",padx = 7)
	replace_button.pack(fill = "x",side = "left",padx = 10)
	exit_button.pack(fill = "x",side = "right",padx = 10,pady = 2)
	
	Find.mainloop()

def getmouselines(give=""):
	"Use mouse to get how many lines in text"
	line, column = map(str,str(text.index("insert")).split("."))
	statusbar.set_label("column", "Col: %s" % column)
	statusbar.set_label("line", "Ln: %s" % line)

def initpath(path):
	"Change path...?"
	os.chdir(path)

def ldequit():
	"Quit lde"
	lde.destroy()
	exit(0)

def modulehelps():
	"Show module helps"
	def Get_helps():
		"Use function to get helps"
		getmodulename = modulename.get()
		Get_info(getmodulename)
		Get_help(getmodulename)
			
	helps = Toplevel()
	modulename = Entry(helps)
	finishinput = Button(helps,text = "Finish",command = Get_helps)
	modulename.pack(fill = "x",side = "left")
	finishinput.pack(fill = "x",side = "right")
	helps.mainloop()

def new_file(give = ""):
	"Create a new file in text"
	text.delete("0.0","end")
	text.pack(fill = BOTH, expand = True)
	statusbar.set_label("type","New" + " file",side = "left")
	lde.title(output("newfile"))
	text.insert(INSERT,__addtext__)
	#text.unbind_class("create","<Button-1>")

def open_file(give = "",status = True):
	"Open file and read it to text"
	"Status : Show the dialog or don't"
	if status:
		text.delete("0.0","end")
		Foldername = askopenfilename(title = output("openfile"), filetypes=[("Python Files", "*.py"),("Python Files (no console)", "*.pyw"),("All Files", "*")])
		try:
			file = open(Foldername,"r",1024,encoding = "utf-8")
			for line in file:
				file.read(0)
				text.insert(INSERT,line)
				lde.update()
		except:
			try:
				file = open(Foldername,"r",1024,encoding = "gbk")
				for line in file.readlines():
					text.insert(INSERT,line)
			except:
				if Foldername == "":
					pass
				else:
					initpath(firstpath)
					showerror("CodeNoteBook",output("saveerror") + " " + Foldername)

		else:
			viewfilemenu.add_command(label = Foldername)# ,command = open_file(Foldername)
			text.pack(fill = BOTH, expand = True)
			lde.title(Foldername)
			Foldername = Foldername.split(".")
			Foldername = Foldername[-1]
			statusbar.set_label("type",Foldername + " file",side = "left")
	else:
		text.delete("0.0","end")
		try:
			file = open(give,"r",encoding = "utf-8")
			for line in file.readlines():
				text.insert(INSERT,line)
		except:
			try:
				file = open(give,"r",encoding = "gbk")
				for line in file.readlines():
					text.insert(INSERT,line)			
			except:
				if give == "":
					pass
				else:
					initpath(firstpath)
					showerror("CodeNoteBook",output("saveerror") + " " + give)
		else:
			viewfilemenu.add_command(label = give) #,command = open_file(give)
			text.pack(fill = BOTH, expand = True)
			lde.title(give)
			give = give.split(".")
			give = give[-1]
			statusbar.set_label("type",give + "file",side = "left")
			
def openpythonhelp():
	"Open python's help"
	docpath = os.getcwd() + "\\asset\\"
	os.system("hh " + docpath + "PythonHelpDoc.chm")

def openldehelp():
	"Open CodeNoteBook's help"
	docpath = os.getcwd() + "\\asset\\"
	os.system("hh " + docpath + "CodeNoteBook.chm")

def paste():
	"Paste"
	try:
		text.insert(SEL_FIRST, text.clipboard_get())
		text.delete(SEL_FIRST, SEL_LAST)
		return
	except:
		pass
	text.insert(INSERT, text.clipboard_get())
	
def quitFullScreen():
	"Quit Full Screen"
	lde.attributes("-fullscreen",False)

def refresh(give = ""):
	"Update GUI"
	lde.update()
	
def redo():
	"Redo"
	text["undo"] = True
	try:
		text.edit_redo()
	except:
		pass	

def runpythonfile():
	"Run python files"
	filename = lde.title()
	if filename == "CodeNoteBook":
		initpath(firstpath)
		showinfo("CodeNoteBook",output("savemsg"))
		save_file()
		runpythonfile()
	else:
		operation = "start python %s" % filename
		system(operation)
		
def save_file(give = ""):
	"""
	"Save file"
	if lde.title() != "CodeNoteBook" and lde.title() != output("newfile") == False:
		try:
			filename = lde.title()
			if filename.endwith()
			
			with open(lde.title() + ".py","w",encoding = "utf-8") as savefile:
				savefile.write(text.get("0.0","end"))
				lde.title(lde.title())
		except:
			if Foldername == "" or " " or None:
				pass
			else:
				showerror("CodeNoteBook",output("saveerror") + " " + lde.title())
	else:
		Foldername = filedialog.asksaveasfilename(title=output("savetitle"), filetypes=[(output("filetype"), "*.py"),("Python Files (no console)", "*.pyw"),("All Files", "*")])
		try:
			with open(Foldername + ".py","w",encoding = "utf-8") as savefile:
				savefile.write(text.get("0.0","end"))
				lde.title(Foldername)
		except:
			if Foldername == "" or " " or None:
				pass
			else:
				showerror("CodeNoteBook",output("saveerror") + " " + lde.title())
	"""
	if lde.title() == "CodeNoteBook" or lde.title() == output("newfile"):
		save_as_file()
	else:
		titles = titles = lde.title()
		if '*' in titles:
			titles = titles.split('*')[-1]
			lde.title(titles)
		filename = titles
		if titles.endswith(".py"):
			pass
		else:
			filename = filename + ".py"	
		
		with open(filename,"w",encoding = "utf-8") as savefile:
				savefile.write(text.get("0.0","end"))
				lde.title(filename)
		
def save_as_file(give = ""):
	"Save file as a new path"
	Foldername = asksaveasfilename(title=output("saveas"), filetypes=[("Python Files", "*.py"),("Python Files (no console)", "*.pyw"),("All Files", "*")])
	try:
		with open(Foldername,"w",encoding = "utf-8") as saveasfile:
			saveasfile.write(text.get("0.0","end"))
			lde.title(Foldername)
	except:
		if Foldername == "" or " " or None:
			pass
		else:
			initpath(firstpath)
			showerror("CodeNoteBook",output("saveerror") + " " + lde.title())

def show_fast_bind(give = ""):
	"Show fast binds"
	binds = "SaveFile:Ctrl-S" + "\n" + "OpenFile:Ctrl-O" + "\n" + "NewFile:Ctrl-N" + "\n" + "Refresh:Ctrl-F" + "\n" + "Quit:Ctrl:Q" + "\n" + "RunFile:<F5>" + "\n" + "ShowHelp:<F1>" + "\n" + "Full/UnfullScreen:<F11>"  + "\n" + "ShowBinds:Ctrl-B" + "\n" + "ShowAboutlde:Ctrl-H" + "\n" + "ShowAboutLICENSE:Ctrl-l" + "\n" + "ChangeFont&Size:Ctrl-Shift-O" + "\n" + "Changelanguage:Ctrl-Shift-L" + "\n" + "FindString:Ctrl-Shift-C"
	initpath(firstpath)
	showinfo("Binds",binds)

def showpythonshell():
	"Run python if have"
	try:
		os.system("start python")
	except:
		showerror("CodeNoteBook","Didn't find Python on this computer")

def showconsole():
	os.system("start python console.py")

def _thread_it(func, *args):
	"Create a function with thread"
	thread = threading.Thread(target=func, args=args)
	thread.setDaemon(True)
	thread.start()
	
def toggleFullScreen():
	"Use Full Screen"
	lde.attributes("-fullscreen",True)

def toolbar(give = ""):
	"Show Toolbar"
	toolbarwindow = Toplevel()
	toolbarwindow.iconbitmap(filepath + "Edit.ico")
	toolbarwindow.resizable(width = True, height = True)
	toolbar = Frame(toolbarwindow,relief="sunken",background="white")

	newimg = Imageopen.open(filepath + "New.png")
	enewimg = ImageTk.PhotoImage(newimg)
	newButton = Button(toolbar, image=enewimg,text = "New",width=50,height=50,command=new_file,relief="flat")
	newButton.image = enewimg
	newButton.pack(side=LEFT, padx=2, pady=2)

	openimg = Imageopen.open(filepath + "Open.png")
	eopenimg = ImageTk.PhotoImage(openimg)
	openButton = Button(toolbar, image=eopenimg,width=50,height=50,command=open_file,relief="flat")
	openButton.image = eopenimg
	openButton.pack(side=LEFT, padx=2, pady=2)

	saveimg = Imageopen.open(filepath + "Save.png")
	esaveimg = ImageTk.PhotoImage(saveimg)
	saveButton = Button(toolbar, image=esaveimg,width=50,height=50,command=save_file,relief="flat")
	saveButton.image = esaveimg
	saveButton.pack(side=LEFT, padx=2, pady=2)

	saveasimg = Imageopen.open(filepath + "Saveas.png")
	esaveasimg = ImageTk.PhotoImage(saveasimg)
	saveasButton = Button(toolbar, image=esaveasimg,width=50,height=50,command=save_as_file,relief="flat")
	saveasButton.image = esaveasimg
	saveasButton.pack(side=LEFT, padx=2, pady=2)

	complieimg = Imageopen.open(filepath + "Complie.png")
	ecomplieimg = ImageTk.PhotoImage(complieimg)
	complieButton = Button(toolbar, image=ecomplieimg,width=50,height=50,command=tocompilefile,relief="flat")
	complieButton.image = ecomplieimg
	complieButton.pack(side=LEFT, padx=2, pady=2)

	runimg = Imageopen.open(filepath + "Run.png")
	erunimg = ImageTk.PhotoImage(runimg)
	runButton = Button(toolbar, image=erunimg,width=50,height=50,command=runpythonfile,relief="flat")
	runButton.image = erunimg
	runButton.pack(side=LEFT, padx=2, pady=2)

	exitimg = Imageopen.open(filepath + "Exit.png")
	eexitimg = ImageTk.PhotoImage(exitimg)
	exitButton = Button(toolbar, image=eexitimg,width=50,height=50,command=ldequit,relief="flat")
	exitButton.image = eexitimg
	
	exitButton.pack(side=LEFT, padx=2, pady=2)

	toolbar.pack(side=TOP, fill=X)
	"""
	textbar = Frame(toolbarwindow,relief="sunken",background="white")
	newLabel = Label(textbar, text = "New",bg = "white")
	newLabel.pack(side=LEFT, padx=2, pady=2)

	openLabel = Label(textbar, text = "Open",bg = "white")
	openLabel.pack(side=LEFT, padx=2, pady=2)

	saveLabel = Label(textbar, text = "Save",bg = "white")
	saveLabel.pack(side=LEFT, padx=2, pady=2)

	saveasnewLabel = Label(textbar, text = "Save as",bg = "white")
	saveasnewLabel.pack(side=LEFT, padx=2, pady=2)

	complieLabel = Label(textbar, text = "Complie",bg = "white")
	complieLabel.pack(side=LEFT, padx=2, pady=2)

	runLabel = Label(textbar, text = "Run",bg = "white")
	runLabel.pack(side=LEFT, padx=2, pady=2)

	exitLabel = Label(textbar, text = "Exit",bg = "white")
	exitLabel.pack(side=LEFT, padx=2, pady=2)
	
	textbar.pack(side=TOP, fill=X)
	"""
	toolbarwindow.mainloop()
	
def tocompilefile():
	"Call the complie file function"
	filepath = lde.title()
	if filepath == "CodeNoteBook":
		initpath(firstpath)
		showinfo("CodeNoteBook",output("savemsg"))
		save_file()
	else:
		createcompilefile(filepath)

def usingrun(give = ""):
	"Run file with thread"
	_thread_it(runpythonfile)

def usingpythonhelp(give = ""):
	"Call openpythonhelp function"
	showerror("Sorry", "Sorry we can not open python's doc because program has a bug")
	#_thread_it(openpythonhelp)

def usingldehelp():
	"Call openldehelp function"
	_thread_it(openldehelp)

def finishshow():
	"Finish show logo"
	Logo.destroy()
	
current_font_family = "Cascadia Mono"
current_font_size =  9
def ctrlwheel(event):
	global current_font_family, current_font_size
	if event.delta > 1:
		text.configure(font = (current_font_family,current_font_size + 1))
		current_font_size += 1
	else:
		text.configure(font = (current_font_family,current_font_size - 1))
		current_font_size -= 1
#logger.info("Finished load function") # debug
#logger.info("Start creating window") # debug

cfg = init("")

if cfg["theme"] == "Dark":
	bg = "black"
	gb = "white"
else:
	bg = "white"
	gb = "black"
"""
Logo = Tk()
Logo.setup("CodeNoteBook", filepath + "Edit.ico", "1030x570", [True, True])
ShowFrame = Frame(Logo)
Logo_ = Imageopen.open(filepath + "present.png")
Logo_ = ImageTk.PhotoImage(Logo_)
ShowLogo = Label(ShowFrame, image = Logo_)
Name_ = Label(ShowFrame, text = "CodeNoteBook",font=("Cascadia Mono", 12, "italic"))
ShowLogo.pack()
Name_.pack()
ShowFrame.pack(anchor = "center")
Name_.pack(anchor = "center")
Logo.attributes("-disabled",True)
Logo.after(10000, finishshow)
Logo.mainloop()
"""

lde = Tk()
lde.setup("CodeNoteBook", filepath + "Edit.ico", "1030x570", [True, True])
"""
def _include():
	lde_back=ctypes.windll.user32.GetParent(lde.winfo_id())
	include_back=ctypes.windll.user32.GetParent(include.winfo_id())
	ctypes.windll.user32.SetParent(lde_back,include.winfo_id())
"""   
#include = Tk()
#include.setup("Include", filepath + "Edit.ico", "1030x570", [True, True])
#include.title('嵌套子窗口测试')


if cfg["theme"] == "Dark":
	lde.darkmode()

#hwnd = windll.user32.FindWindowW(c_char_p(None), "CodeNoteBook")
"""
GWL_STYLE = -16
GWL_EXSTYLE = -20
old1=windll.user32.GetWindowLongA(hwnd,GWL_STYLE)
old2=windll.user32.GetWindowLongA(hwnd,GWL_EXSTYLE)

WS_BORDER = 0x800000
WS_CAPTION = 0xC00000 # WS_BORDER Or WS_DLGFRAME
WS_CHILD = 0x40000000
WS_CLIPCHILDREN = 0x2000000
WS_CLIPSIBLINGS = 0x4000000
WS_POPUP = 0x80000000
WS_DLGFRAME = 0x400000
WS_DISABLED = 0x8000000
WS_OVERLAPPEDWINDOW = 0xcf0000
WS_THICKFRAME = 0x40000
WS_VISIBLE = 0x10000000

WS_EX_APPWINDOW = 0x40000
WS_EX_DLGMODALFRAME = 0x1
WS_EX_ACCEPTFILES = 0x10
WS_EX_CLIENTEDGE= 0x200
WS_EX_TOOLWINDOW = 0x80
WS_EX_WINDOWEDGE = 0x100

#windll.user32.SetWindowLongA(hwnd, GWL_STYLE, old1)
#windll.user32.SetWindowLongA(hwnd, GWL_EXSTYLE, old2)
#windll.user32.SetWindowLongA(hwnd,GWL_STYLE,WS_VISIBLE+WS_CLIPSIBLINGS+WS_CLIPCHILDREN)
#windll.user32.SetWindowLongA(hwnd,GWL_STYLE,WS_VISIBLE+WS_CLIPSIBLINGS+WS_CLIPCHILDREN + WS_THICKFRAME + WS_OVERLAPPEDWINDOW)
#windll.user32.SetWindowLongA(hwnd, GWL_EXSTYLE, WS_EX_CLIENTEDGE)
#windll.user32.SetWindowLongA(hwnd,GWL_EXSTYLE, WS_EX_TOOLWINDOW)
"""
#lde.attributes('-alpha',0.9875)

#logger.info("Adding window settings") # debug

# menu {
#logger.info("Loading menu & functions") # debug

menubar = Menu(lde)
filemenu = Menu(menubar, tearoff=0, activebackground = bg, activeforeground = gb)
viewfilemenu = Menu(menubar,tearoff=0, activebackground = bg, activeforeground = gb)
filemenu.add_command(label= "AboutFile", command=Aboutfile)
filemenu.add_command(label= output("newfile"), command=new_file)
filemenu.add_command(label= output("open"), command=open_file)
filemenu.add_command(label= output("save"), command=save_file)
filemenu.add_command(label= output("saveas"), command=save_as_file)
filemenu.add_cascade(label= output("viewfile"),menu=viewfilemenu)
viewfilemenu.add_command(label=output("clear"),command=Clear_menu)
filemenu.add_separator()
filemenu.add_command(label=output("quit"), command=ldequit)
menubar.add_cascade(label=output("filemenu"), menu=filemenu,underline = 0,background = "black")

editmenu = Menu(menubar, tearoff=0, activebackground = bg, activeforeground = gb)
editmenu_edit = Menu(editmenu, tearoff=0, activebackground = bg, activeforeground = gb)
editmenu.add_command(label=output("refresh"), command=refresh)
editmenu.add_command(label=output("find"), command=find)
editmenu_edit.add_command(label=output("undo"),command=undo)
editmenu_edit.add_command(label="redo",command=redo)
editmenu_edit.add_command(label=output("cut"),command=cut)
editmenu_edit.add_command(label=output("copy"),command=copy)
editmenu_edit.add_command(label=output("paste"),command=paste)
editmenu.add_cascade(label=output("edit"),menu=editmenu_edit)
menubar.add_cascade(label=output("editmenu"), menu=editmenu,underline = 0)

runmenu = Menu(menubar, tearoff=0, activebackground = bg, activeforeground = gb)
runmenu.add_command(label=output("run"),command=runpythonfile)
runmenu.add_command(label=output("compliefile"),command=tocompilefile)
shellmenu = Menu(menubar, tearoff=0, activebackground = bg, activeforeground = gb)
shellmenu.add_command(label=output("pythonshellconsole"),command=showpythonshell)
shellmenu.add_command(label="Console", command = showconsole)
#shellmenu.add_command(label=output("pythonshellgui"),command=pass)
runmenu.add_cascade(label=output("shell"),menu=shellmenu)
menubar.add_cascade(label=output("runmenu"), menu=runmenu,underline = 0)

optionmenu = Menu(menubar, tearoff=0, activebackground = bg, activeforeground = gb)
optionmenu.add_command(label=output("font"),command=changefontandsize)
optionmenu.add_command(label=output("language"),command=changelanguages)
menubar.add_cascade(label=output("option"),menu=optionmenu,underline = 0)

helpmenu = Menu(menubar, tearoff=0, activebackground = bg, activeforeground = gb)
helpmenu.add_command(label=output("pythonhelp"),command=usingpythonhelp)
helpmenu.add_command(label=output("ldehelp"),command=usingldehelp)
helpmenu.add_command(label=output("help"),command=Aboutgui)
helpmenu.add_command(label=output("bind"),command=show_fast_bind)
menubar.add_cascade(label=output("helpmenu"), menu=helpmenu,underline = 0)

settingsmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Settings", command = Settings, underline = 0)
lde.config(menu = menubar)

#logger.info("Created frame,text,menu,label,statusbar,scrollbar") # debug

#logger.info("Creating frame & tools") # debug
	
textframe = Frame(lde)
scrollbarx = Scrollbar(textframe,)
scrollbary = Scrollbar(textframe, orient = HORIZONTAL)

text = Text(textframe,yscrollcommand = scrollbarx.set,xscrollcommand = scrollbary.set,wrap = "none",highlightbackground = bg,insertborderwidth = 0,relief = "flat",selectbackground = "grey",undo = True)
text.focus_set()
textchanged = IntVar(value = 0)
text.config(tabs=("1c","2c"))
text.configure(font=("Cascadia Code", 9, "normal"))

color_config(text)
Percolator = Percolator(text)
ColorDelegator = ColorDelegator()
Percolator.insertfilter(ColorDelegator)

scrollbarx.config(command = text.yview)
scrollbary.config(command = text.xview)
scrollbarx.pack(side = RIGHT, fill = Y)
scrollbary.pack(side = BOTTOM, fill = X)
textframe.pack(fill = BOTH, expand = True)

text.bind("<Control-MouseWheel>", ctrlwheel)

def autoaddk(event):
	text.insert(INSERT, "{")
	text.insert(INSERT, "}")
	
text.bind("<KeyPress-{>", autoaddk)
#logger.info("Load statusbar") # debug

class StatusBar(Frame):
	def __init__(self, master, **kw):
		Frame.__init__(self, master, **kw)
		self.labels = {}

	def set_label(self, name, text="", side="right", width=0):
		if name not in self.labels:
			label = Label(self, borderwidth=0, anchor="w")
			label.pack(side=side, pady=0, padx=4)
			self.labels[name] = label
		else:
			label = self.labels[name]
		if width != 0:
			label.config(width=width)
		label.config(text=text)

statusframe = Frame(lde)
Sizegrip(statusframe).pack(side = RIGHT)
statusbar = StatusBar(statusframe)

statusbar.set_label("type", "None",side = "left")
statusbar.set_label("column", "Col: ")
statusbar.set_label("line", "Ln: ")
statusbar.set_label("Split","|")
statusbar.set_label("import","Imp:")
statusbar.set_label("func","Func: ")
statusbar.set_label("class","Cls: ")

statusbar.pack(fill = X)
statusframe.pack(fill = X)

def changetitle(give = ""): 
	if '*' in lde.title():
		pass
	else:
		newtitle = "*" + lde.title()
		lde.title(newtitle)

text.bind(":", checkindent)
text.bind("<Return>",autoindent)
text.bind("<Key>", changetitle)	

bindtags = list(text.bindtags())
bindtags.insert(2,"get")
text.bindtags(tuple(bindtags))
text.bind_class("get","<Key>",getmouselines)

bindtags = list(text.bindtags())
bindtags.insert(1,"counts")
text.bindtags(tuple(bindtags))
text.bind_class("counts","<Key>",countfuncandclassandimport)

def show():
	lde.attributes("-disabled",True)
	progressbar["maximum"] = 100
	progressbar["value"] = 0
	for i in range(100):
		if progressbar["value"] == 20:
			statustext["text"] = "Loading tools & plugins"
		elif progressbar["value"] == 35:
			statustext["text"] = "Finish loading"
		elif progressbar["value"] == 50:
			statustext["text"] = "Loading settings"
		elif progressbar["value"] == 75:
			statustext["text"] = "Loading languages"
		elif progressbar["value"] == 85:
			statustext["text"] = "Using loaded packages"
		elif progressbar["value"] == 90:
			statustext["text"] = "Saving Log"
		elif progressbar["value"] == 99:
			statustext["text"] = "Ready"

		progressbar["value"] += 1
		lde.update()
	
	lde.attributes("-disabled",False)
	progressbar["value"] = 0

progressbar = Progressbar(statusbar)
separators = Label(statusbar,text = "|")
statustext = Label(statusbar,text = "Loading")
separators.pack(side = LEFT,padx = 10)
progressbar.pack(side = LEFT)
statustext.pack(side = LEFT,padx = 5)


#logger.info("Add keys") # debug

lde.bind("<Button-1>",getmouselines)
lde.bind("<Control-KeyPress-s>",save_file)
lde.bind("<Control-Shift-KeyPress-S>",save_as_file)
lde.bind("<Control-KeyPress-o>",open_file)
lde.bind("<Control-KeyPress-n>",new_file)
lde.bind("<Control-KeyPress-f>", Aboutfile)
lde.bind("<Control-Shift-KeyPress-C>",find)
lde.bind("<Control-Shift-KeyPress-L>",changelanguages)
lde.bind("<Control-Shift-KeyPress-O>",changefontandsize)
lde.bind("<Control-KeyPress-q>",ldequit)
lde.bind("<Control-KeyPress-l>",aboutlicense)
lde.bind("<Control-KeyPress-h>",Aboutgui)
lde.bind("<Control-C>",copy)
lde.bind("<Control-V>",paste)
lde.bind("<Control-X>",cut)
lde.bind("<Control-Z>",undo)
lde.bind("<Control-Y>",redo)
lde.bind("<Button-3>",click)
lde.bind("<F5>",usingrun)
lde.bind("<F6>",refresh)
lde.bind("<F1>",usingpythonhelp)
lde.bind("<Control-KeyPress-b>",show_fast_bind)
lde.bind("<F11>",
        lambda event: lde.attributes("-fullscreen",
				not lde.attributes("-fullscreen")))

# }

#create_tooltip()

#logger.info("Set drop & settings") # debug
"""
logger.info("Back to the first path") # debug
logger.info("Save settings & functions") # debug
logger.info("All things saved")  # debug
logger.info("Finish loading") # debug
"""

windnd.hook_dropfiles(lde,func = dragged_files)
myappid = "CodeNoteBook"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#blur_window_background(lde, dark=False)
os.chdir(firstpath)
#show()
"""
def blur():
	from ctypes import windll
	from windowblur import blur
	hwnd = windll.user32.GetForegroundWindow()
	blur(hwnd = hwnd, Acrylic = True, AccentState = 3) #Custom AccentState
lde.bind("<F4>", blur)
"""
#include.after(10, _include)
#include.mainloop()
set_theme(cfg["theme"].lower())
lde.protocol("WM_DELETE_WINDOW", exitsave)
lde.mainloop()



