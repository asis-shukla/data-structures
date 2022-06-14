#Stack operations
# initialize
# push element, insert new element at the top
# pop element, return top element

class Stack:
	def __init__(self):
		self.stack = []
		self.top = -1

	def push(self, pushed_value):
		self.top = self.top + 1
		self.stack.append(pushed_value)
		return self.top + 1

	def pop(self):
		if self.top == -1:
			return "Stack is empty"
		self.top = self.top - 1
		returnedElement = self.stack[-1]
		self.stack = self.stack[:len(self.stack)-1]
		return returnedElement

tabs = Stack()
tabs.push(2)
tabs.push(7)
el = tabs.pop()
print(el)
e = tabs.push(10)
el = tabs.pop()
print(el)
el = tabs.pop()
print(el)
el = tabs.pop()
print(el)
