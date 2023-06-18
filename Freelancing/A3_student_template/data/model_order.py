#Order Class
class Order:
    def __init__(self,orderID,CustomerID,ProductID,time):
        self.order_id = orderID
        self.user_id = CustomerID
        self.pro_id = ProductID
        self.order_time = time
    def __str__(self):
        print("Order ID: ",self.order_id,end=', ')
        print("User ID: ",self.user_id,end=', ')
        print("Product ID: ",self.pro_id,end=', ')
        print("Order Time: ",self.order_time,end=', ')
    