#Producrt class
class Product:
    def __init__(self,id='',model='',cat='',dis='',name='',curr='',raw='',likes=''):
        self.pro_id = id
        self.pro_model = model
        self.pro_category = cat
        self.pro_discount = float(dis)
        self.pro_name = name
        self.pro_current_price = float(curr)
        self.pro_raw_price = float(raw)
        self.pro_likes_count = int(likes)
    
    def __str(self):
        print("ID: ",self.pro_id,end=', ')
        print("Model: ",self.pro_model,end=', ')
        print("Category: ",self.pro_category,end=', ')
        print("Discount: ",self.pro_discount,end=', ')
        print("Name: ",self.pro_name, end=', ')
        print("Current Price: ",self.pro_current_price, end=', ')
        print("Raw Price: ",self.pro_raw_price, end=', ')
        print("Likes Count: ",self.pro_likes_count, end=', ')