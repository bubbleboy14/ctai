import json, random
from cantools import pubsub
from cantools.util import log
from aiio import Brain

class ChatterBox(pubsub.Bot):
	def __init__(self, server, channel, name=None):
		pubsub.Bot.__init__(self, server, channel, name)
		self.channel = channel
		self.brain = Brain(name, retorts=False)

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
			self.server.publish({
				"message": {
					"action": "say",
					"data": {
						"message": resp
					}
				},
				"channel": self.channel.name
			}, self)
