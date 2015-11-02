# Adapted from https://code.google.com/p/dragonfly-modules/source/browse/trunk/command-modules/_variable_format.py?r=45

from dragonfly.all import (Grammar, CompoundRule,
                           Dictation, Choice, Key, Text)

from utils import formatting

(normal, no_space) = range(2)

class HandlerBase(object):

	spec = None
	spacing = no_space

	def handle_dictation(self, dictation):
		if self.spacing == normal:
			engine.mimic(["test"])
			Key("backspace:4").execute()
		formatted = self.format_dictation(dictation)
		Text(formatted).execute()

	def format_dictation(self, dictation):
		pass


class UnderscoreHandler(HandlerBase):
	spec = "snake"
	def format_dictation(self, dictation):
		return formatting.format_snake(dictation)

class CamelCaseHandler(HandlerBase):
	spec = "camel"
	def format_dictation(self, dictation):
		return formatting.format_camel(dictation)

class StudleyHandler(HandlerBase):
	spec = "studley"
	def format_dictation(self, dictation):
		return formatting.format_pascal(dictation)

class ScreamingSnakeHandler(HandlerBase):
	spec = "screaming"
	def format_dictation(self, dictation):
		return formatting.format_screaming(dictation)

class SpineCaseHandler(HandlerBase):
	spec = "spine"
	def format_dictation(self, dictation):
		return formatting.format_spine(dictation)

class KebabCaseHandler(HandlerBase):
	spec = "kebab"
	def format_dictation(self, dictation):
		return formatting.format_kebab(dictation)

#---------------------------------------------------------------------------
# Create the main command rule.

class CommandRule(CompoundRule):

	handlers = {}
	for value in globals().values():
		try:
			if issubclass(value, HandlerBase) and value is not HandlerBase:
				instance = value()
				handlers[instance.spec] = instance.handle_dictation
		except TypeError:
			continue

	spec	 = "<handler> <dictation>"
	extras   = [
				Choice("handler", handlers),
				Dictation("dictation"),
			   ]

	def _process_recognition(self, node, extras):
		handler = extras["handler"]
		dictation = extras["dictation"]
		handler(dictation)


#---------------------------------------------------------------------------

grammar = Grammar("Variable format")
grammar.add_rule(CommandRule())
grammar.load()
