# -*- coding: utf8 -*-
import math
import json

class Agent:
	
	def say_hello(self, first_name):
		return "Bien le bonjour " + first_name + " !"

	def __init__(self, position, **agent_attributes):
		self.position = position
		for attr_name, attr_value in agent_attributes.items():
			setattr(self, attr_name, attr_value)

class Position:
	def __init__(self, longitude_degrees, latitude_degrees):
		self.longitude_degrees = longitude_degrees
		self.latitude_degrees = latitude_degrees

	@property
	def longitude(self):
		return self.longitude_degrees * math.pi / 180

	@property
	def latitude(self):
		return self.latitude_degrees * math.pi / 180
	
	

def main():
	for agent_attributes in json.load(open("agents-100k.json")):
		longitude = agent_attributes.pop("longitude")
		latitude = agent_attributes.pop("latitude")
		position = Position(longitude, latitude)
		agent = Agent(position, **agent_attributes)
		print(agent.position.latitude)

main()