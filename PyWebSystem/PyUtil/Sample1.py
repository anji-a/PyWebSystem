import traceback

class Sample1:
	def __init__(self, sessionid={}, params={}, *args, **kwargs):
		self.sessionid = sessionid
		self.params = params
		self.args = args
		self.kwargs = kwargs

	def process(self):
		''' Step 0define'''
		self.fun0()
		for loopindex, element in self.kwargs.items():
			''' Step 1define'''
			self.fun1()
		''' Step 2define'''
		self.fun2()
		
	def fun0(self):
		print("hello", traceback.extract_stack(None, 10))
	def fun1fun0(self):
		print("hello", traceback.extract_stack(None, 10))
	def fun1fun1fun0(self):
		print("hello", traceback.extract_stack(None, 10))
	def fun1fun1(self):
		print("hello", traceback.extract_stack(None, 10))
		''' Step 0define'''
		self.fun1fun1fun0()
		
	def fun1fun2(self):
		print("hello", traceback.extract_stack(None, 10))
	def fun1(self):
		print("hello", traceback.extract_stack(None, 10))
		''' Step 0define'''
		self.fun1fun0()
		for loopindex, element in self.kwargs.items():
			''' Step 1define'''
			self.fun1fun1()
		
		''' Step 2define'''
		self.fun1fun2()
		
	def fun2(self):
		print("hello", traceback.extract_stack(None, 10))