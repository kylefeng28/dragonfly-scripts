from dragonfly.all import Key

abbreviations = {
	"attribute" : "attr",
	"property"  : "prop",
	"string"    : "str",
}

# Adapted from Tavis Rudd's alphabet.txt and PyCon talk
# https://gist.github.com/tavisrudd/5361092
# https://www.youtube.com/watch?v:8SkdfdXWYaI
alphabet = {
	"aff"    : Key("a"),
	"brav"   : Key("b"),
	"bravo"  : Key("b"),
	"cai"    : Key("c"),
	"doy"    : Key("d"),
	"delt"   : Key("d"),
	"delta"  : Key("d"),
	"eck"    : Key("e"),
	"echo"   : Key("e"),
	"fay"    : Key("f"),
	"goff"   : Key("g"),
	"hoop"   : Key("h"),
	"ish"    : Key("i"),
	"jo"     : Key("j"),
	"keel"   : Key("k"),
	"lee"    : Key("l"),
	"lima"   : Key("l"),
	"mike"   : Key("m"),
	"noy"    : Key("n"),
	"osc"    : Key("o"),
	"osh"    : Key("o"),
	"pui"    : Key("p"),
	"pom"    : Key("p"),
	"quebec" : Key("q"),
	"queen"  : Key("q"),
	"ree"    : Key("r"),
	"soi"    : Key("s"),
	"tay"    : Key("t"),
	"uni"    : Key("u"),
	"umm"    : Key("u"),
	"van"    : Key("v"),
	"wes"    : Key("w"),
	"xanth"  : Key("x"),
	"yaa"    : Key("y"),
	"zul"    : Key("z"),
	"zulu"   : Key("z"),
}

nato_phonetic = {
	"alpha"    : Key("a"),
	"bravo"    : Key("b"),
	"charlie"  : Key("c"),
	"delta"    : Key("d"),
	"echo"     : Key("e"),
	"foxtrot"  : Key("f"),
	"golf"     : Key("g"),
	"hotel"    : Key("h"),
	"indigo"   : Key("i"),
	"juliet"   : Key("j"),
	"kilo"     : Key("k"),
	"lima"     : Key("l"),
	"mike"     : Key("m"),
	"november" : Key("n"),
	"oscar"    : Key("o"),
	"papa"     : Key("p"),
	"quebec"   : Key("q"),
	"romeo"    : Key("r"),
	"sierra"   : Key("s"),
	"tango"    : Key("t"),
	"uniform"  : Key("u"),
	"victor"   : Key("v"),
	"whiskey"  : Key("w"),
	"x-ray"    : Key("x"),
	"yankee"   : Key("y"),
	"zulu"     : Key("z"),
}

symbols = {
	"slap"   : Key("enter"),
	"laip"   : Key("lparen"),
	"raip"   : Key("rparen"),
	"lace"   : Key("lbrace"),
	"race"   : Key("rbrace"),
	"lack"   : Key("lbracket"),
	"rack"   : Key("rbracket"),
}

tokens = dict(alphabet.items() + nato_phonetic.items() + symbols.items())

__all__ = tokens
