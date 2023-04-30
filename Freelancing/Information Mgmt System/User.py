class User:
    users={}
    def __init__(self) :
        file1 = open('data/user.txt', 'r')
        Lines = file1.readlines()
        for line in Lines:
            [user,pwd] = line.split()
            self.users[user] = pwd
        
        print(self.users)


    def encrypt(self,user_password):
        str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str2 = "!#$%&()*+-./:;<=>?@\^_`{|}~"
        encrypted_answer = ""
        for i in range(len(user_password)):
            letter =user_password[i]
            ascii = ord(letter)
            reminder1 = ascii % len(str1)
            str1_letter = str1[reminder1]
            reminder2 = i % len(str2)
            str2_letter = str2[reminder2]
            encrypted_answer+=str1_letter+str2_letter
        encrypted_answer = "^^^" + encrypted_answer + "$$$"
        return encrypted_answer


    def login(self,user_name, user_password):
        if user_name not in self.users:
            return None
        
        if(user_password == self.users[user_name]):
            return("Welcome, "+user_name)

        else:
            return(None)

user = User()