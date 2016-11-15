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
	brain = getBrain(config.brain or random.choice(randos), fallback=True)
	statement = cgi_get("statement")
	succeed(brain(statement))

respond(response)