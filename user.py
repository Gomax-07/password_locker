class User:
    """
    Class that generates new instances of users
    """
    user_list =[]

    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.pass_word = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

      

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



