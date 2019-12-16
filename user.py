import pyperclip
import string
import random
from user import User

class Credential:
	'''
	Class to create  account credentials, generate passwords and save credentials and passwords
	'''
	# Class Variables

	credentials_list =[]

	def __init__(self,account,userName,password):

		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.account = account
		self.userName = userName
		self.password = password

	def save_credentials(self):
		'''
		save_credentials method saves a newly created users to credentials_list
		'''
		# global users_list
		Credential.credentials_list.append(self)

	def delete_credential(self):
		'''
		Deletes credentials on user command
		'''

		self.credentials_list.remove(self)	

	@classmethod
	def find_credentials(cls,account):
		'''
		Method that finds credentials from credentials_list
		'''
		for new in cls.credentials_list:
			if new.account == account:
				return new
		
	@classmethod
	def credential_exists (cls,account):
		'''
		Method that checks if a credential exists in the credentials_List
		'''
		for exist in cls.credentials_list:
			if exist.account == account:
				return True
		return False


	def generate_password(self):
		'''
		Method to generate an 8 character password for a user 
		'''
		user_password = string.ascii_lowercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
		return ''.join(random.choice(user_password) for _ in range(0,12))

	@classmethod
	def display_credentials(cls):
		'''
		Class method to display the list of credentials saved
		'''
		return cls.credentials_list

	# @classmethod
	# def copy_credential(cls,site_name):
	# 	'''
	# 	Class method that copies a credential's info after the credential's site name is entered
	# 	'''
	# 	find_credential = Credential.find_by_site_name(site_name)
	# 	return pyperclip.copy(find_credential.password)


