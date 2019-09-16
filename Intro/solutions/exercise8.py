if __name__=="__main__":
	personal_data={"Name":"",
              "Surname":"",
              "Birth":{
                  "Place of birth":"",
                  "Birthday":""
              },
               "Age":""
              }
	personal_data['Name']=input("Write your name: ")
	personal_data['Surname']=input("Write your surname: ")
	personal_data['Birth']['Place of birth']=input("Write your place of birth: ")
	personal_data['Birth']['Birthday']=input("Write the date of your birthday: ")
	personal_data['Age']=input("Write your age: ")
	
	print(personal_data)