from model_user import User

#Customer Class
class Customer(User):
    def __init__(self,user_id,user_name,user_password,user_register_time,role):
        super().__init__(user_id,user_name,user_password,user_register_time,role)
    
    