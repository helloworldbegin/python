class BinaryTree():
	def __init__(self,root_obj):
		self.key = root_obj
		self.left_child = None
		self.right_child = None
	def insertLeft(self,new_node):
		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.left_child = self.left_child
			self.left_child = t
	def insertRight(self,new_node):
		if self.right_child == None:
			self.right_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.right_child = self.right_child
			self.right_child = t
	def getLeftChild(self):
		return self.left_child
	def getRightChild(self):
		return self.right_child
	def setRootVal(self,obj):
		self.key = obj
	def getRootVal(self):
		return self.key

class BTreeNode():
	def __init__(self,data):
		self.data = data
		self.left_child = None
		self.right_child = None
	def insertLeftChild(self,child_root):
		if self.left_child == None:
			self.left_child = child_root
		else:
			child_root.left_child = self.left_child
			self.left_child = child_root
	def insertLeft(self,data):
		if self.left_child == None:
			self.left_child = BTreeNode(data)
		else:
			t = BTreeNode(data)
			t.left_child = self.left_child
			self.left_child = t
	def insertRightChild(self,child_root):
		if self.right_child == None:
			self.right_child == child_root
		else:
			child_root.right_child = self.right_child
			self.right_child = child_root
	def insertRight(self,data):
		if self.right_child == None:
			self.right_child = BTreeNode(data)
		else:
			t = BTreeNode(data)
			t.right_child = self.right_child
			self.right_child = t
	def getLeftChild(self):
		return self.left_child
	def getRightChild(self):
		return self.right_child
	def setNodeVal(self,data):
		self.data = data

def buildParseTree(fpexp):
	fplist = fpexp.split()
	p_stack = Stack()
	e_tree = BTreeNode('')
	p_stack.push(e_tree)
	current_tree = e_tree
	for i in fplist:
		if i == '(':
			current_tree.insertLeft('')
			p_stack.push(current_tree)
			current_tree = current_tree.getLeftChild()
		elif i not in ['+','-','*','/',')']:
			current_tree.setNodeVal(int(i))
			current_tree = p_stack.pop()
		elif i in ['+','-','*','/']:
			current_tree.setNodeVal(i)
			current_tree.insertRight('')
			p_stack.push(current_tree)
			current_tree = current_tree.getRightChild()
		elif i == ')':
			current_tree = p_stack.pop()
		else:
			raise ValueError
	return e_tree
