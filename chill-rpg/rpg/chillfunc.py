import os
import sys
import time
from clint.textui import colored

def clear():
	if os.name == 'nt':
		_ = os.system('cls')
	
	else:
		_ = os.system('clear')
		
