import random
from aiio import getBrain
from cantools.web import respond, succeed, fail, cgi_get
from cantools import config, util

randos = [
	"Arnold Schwarzeneggar",
	"Pee Wee Herman",
	"Prince Charles",
	"Barney the Dinosaur"
]

def response():
	idef = config.brain or random.choice(randos)
	identity = cgi_get("identity", default=idef)
	brain = getBrain(identity, vibe=cgi_get("vibe", default="all"),
		mood=cgi_get("mood", required=False), fallback=True)
	succeed(brain(cgi_get("statement")))

respond(response)