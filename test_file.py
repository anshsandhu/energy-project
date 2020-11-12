class solar(temp):

	def __init__(self):
		self.temp = temp

	def T_o(self,temp):
		return self.temp + 5

ag = solar(5)	

print(ag.T_o())
