# from dragonfly.all import Grammar, CompoundRule, MappingRule, Key, Text, Integer
from dragonfly.all import *
import pythoncom, time

# Import command modules
import _token_mapping
import _variable_format
import _main

while True:
	pythoncom.PumpWaitingMessages()
	time.sleep(.1)
