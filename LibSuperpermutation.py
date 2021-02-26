class Node():
	def __init__(self, _label):
		self.checked = False
		self.label = str(_label)
	def __str__(self):
		return "Node({})".format(self.label)
	def distance(self, nodeB):
		if self.label == nodeB.label:
			return 0
		for i in range(1, len(self.label)):
			if self.label[i:] == nodeB.label[:-i]:
				return i
		return len(self.label)

class Superpermutation():
	def __init__(self, _label=""):
		self.label = _label
		self.weight = len(self.label)
	def __str__(self):
		return "Superpermutation({}: {})".format(self.weight, self.label)
	def include(self, node):
		node.check = True
		if self.label[len(self.label)-len(node.label):] == node.label:
			return self
		for i in range(1, len(node.label)+1):
			if self.label[len(self.label)-(len(node.label)-i):] == node.label[:-i]:
				self.label += node.label[(len(node.label)-i):]
				self.weight += i
				break
		return self