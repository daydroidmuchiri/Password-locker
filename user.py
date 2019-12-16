class User:
	'''
	Class that generates user accounts and save their information
	'''
	
	users_list = []
	# def setUp(self):
	# 	'''
	# 	'''
	# 	self.new_user = User("Ngina","Phillis","ngina123")

	def __init__(self,username,password):
		'''
		Method to define the properties that each user object will hold.
		'''

		# instance variables
		self.username = username
		# self.account = account
		self.password = password

	def save_user(self):
		''' 
		save_user method saves newly created users to users_list
		'''
		User.users_list.append(self)

	def delete_user(self):
		User.users_list.remove(self)
	
	@classmethod 
	def user_exists(cls,name):
		for user in cls.users_list:
			if user.username == name :
				return True
		return False

