class User:
    """
    Class that generates new instances of contacts
    """
    contact_list =[]

    def __init__(self,first_name,last_name,phone_number,email):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

new_contact = User("James","John","08987","james@iajwkdj.com")



print(new_contact.last_name,new_contact.first_name)

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