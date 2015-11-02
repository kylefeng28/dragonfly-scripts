from formatting import *

def test_formatting():
	text = "some words"
	cases = [ format_snake, format_camel, format_pascal, format_screaming, format_spine, format_kebab ]
	for case in cases:
		print(case.__name__)
		print(case(text))
		print("\n")
