from utils.tokens import tokens

from dragonfly.all import (Grammar, MappingRule,
                           Integer, Dictation)

class TokenMappingRule(MappingRule):
	mapping = tokens

	extras = [
		Integer("n", 1, 20),
		Dictation("text"),
	]
	defaults = {
		"n": 1,
	}

grammar = Grammar("Token mapping")
grammar.add_rule(TokenMappingRule())
grammar.load()
