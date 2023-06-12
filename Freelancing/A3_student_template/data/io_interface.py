class IOInterface:

    #Function to get the user input by displaying the message and return the list of args
    def get_user_input(self,msg,num_of_args):
        print(msg)
        args = input()
        args= args.split(' ')
        if(len(args)<num_of_args):
            while(len(args)<num_of_args):
                args.append("")
        return args
    
    #The main driver menu
    def main_menu(self):
        print("\nMAIN MENU")
        print('1.Login')
        print('2.Register')
        print('3.Exit')
        ch = input("Enter your Choice : ")
        try:
            ch = int(ch)
            if(ch>3 or ch<1):
                print("Please enter a valid entry")
                self.main_menu()
        except:
            print("Please enter a valid entry")
            self.main_menu()
        return ch

    #Function to cordinate the admin menu
    def admin_menu(self):
        print('\nADMIN MENU')
        print('1.Show products')
        print('2.Add customers')
        print('3.Show customers')
        print('4.Show orders')
        print('5.Generate test data')
        print('6.Generate all statistical figures')
        print('7.Delete all data')
        print( '8.Delete customer using customer id')
        print('9.Delete order using order id')
        print('10.Delete product using product id')
        print('11.Logout')
        ch = input("Enter your choice : ")
        try:
            ch = int(ch)
            if(ch>11 or ch<1):
                print("Please enter a valid entry")
                self.admin_menu()
        except:
            print("Please enter a valid entry")
            self.admin_menu()
        return ch
    
    #Function to cordinate the Customer Menu
    def customer_menu(self):
        print('\nCUSTOMER MENU')
        print('1.Show profile')
        print('2.Update profile')
        print('3.Show products (user input could be “3 keyword” or “3”)')
        print('4.Show history orders')
        print('5.Generate all consumption figures')
        print('6.Get product using product id')
        print('7.Logout')
        ch = input()
        try:
            ch = int(ch)
            if(ch>7 or ch<1):
                print("Please enter a valid entry")
                self.customer_menu()
        except:
            print("Please enter a valid entry")
            self.customer_menu()
        return ch
    
    #Prints a message
    def print_message(self,msg):
        print(msg)

    #prints an object
    def print_object(self,obj):
        print(obj.__str__())
    
    #prints an error message
    def print_error_message(self,source,msg):
        print(source,msg)