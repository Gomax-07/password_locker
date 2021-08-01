class User:
    """
    Class that generates new instances of contacts
    """
    user_list =[]

    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.pass_word = password
      

new_user = User("James","John","08987")

print("First Name?")
first_name = input()
print("Last Name?")
last_name = input()
print("Password?")
password = input()

user_name = first_name+ ""+last_name
print(user_name,password)


print(new_user.last_name,new_user.first_name,new_user.pass_word)

class Credentials:
    """
    Class that generates new instances of contacts
    """
    credentials_list =[]

    def __init__(self,first_name,last_name,phone_number,email):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

new_contact = Credentials("James","John","08987","james@iajwkdj.com")



print(new_contact.last_name,new_contact.first_name)