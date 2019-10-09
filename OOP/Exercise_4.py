class Contact():
	"""Contact defined by his name surname and emal"""
	def __init__(self,name,surname,mail):
		self.name=name
		self.surname=surname
		self.mail=mail
	def __repr__(self):
		return "{},{},{}".format(self.name,self.surname,self.mail)

class AddressBook():
	"""Collection of object of the class Contact
	The available methods are:
	show():shows the list of contacts
	find_by_name():returns all the contact with that name
	find_by_surname():returns all the contact with that surname
	add_contact(name,surname,email):adds the contact to the book
	remove_contact(name): remove all the contacts with the given name
	save():saves the book"""
	def __init__(self):
		fileContent=open('contacts.txt').read()
		self.contacts=[]
		lines=fileContent.splitlines()
		for line in lines:
			contact_raw=line.split(',')
			self.add_contact(contact_raw[0],contact_raw[1],contact_raw[2])
	def show(self):
		"""shows the list of contacts"""
		for contact in self.contacts:
			print(contact)
	
	def find_by_name(self,name):
		"""find_by_name():returns all the contact with that name"""
		results=[contact for contact in self.contacts if contact.name==name]
		print("I found the following results:\n")
		for x in results:
			print(x)
	def find_by_surname(self,surname):
		"""find_by_surname():returns all the contact with that surname"""
		results=[contact for contact in self.contacts if contact.surname==surname]
		print("I found the following results:\n")
		for x in results:
			print(x)
	def add_contact(self,name,surname,mail):
		"""
		add_contact(name,surname,email):adds the contact to the book
		"""
		self.contacts.append(Contact(name,surname,mail))
		
	def remove_contact(self,name):
		"""remove_contact(name): remove all the contacts with the given name"""
		for i in range(len(self.contacts)):
			if self.contacts[i].name==name:
				self.contacts.pop(i)
	def save(self):
		"""save():saves the book"""
		fp=open('contacts.txt','w')
		for c in self.contacts:
			s=c.name+','+c.surname+','+c.mail+'\n'
			fp.write(s)
			
if __name__=="__main__":
	book=AddressBook()
	print('Welcome to the application to manage your contacts')
	c=''
	helpMessage="Press 's' tho show the list of contacts\nPress 'n' to add a contact\nPress 'f' to find a contact\nPress 'd' to delete a contact\nPress 'q'to save end exit"
	while True:
		print(helpMessage)
		command=input()
		if command=='s':
			book.show()
		elif command=='n':
			name=input('Write the name of the contact : ')
			surname=input('Write the surname of the contact : ')
			mail=input('Write the mail of the contact : ')
			book.add_contact(name,surname,mail)
			print('Contact Added')
		elif command=='d':
			name=input('Write the name of the contact you want to delete : ')
			book.remove_contact(name)
		elif command=='q':
			book.save()
			break
		else:
			print('Command not available')