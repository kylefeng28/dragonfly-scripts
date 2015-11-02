from dragonfly import (Key, Grammar, Mimic,
                       Dictation, MappingRule, Text)

class MainRule(MappingRule):
	mapping = {
		"snore": Mimic("stop", "listening"),
	}
 
grammar = Grammar("main")
grammar.add_rule(MainRule())
grammar.load()
