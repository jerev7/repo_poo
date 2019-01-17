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

class Zone:
	
	MIN_LONGITUDE_DEGREES = -180
	MAX_LONGITUDE_DEGREES = 180
	WIDTH_DEGREES = 1
	HEIGHT_DEGREES = 1
	MIN_LATITUDE_DEGREES = -90
	MAX_LATITUDE_DEGREES = 90
	ZONES = []

	def __init__(self, corner1, corner2, inhabitants):
		self.corner1 = corner1
		self.corner2 = corner2
		self.inhabitants = 0

	@classmethod
	def initialize_zones(cls):
		for latitude in range (cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
			for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, self.WIDTH_DEGREES):
				bottom_left_corner = Position(longitude, 1)
				top_right_corner = Position(longitude + cls.WIDTH_DEGREES, 1 + cls.HEIGHT_DEGREES)
				zone = Zone(bottom_left_corner, top_right_corner)
				cls.ZONES.append(zone)
	

def main():
	for agent_attributes in json.load(open("agents-100k.json")):
		longitude = agent_attributes.pop("longitude")
		latitude = agent_attributes.pop("latitude")
		position = Position(longitude, latitude)
		agent = Agent(position, **agent_attributes)
		

main()