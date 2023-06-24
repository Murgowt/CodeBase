import pandas as pd
import glob
import json
from datetime import datetime
import ast
from model_product import Product
import matplotlib.pyplot as plt
from operation_user import UserOperation

class AdminOperation:
    #Registers an admin
    def register_admin(self):
        f  = open('data/users.txt','r')
        lines = f.readlines()
        f.close()
        usernames =[]
        for line in lines:
            data = ast.literal_eval(line)
            if(data['user_role']=='admin'):
                usernames.append(data['user_name'])
            
        time = datetime.now()
        time= time.strftime("%d-%m-%Y_%H:%M:%S")
        UO = UserOperation()
        user_id = UO.generate_unique_user_id()
        username= 'admin1'
        i=1
        while(username in usernames):
            username= 'admin'+str(i)
            i+=1
        pwd='pwd'+str(i)
        user_role = 'admin'
        user_register_time =time
        
        f  = open('data/users.txt','r')
        lines = f.readlines()
        f.close()
        obj = {
            "user_id":user_id,
            "user_name":username,
            "user_password":UO.encrypt_password(pwd),
            'user_registered_time':time,
            'user_role':user_role
        }

        lines.append(str(obj))
        f  = open('data/users.txt','w')
        for i in lines:
            f.write(str(i).rstrip()+"\n")
        f.close()
    