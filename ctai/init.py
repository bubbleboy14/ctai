dirs = ["bots", "brains"]
syms = {
	".": ["_respond.py"],
	"bots": ["chatterbox.py"]
}
model = {
	"aiio.model": ["*"]
}
routes = {
	"/_respond": "_respond.py"
}
