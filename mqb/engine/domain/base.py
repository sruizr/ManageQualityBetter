class Node:
	def __init__(self, name=None):
		self.name = name


class Person(Node):
	pass

class Machine(Node):
	pass


class Movement:
	def __inti__(self, category):
		self.category = category


class Process(Movement):
 	pass


class Resource:
	pass


class Material(Resource):
	def __init__(self, qty=1):
		self.qty = 1


class 