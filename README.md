# ctai
This plugin combines aiio models and functionality with the cantools bot system.

# Back (Init Config)

    dirs = ["bots"]
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
    