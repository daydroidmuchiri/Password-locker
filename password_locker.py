import pyperclip
from user import User
from credentials import Credential
import string
import random

def create_user(username,password):
	'''
	Function to create a new user account
	'''
	new_user = User(username,password)
	return new_user

def save_user(user):
	'''
	Function to save new user account
	'''
	user.save_user()

def user_exist (name):
	'''
	Checks if user exists
	'''
	return User.user_exists(name)
		
# def verify_user(firstname,password):
# 	'''
# 	Function that verifies the existence of the user before creating user credentials
# 	'''
# 	verify_user = Credential.check_user(firstname,password)
# 	return verify_user

def create_credential (account, userName, password):
	'''
	Function creates new credential
	'''
	new_credential = Credential ( account, userName, password)
	return new_credential


def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials (credential)

def find_credentials(account):
	'''
	Method to find credentials
	'''
	return Credential.find_credentials(account)

def check_credentials(account):
	'''
	Checks if credential exists
	'''
	return Credential.credential_exists(account)

def delete_credentials(credential):
	'''
	Deletes credential after user command 
	'''
	return Credential.delete_credential(credential)

def display_credentials(user_name):
	'''
	Function to display credentials created and saved by the user
	'''
	return Credential.display_credentials ()

def generate_password(self):
	'''
	Method to generate an 8 character password for a user 
	'''
	ge_password = generate_password(self)
	return ge_password

			
def main():
	while True:
	 print(' ')
	 print('******Hey there, welcome to password locker***** I would like to: \n 1-Create an Account \n 2-Log In \n 3-Exit')
	 print(' ')
	 short_code = input().lower().strip()
	 if short_code == "1":
		 print('Enter preferred username')
		 user_name = input()
		 print ('Create password')
		 password = input ()
		 save_user(create_user(user_name,password))
		 print(" ")
		 print(f"New Account Created for: {user_name} password: {password}")
		 print("-"*69)

		 while True:
			 print("")
			 print("Log in ")
			 print("Enter your username")
			 username = input()
			 print("Enter password")
			 password1 = input()

			 if username != user_name or password1 != password:
				 print("Please enter correct account details!")

				 continue
			 else:
				 print(f"Welcome to your password locker account {username}.")
				 print(" ")
				 print(" ")
				

				 while True:
					 print("\n AD- Add credential \n VW- View existing credentials \n RM- Delete credential \n EX- Exit application")
					 
					 option = input()

					 if option == 'AD':
						 while True:
							 print ("Continue to add account (Y-Yes/ N- No)")
							 addacc = input()
							 if addacc == "Y":
								 
								 print ("Enter Account name")
								 accountname = input()
								 print ("Enter user name")
								 accuser = input()
								 print ( "Enter password")
								 print("Would you like a computer generated password?(Y/N)")
								 accpassword = input()
								 if accpassword == "Y":
								 	 accpassword = random.randint(9, 30000)
								 	 print (" ")
								 	 print (f"Account:{accountname} username: {accuser} password: {accpassword}")
								 elif accpassword == "N":
								 	 print ("Create password")
								 	 accpassword = input ()
								 	 print (f"Account:{accountname} username: {accuser} password: {accpassword}")
									#  print ("_" * 69 )	
								 
								 save_credential(create_credential(accountname, accuser, accpassword))
							 elif addacc == "N":
								 break
							 else:
								 print ("Invalid choice")
					 elif option == "VW":
						 while True:
							#  print ("Here are your credentials:")
							 if display_credentials (user_name):
								 for credential in display_credentials(user_name):
									 print ("Here are your credentials:")
									 print (f"Account : {credential.account} username: {credential.userName} password: {credential.password}")

									 print ("=" * 69 )

							 else:
								 print ("Your credential list is empty")
								 
							 print ("To go back to main menu - menu, to exit- Ex ")

							 back = input()
							 if back == "menu":
								 break
							 elif back == "Ex":
								 continue
							 else:
								 print("Enter valid option!")

					 elif option == "RM":
						 print ("What account would you like to delete?")
						 credname = input()
						 if check_credentials(credname):
							 deletecred = find_credentials(credname)
							 print ("Are you sure you want to delete credential? (Y-Yes N-No)")
							 delete = input()
							 if delete == 'Y':
								 delete_credentials(deletecred)
								 print("Credential has been removed from list")
								 break
							 elif delete == 'N':
								 continue
						 else:
							 print("Credential not found")

					 elif option == "EX":
						 print("Are you sure you want to leave password locker? Y-Yes/ N-No")

						 leave = input ()
						 if leave == "Y":
							 print("Successfully exited!")
							 break

						 else:
							 if leave == "N":
								 continue
	 if short_code == "2":
			 print("")
			 print("Log in ")
			 print("Enter your username")
			 username = input()
			 print("Enter password")
			 password1 = input()

			 verify = user_exist(username)

			 if verify == True:
				 print("Welcome to your password locker account!")
			
				 while True:
					 print("\n AD- Add credential \n VW- View existing credentials \n RM- Delete credential \n EX- Exit application")
					 
					 option = input()

					 if option == 'AD':
						 while True:
							 print ("Continue to add account (Y-Yes/ N- No)")
							 addacc = input()
							 if addacc == "Y":
								 
								 print ("Enter Account name")
								 accountname = input()
								 print ("Enter user name")
								 accuser = input()
								 print ( "Enter password")
								 print("Would you like a computer generated password?(Y/N)")
								 accpassword = input()
								 if accpassword == "Y":
								 	 accpassword = random.randint(9, 30000)
								 	 print (" ")
								 	 print (f"Account:{accountname} username: {accuser} password: {accpassword}")
								 elif accpassword == "N":
								 	 print ("Create password")
								 	 accpassword = input ()
								 	 print (f"Account:{accountname} username: {accuser} password: {accpassword}")
									#  print ("_" * 69 )	
								 
								 save_credential(create_credential(accountname, accuser, accpassword))
							 elif addacc == "N":
								 break
							 else:
								 print ("Invalid choice")
					 elif option == "VW":
						 while True:
							#  print ("Here are your credentials:")
							 if display_credentials (user_name):
								 for credential in display_credentials(user_name):
									 print ("Here are your credentials:")
									 print (f"Account : {credential.account} username: {credential.userName} password: {credential.password}")

									 print ("=" * 69 )

							 else:
								 print ("Your credential list is empty")
								 
							 print ("To go back to main menu - menu, to exit- Ex ")

							 back = input()
							 if back == "menu":
								 break
								 
							 elif back == "Ex":
								 continue
							 else:
								 print("Enter valid option!")

					 elif option == "RM":
						 print ("What account would you like to delete?")
						 credname = input()
						 if check_credentials(credname):
							 deletecred = find_credentials(credname)
							 print ("Are you sure you want to delete credential? (Y-Yes N-No)")
							 delete = input()
							 if delete == 'Y':
								 delete_credentials(deletecred)
								 print("Credential has been removed from list")
								 break
							 elif delete == 'N':
								 continue
						 else:
							 print("Credential not found")

					 elif option == "EX":
						 print("Are you sure you want to leave password locker? Y-Yes/ N-No")

						 leave = input ()
						 if leave == "Y":
							 print("Successfully exited!")
							 break
				             
						 else:
							 if leave == "N":
								 continue	  
			 
			 else:
				 print(f"That username does not exist.Please create an account")
				 print(" ")
				 print(" ")
				

	 if short_code == "3":	
				  break	 
				
if __name__ == '__main__':
	main()














