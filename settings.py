# Imports
import json
from tkinter import *
from tkinter.messagebox import askyesno
from tkinter.ttk import *
from os import getcwd, path, chdir
from sv_ttk import set_theme
# datas
_path = getcwd() + "\\asset\\"
__path = _path + "configs\\"

# Functions
def CFGError(cfg):
	message = """
	Config file has error, this is the traceback:
	Error : %s
		ErrorFrom : %s
		ErrorType : %s
	Final:
		Raise : %d
	""" % (cfg["Error"], cfg["From"], cfg["Type"], cfg["Raise"])
	showerror("Config File Error", message = message, more = True)

def LoadCFG(filename):
	cfg_file = open(filename)
	"""
	try:
		cfg = json.load(cfg_file)
	except:
		CFGError()
	"""
	cfg = json.load(cfg_file)
	cfg_file.close()
	return cfg

def SaveCFG(cfg, filename = __path + "cfg.json"):
	cfg_file = open(filename, "w+")
	json.dump(cfg, cfg_file)
	cfg_file.close()

def init(dconfig, filename = __path + "cfg.json"):
	if not path.isfile(filename):
		cfg_file = open(filename, "w+")        
		json.dump(dconfig, cfg_file)
		CFGError()
		cfg_file.close()
		return LoadCFG(filename = filename)
	else:
		return LoadCFG(filename)
		
def _Apply():
	SaveCFG(cfg)
	config.destroy()
	
def _Okay():
	SaveCFG(cfg)
	
def _Cancel():
	if askyesno("Tip", "Do you really want to cancel this settings?"): # language replace 
		config.destroy()

def _Show():
	global show
	def changetheme():
		if cfg["theme"] != "Dark": cfg["theme"] = "Dark"
		else: cfg["theme"] = "Light"
		_themechange["text"] = "Theme : Now theme is %s" % cfg["theme"] 
		set_theme(cfg["theme"].lower())
		config.update()
	
	# data
	true = True
	false = False
	
	show = Frame(choose) # Program show, ex : theme, geometry...
	
	# theme
	theme = Frame(show)
	_themechange = Label(theme, text = "Theme : Now theme is %s" % cfg["theme"])
	themechange = Button(theme, text = "Change", command = changetheme)
	_themechange.pack(fill = X, side = TOP)
	themechange.pack(fill = Y, side = LEFT,padx = 75)
	theme.pack(fill = X,expand = False, padx = 10, pady = 10)
	
	# mica
	mica = Frame(show)
	_applymica = Label(mica, text = "Apply Mica (Only Support Window11 22H2)")
	applymica = Checkbutton(mica, style="Switch.TCheckbutton")
	applymica.state(["!alternate"])
	if cfg["mica"]: applymica.state(["!alternate", "selected"])
	if applymica.state() != ["!alternate", "selected"]:
		cfg["mica"] = true
	else:
		cfg["mica"] = false
	_applymica.pack(fill = X, side = LEFT)
	applymica.pack(fill = X, side = LEFT)
	mica.pack(fill = X, side = TOP, expand = False,padx = 10, pady = 10)

def Settings():
	global choose, cfg, config
	cfg = init("{}")
	# Window
	config = Toplevel()
	config.title("Settings")
	config.iconbitmap(_path + "Edit.ico")
	config.geometry("806x435")
	choose = Notebook(config, height = 800)
	_Show()
	editor = Frame(choose) # Program editor, ex : font, size, highlight

	#set_theme(cfg["theme"].lower())
	
	sep = Separator(config, orient = HORIZONTAL)
	configs = Frame(config)

	Apply = Button(configs, text = "Apply", command = _Apply)
	Okay = Button(configs, text = "Okay", command = _Okay)
	Cancel = Button(configs, text = "Cancel", command = _Cancel)

	Cancel.pack(fill = Y, side = RIGHT, padx = 3, pady = 2)
	Okay.pack(fill = Y, side = RIGHT, padx = 3, pady = 2)
	Apply.pack(fill = Y, side = RIGHT, padx = 3, pady = 2)

	choose.add(show, text = "Show")
	choose.add(editor, text = "Editor") 

	configs.pack(fill = X, side = BOTTOM)
	sep.pack(fill = X, side = BOTTOM)
	choose.pack(fill = X, side = TOP)

	config.protocol("WM_DELETE_WINDOW", _Cancel)

	config.mainloop()

if __name__ == "__main__":
	Settings()
