#User class
class User:
    def __init__(self,user_id,user_name,user_password,user_register_time,role):
        self.user_id =user_id
        self.user_name  =user_name
        self.user_password =user_password
        self.user_registered_time=user_register_time
        self.user_role =role
    
    def __str__(self):
        print( 'User ID: ',self.user_id ,end=", ")
        print( 'User Name: ',self.user_name,end=", ")
        print( 'User Password: ', self.user_password,end=", ")
        print( 'User Registration Time: ', self.user_registered_time,end=", ")
        print( 'User Role: ', self.user_role,end=".")