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
	brain = getBrain(cgi_get("identity", default=idef), vibe=cgi_get("vibe", default="all"),
		mood=cgi_get("mood", required=False), options=cgi_get("options", required=False))
	succeed(brain(cgi_get("statement")))

respond(response)