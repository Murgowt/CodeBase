from io_interface import IOInterface
from operation_user import UserOperation
import ast
from model_customer import Customer
from opreation_product import ProductOperation
from operation_order import OrderOperation
from model_admin import Admin
from model_user import User
from operation_customer import CustomerOperation
from operation_admin import AdminOperation
IO=IOInterface()
UO = UserOperation()
PO = ProductOperation()
OO = OrderOperation()
CO = CustomerOperation()
AO = AdminOperation()


#Inputs the creds and logs in an user
def login_control():
    username = input("Enter username: ")
    pwd = input("Enter passwrod: ")
    res=UO.login(username,pwd)
    if(res=='customer'):
        customer_control(username)
    elif(res=='admin'):
        admin_control(username)
    else:
        print("Invalid Credentials")
        main()

#driver function for the customer menu
def customer_control(username):
    f  = open('data/users.txt','r')
    lines = f.readlines()
    f.close()
    id = ''
    pwd = ''
    time =''
    for line in lines:
        data = ast.literal_eval(line)
        if(data['user_name']==username):
            id = data['user_id']
            pwd = data['user_password']
            time = data['user_registered_time']
    cus = Customer(id,username,pwd,time,'customer')
    ch=IO.customer_menu()
    #Displays information of a customer
    if(ch==1):
        cus.__str__()
    #updates a customer
    elif(ch ==2 ):
        attribute = input('What do you want to change(user_password/user_name): ')
        newValue = input('Enter new Value: ')
        try:
            cus.update_customer(attribute,newValue)
        except:
            print("Please choose either user_password or user_name")
    #Gets the products information
    elif(ch ==3):
        pg = int(input("Enter page number: "))
        data=PO.get_product_list(pg)
        for pro in data[0]:
            print(pro.pro_name)
    #Gets the order history of cusotomer
    elif(ch==4):
        his = OO.get_history_of_customer_order(id)
        f = open('data/products.txt','r')
        lines = f.readlines()
        objs=[]
        data={}
        for line in lines:
            obj = ast.literal_eval(line)
            if(str(obj['pro_id']) in his):
                objs.append(obj['pro_name'])
        print("Products ordered previously: ")
        for i in objs:
            print(i)
    #Generates the cutomer's consumption graph
    elif(ch ==5):
        OO.generate_single_customer_consumption(id)
    #Gets a product info
    elif(ch==6):
        proID = int(input("Enter product ID: "))
        product = PO.get_product_by_id(proID)
        if(product is None ):
            print("Product ID is invalid")
        else:
            print(product.pro_name)
    elif(ch==7):
        main()
        return
    customer_control(username)

#Driver function for the Admin menu
def admin_control(username):
    f  = open('data/users.txt','r')
    lines = f.readlines()
    f.close()
    id = ''
    pwd = ''
    time =''
    for line in lines:
        data = ast.literal_eval(line)
        if(data['user_name']==username):
            id = data['user_id']
            pwd = data['user_password']
            time = data['user_registered_time']
    cus = User(id,username,pwd,time,'admin')
    ch=IO.admin_menu()
    #Displays the product infos
    if(ch==1):
        pg = int(input("Enter page number: "))
        data=PO.get_product_list(pg)
        for pro in data[0]:
            print(pro.pro_name)
    #creates a customer
    elif(ch==2):
        username = input("Enter Username: ")
        pwd = input("Enter password: ")
        email = input("Enter email: ")
        mobile = input("Enter Mobile: ")
        if(CO.register_customer(username,pwd,email,mobile) != False):
            print("Customer created.")
    #displays the product info
    elif(ch == 3):
        page_no = int(input("Enter page number: "))
        cus=CO.get_customer_list(page_no)
        for custs in cus[0]:
            print(custs.user_name)
    #Displays orders
    elif(ch==4):
        pg = int(input("Enter page number: "))
        print("The order IDs on the page are: ")
        data=OO.get_order_list(pg)
        for pro in data[0]:
            print(pro.order_id)
    #Generate Test data
    elif(ch==5):
        OO.generate_test_order_data()

    #Creates all the graphs
    elif(ch==6):
        PO.generate_category_figure()
        PO.generate_discount_figure()
        PO.generate_likes_count_figure()
        OO.generate_all_customers_consumption_figure()
        OO.generate_all_top_10_best_sellers()
    
    #Deletes all data
    elif(ch==7):
        PO.delete_all_products()
        OO.delete_all_orders()
        CO.delete_all_customers()

    #deletes a customer
    elif(ch==8):
        cusID = input("Enter customerID : ")
        CO.delete_customer(cusID)
    #deletes a  order
    elif(ch==9):
        orderID = input("Enter Order ID: ")
        OO.delete_order(orderID)
    
    #deletes a product
    elif(ch==10):
        proID = input("product ID: ")
        PO.delete_product(proID)
    
    #logout
    elif(ch==11):
        main()
        return
    
    admin_control(username)

        
#Main Menu
def main():
    ch=IO.main_menu()
    if(ch ==1):
        login_control()
    elif(ch==2):
        username = input("Enter Username: ")
        pwd = input("Enter password: ")
        email = input("Enter email: ")
        mobile = input("Enter Mobile: ")
        if(CO.register_customer(username,pwd,email,mobile) != False):
            print("Customer created.")
            
    elif(ch==3):
        return
    main()
        

main()