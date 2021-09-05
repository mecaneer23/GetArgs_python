import sys

help_message = f"USAGE:\n{sys.argv[0]} [OPTIONS]\n\n"

def help_function():
	global help_message
	print(help_message)

shorthands = {}
info = {}

def error(message):
	print(f"ERROR: {message}")
	sys.exit(1)

def add_argument(argument: str, shorthand: str=None, function=help_function, description: str=None):
	global info, shorthands
	if not argument.isalpha():
		error("Arguments can only consist of letters")
	elif len(shorthand) > 1:
		error("<shorthand> must be a single character")
	elif description == None:
		error("For usablility, make sure to include a description. If you don't want a description, set description=\"\".")
	else:
		shorthands[shorthand] = argument
		info[argument] = [function, description]

def handle_args():
	global help_message
	descs = [info[i][1] for i in info]
	for arg, short, desc in zip(info, shorthands, descs):
		help_message += f"--{arg}    \t-{short}\t\t{desc}\n"
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
					info[v[2:]][0]()
			else:
				error(f"Length of argument must be greater than zero")
		elif v[0] == "-":
			for value in v[1:]:
				info[shorthands[value]]()

add_argument("help", "h", help_function, "Displays this message")