import os
import colorama

def clrscr():          # we have defined a new function to clear the screen.
	name = os.name
	if name == "nt":
		os.system('cls')
	elif name == "posix":
		os.system('clear')
		
def get_sys():                     # To find System Name.
	return os.name

def return_color(text, color = 'WHITE'):			# Defining a color function.
	disp_color = ""
	if color == 'WHITE':
		disp_color = colorama.Fore.WHITE
	elif color == 'RED':
		disp_color = colorama.Fore.RED
	elif color == 'BLUE':
		disp_color = colorama.Fore.BLUE
	elif color == 'MAGENTA':
		disp_color = colorama.Fore.MAGENTA
	elif color == 'CYAN':
		disp_color = colorama.Fore.CYAN	
	elif color == 'GREEN':
		disp_color = colorama.Fore.GREEN
	elif color == 'YELLOW':
		disp_color = colorama.Fore.YELLOW
	return (disp_color + text + colorama.Fore.WHITE)
	