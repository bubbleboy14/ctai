import random
from aiio import getBrain
from cantools.web import respond, succeed, cgi_get
from cantools import config

randos = [
	"Arnold Schwarzeneggar",
	"Pee Wee Herman",
	"Prince Charles",
	"Barney the Dinosaur"
]

def response():
	idef = config.brain or random.choice(randos)
	iden = cgi_get("identity", default=idef)
	brain = getBrain(iden, vibe=cgi_get("vibe", default="all"),
		mood=cgi_get("mood", required=False), options=cgi_get("options", required=False))
	succeed(brain(cgi_get("statement"), cgi_get("name", default=iden), cgi_get("asker", default="rando")))

respond(response)