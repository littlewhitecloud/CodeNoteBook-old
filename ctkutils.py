# (C)ustom (tk)inter (u)tils
# By sadjok
# Thanks for docs on web and examples on github

__author__ = "sadjok"
__name__ = "Ctkutils"
__information__ = "(C)ustom (tk)inter (u)tils"
__version__  = "1.0.0"
__help__ = ["github projects", "github forums", "web docs", "Bilibili", "CSDN", "tkinter doc", "idle", "examples"]

# Imports
import tkinter
import ctypes

# Modified Tk & Toplevel

# Error TraceBacks
class ResourceNotFoundError(Exception):
	def __init__(self, filename):
		self.error = "Resource file : \"%s\" not define" % filename
	
	def __str__(self):
		return repr(self.error)

class FunctionNotFoundError(Exception):
	def __init__(self, func):
		self.error = "Function : \"%s\" not define" % func
	
	def __str__(self):
		return repr(self.error)

class WindowEffectError(Exception):
	def __init__(self):
		self.error = "Window can't be effect"
	
	def __str__(self):
		return repr(self.error)
	
class ThemeSetError(Exception):
	def __init__(self, theme):
		self.error = "Wrong theme : %s must be \"dark\" | \"light\"" % theme 

# Modified Tk
# Add setup, darkmode, usetheme
class Tk(tkinter.Tk):
	def __init__(self, parent = None, **kwargs):
		super().__init__()
		self.sourcefile = "asset\\themes\\themes.tcl"
	
	def setup(self, title, icon, geometry, resizeable = [True, True]):
		"A setup function for self"
		try:
			self.title(title)
			try:
				self.iconbitmap(icon)
			except:
				raise ResourceNotFoundError(icon)
			try:
				self.geometry(geometry)
			except:
				raise GeometrySetError()
			self.resizable(width = resizeable[0], height = resizeable[1])
		except:
			raise WindowEffectError()
			
	def darkmode(self, sync = True):
		"Change mode to dark mode"
		try:
			if sync:
				self.usetheme(self.sourcefile, theme = "dark")
		except:
			ResourceNotFoundError(self.sourcefile)
		self.update()
		DWMWA_USE_IMMERSIVE_DARK_MODE = 20
		set_self_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
		get_parent = ctypes.windll.user32.GetParent
		hwnd = get_parent(self.winfo_id())
		rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
		value = 2
		value = ctypes.c_int(value)
		set_self_attribute(hwnd, rendering_policy, ctypes.byref(value), ctypes.sizeof(value))
		self["background"] = "black"
		self.update()
		self.update()
		
	def usetheme(self, source_file = "", theme = "light"):
		if source_file:
			self.sourcefile = sourcefile
		try:
			try:
				self.tk.call("source", f"{source_file}")
			except:
				ResourceNotFoundError(source_file)

			if theme == "light" or theme == "dark":
				self.tk.call("set_theme", f"{theme}")
			else:
				ThemeSetError(theme)
		except:
			WindowEffectError()

# Add setup, darkmode, usetheme
class Toplevel(tkinter.Toplevel):
	def __init__(self, parent = None, **kwargs):
		super().__init__()
		self.sourcefile = "asset\\themes\\themes.tcl"
	
	def setup(self, title, icon, geometry, resizeable = [False, False]):
		"A setup function for self"
		try:
			self.title(title)
			try:
				self.iconbitmap(icon)
			except:
				raise ResourceNotFoundError(icon)
			try:
				self.geometry(geometry)
			except:
				raise GeometrySetError()
			self.resizable(width = resizeable[0], height = resizeable[1])
		except:
			raise WindowEffectError()
			
	def darkmode(self, sync = True):
		"Change mode to dark mode"
		try:
			if sync:
				self.usetheme(self.sourcefile, theme = "dark")
		except:
			ResourceNotFoundError(self.sourcefile)
		self.update()
		DWMWA_USE_IMMERSIVE_DARK_MODE = 20
		set_self_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
		get_parent = ctypes.windll.user32.GetParent
		hwnd = get_parent(self.winfo_id())
		rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
		value = 2
		value = ctypes.c_int(value)
		set_self_attribute(hwnd, rendering_policy, ctypes.byref(value), ctypes.sizeof(value))
		self["background"] = "black"
		self.update()
		self.update()
		
	def usetheme(self, source_file = "", theme = "light"):
		if source_file:
			self.sourcefile = sourcefile
		try:
			try:
				self.tk.call("source", f"{source_file}")
			except:
				ResourceNotFoundError(source_file)

			if theme == "light" or theme == "dark":
				self.tk.call("set_theme", f"{theme}")
			else:
				ThemeSetError(theme)
		except:
			WindowEffectError()

# Extened
# Forgetted i'm windows 10
def blur_window_background(window:tkinter.Tk, bg_color=None, dark:bool=False):
	from tkinter import ttk
	import re
	import platform
	"Make thw window backgroud blur"
	ttkbgcolor = str(ttk.Style().lookup(".", "background"))
	match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', ttkbgcolor)
	if match:                      
		bg_color = ttkbgcolor
	else:
		if bg_color == None:
			bg_color="#fafafa"
			window.configure(bg=bg_color)
		else:
			window.configure(bg=bg_color)
	
	if int(platform.version().lstrip("10.0.")) >= 22000:
		window.wm_attributes("-transparent", bg_color)
		window.update()
		if dark:
			ApplyMica(
				HWND=ctypes.windll.user32.GetParent(window.winfo_id()), ColorMode=MICAMODE.DARK
			)
		else:
			ApplyMica(
				HWND=ctypes.windll.user32.GetParent(window.winfo_id()), ColorMode=MICAMODE.LIGHT
			)
	else:
		return "Your operating system doesnt support mica blurring!"
