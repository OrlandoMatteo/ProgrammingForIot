import json
class Contact():
	def __init__(self,name,surname,mail):
		self.name=name
		self.surname=surname
		self.mail=mail
	def __repr__(self):
		return "Name:{}, Surname:{}, mail:{}".format(self.name,self.surname,self.mail)
	def jsonify(self):
		contact={'name':self.name,'surname':self.surname,'mail':self.mail}
		return contact

class AddressBook():
	def __init__(self):
		file_content=json.load(open('contacts.json'))
		self.contacts=[]
		for contact in file_content.get('contacts'):
			self.contacts.append(Contact(contact.get('name'),contact.get('surname'),contact.get('email')))
	
	def show(self):
		for contact in self.contacts:
			print(contact)
	
	def find_by_name(self,name):
		results=[contact for contact in self.contacts if contact.name==name]
		print("I found the following results:\n")
		for x in results:
			print(x)
	def find_by_surname(self,surname):
		results=[contact for contact in self.contacts if contact.surname==surname]
		print("I found the following results:\n")
		for x in results:
			print(x)
	def add_contact(self,name,surname,mail):
		"""
		new_contact(name,surname,mail):
		"""
		self.contacts.append(Contact(name,surname,mail))
		
	def remove_contact(self,name):
		"""remove_contact(name)"""
		contact=[contact for contact in self.contacts if contact.name==name]
		self.contacts.pop(self.contacts.index(contact[0]))
	def save(self):
		"""save()"""
		fp=open('contacts.json','w')
		content={'contacts':[]}
		for c in self.contacts:
			content['contacts'].append(c.jsonify())
		json.dump(content,fp)
		fp.close()

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
			book.remove_contact('name')
		elif command=='q':
			book.save()
			break
		else:
			print('Command not available')
	
		
			
		
		
	
		
	
	