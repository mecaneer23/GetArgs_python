import getargs as ga

def a():
	print("a", end="")
def b():
	print("b", end="")
def c():
	print("c", end="")
def d():
	print("d", end="")
def e():
	print("e", end="")
def f():
	print("f", end="")
def g():
	print("g", end="")
def h():
	print("h", end="")
def i():
	print("i", end="")
def j():
	print("j", end="")
def k():
	print("k", end="")
def l():
	print("l", end="")
def m():
	print("m", end="")
def n():
	print("n", end="")
def o():
	print("o", end="")
def p():
	print("p", end="")
def q():
	print("q", end="")
def r():
	print("r", end="")
def s():
	print("s", end="")
def t():
	print("t", end="")
def u():
	print("u", end="")
def v():
	print("v", end="")
def w():
	print("w", end="")
def x():
	print("x", end="")
def y():
	print("y", end="")
def z():
	print("z", end="")

ga.add_argument("printA", "a", a, "This function prints out the letter \'a\'")
ga.add_argument("printB", "b", b, "This function prints out the letter \'b\'")
ga.add_argument("printC", "c", c, "This function prints out the letter \'c\'")
ga.add_argument("printD", "d", d, "This function prints out the letter \'d\'")
ga.add_argument("printE", "e", e, "This function prints out the letter \'e\'")
ga.add_argument("printF", "f", f, "This function prints out the letter \'f\'")
ga.add_argument("printG", "g", g, "This function prints out the letter \'g\'")
ga.add_argument("printH", "h", h, "This function prints out the letter \'h\'")
ga.add_argument("printI", "i", i, "This function prints out the letter \'i\'")
ga.add_argument("printJ", "j", j, "This function prints out the letter \'j\'")
ga.add_argument("printK", "k", k, "This function prints out the letter \'k\'")
ga.add_argument("printL", "l", l, "This function prints out the letter \'l\'")
ga.add_argument("printM", "m", m, "This function prints out the letter \'m\'")
ga.add_argument("printN", "n", n, "This function prints out the letter \'n\'")
ga.add_argument("printO", "o", o, "This function prints out the letter \'o\'")
ga.add_argument("printP", "p", p, "This function prints out the letter \'p\'")
ga.add_argument("printQ", "q", q, "This function prints out the letter \'q\'")
ga.add_argument("printR", "r", r, "This function prints out the letter \'r\'")
ga.add_argument("printS", "s", s, "This function prints out the letter \'s\'")
ga.add_argument("printT", "t", t, "This function prints out the letter \'t\'")
ga.add_argument("printU", "u", u, "This function prints out the letter \'u\'")
ga.add_argument("printV", "v", v, "This function prints out the letter \'v\'")
ga.add_argument("printW", "w", w, "This function prints out the letter \'w\'")
ga.add_argument("printX", "x", x, "This function prints out the letter \'x\'")
ga.add_argument("printY", "y", y, "This function prints out the letter \'y\'")
ga.add_argument("printZ", "z", z, "This function prints out the letter \'z\'")

try:
	ga.handle_args()
except KeyError:
	print("ERROR: That isn't a valid argument!")