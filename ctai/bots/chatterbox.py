import json, random, event
from cantools import pubsub
from cantools.util import log
from aiio import Brain

class ChatterBox(pubsub.Bot):
	def __init__(self, server, channel, name=None, delay=0, vibe="random", mood=None, options=None):
		pubsub.Bot.__init__(self, server, channel, name)
		self.channel = channel
		self.delay = delay
		self.brain = Brain(name, vibe=vibe, mood=mood, options=None)

	def _pub(self, msg):
		self.server.publish({
			"message": {
				"action": "say",
				"data": {
					"message": msg
				}
			},
			"channel": self.channel.name
		}, self)

	def on_publish(self, data):
		log("ChatterBox received publish: %s"%(json.dumps(data),))
		if data["user"] == self.name:
			return log("(skipping self publish)")
		msg = data["message"]
		if not isinstance(msg, basestring):
			if msg["action"] == "say":
				msg = msg["data"]["message"]
			else:
				return
		log("processing message: %s"%(msg,))
		resp = self.brain(msg)
		if resp:
			event.timeout(self.delay, self._pub, resp)
