import sys

help_message = f"USAGE:\n{sys.argv[0]} [OPTIONS]\n\n--help\t\t-h\t\tDisplays this message\n"

def help_function():
	global help_message
	print(help_message)

functions = {
	"help": help_function
}
shorthands = {
	"h": "help"
}

def error(message):
	print(f"ERROR: {message}")
	sys.exit(1)

def add_argument(argument: str, shorthand: str=None, function=help_function, description: str=None):
	global functions, shorthands, help_message
	if not argument.isalpha():
		error("Arguments can only consist of letters")
	elif len(shorthand) > 1:
		error("<shorthand> must be a single character")
	elif description == None:
		error("For usablility, make sure to include a description. If you don't want a description, set description=\"\".")
	else:
		functions[argument] = function
		shorthands[shorthand] = argument
		help_message += f"--{argument}    \t-{shorthand}\t\t{description}\n"

def handle_args():
	for i, v in enumerate(sys.argv):
		if v[0:2] == "--":
			if len(v) >= 2:
				if "=" in v:
					error("function in progress")
					for idx in range(len(v)):
						if v[idx] == "-":
							pass
						elif v[idx].isalpha() and v[idx+1] == "=":
							v[2:idx]
				else:
					functions[v[2:]]()
			else:
				error(f"Length of argument must be greater than zero")
		elif v[0] == "-":
			for value in v[1:]:
				functions[shorthands[value]]()
