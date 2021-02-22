class Node():
	def __init__(self, _label):
		self.label = _label
	def __str__(self):
		return "Node({})".format(self.label)
	def distance(self, nodeB):
		if self.label == nodeB.label:
			return 0
		for i in range(1, len(self.label)):
			if self.label[i:] == nodeB.label[:-i]:
				return i
		return ORDER