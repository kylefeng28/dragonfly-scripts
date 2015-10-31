# snake_case
def format_snake(dictation):
	""" snake <dictation> """
	words = str(dictation).split(" ")
	return "_".join(words)

# camelCase
def format_camel(dictation):
	""" camel <dictation> """
	words = str(dictation).split(" ")
	return words[0] + "".join(w.capitalize() for w in words[1:])

# PascalCase (StudleyCaps)
def format_pascal(dictation):
	""" pascal <dictation> """
	words = [ w.capitalize() for w in str(dictation).split(" ") ]
	return "".join(words)

# SCREAMING_SNAKE
def format_screaming(dictation):
	""" screaming <dictation> """
	words = [ w.upper() for w in str(dictation).split(" ") ]
	return "_".join(words)

# spine-case (lisp-case)
def format_spine(dictation):
	""" spine <dictation> """
	words = str(dictation).split(" ")
	return "-".join(words)

# Kebab-Case
def format_kebab(dictation):
	""" kebab <dictation> """
	words = [ w.capitalize() for w in str(dictation).split(" ") ]
	return "-".join(words)

# Tests
def test():
	text = "some words"
	cases = [ format_snake, format_camel, format_pascal, format_screaming, format_spine, format_kebab ]
	for case in cases:
		print(case.__name__)
		print(case(text))
		print("\n")
