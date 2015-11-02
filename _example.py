# from dragonfly.all import Grammar, CompoundRule, MappingRule, Key, Text, Integer
from dragonfly.all import *
import pythoncom, time

# Voice command rule combining spoken form and recognition processing.
class ExampleCompoundRule(CompoundRule):
    spec = "Doctor Who"
    def _process_recognition(self, node, extras):
         print "EXTERMINATE"

# Create a grammar which contains and loads the command rule.
grammar = Grammar("example grammar")

# Add the rules to the grammar.
grammar.add_rule(ExampleCompoundRule())

# Load the grammar.
grammar.load()

while True:
    pythoncom.PumpWaitingMessages()
    time.sleep(.1)
