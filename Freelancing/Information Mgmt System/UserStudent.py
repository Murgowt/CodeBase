from User import User
import random
class UserStudent(User):
    units=[]
    enrolled_units=[]
    def __init__(self,name,pwd,available_units=[],enrolled_units=[],logged=False):
        super().__init__(name,pwd,"ST","enabled",logged)
        if(not logged and not self.check_username_exists(name)):
            self.units = available_units
            self.enrolled_units = enrolled_units
            file1 = open('data/unit.txt', 'r')
            Lines = file1.readlines()
            file1.close()
            new_unit_data=[]
            for line in Lines:
                for unit in enrolled_units:
                    if(str(unit.unit_id) in line):
                        data = line.split()
                        if(len(data)<5):
                            print("Cant assign a student to a subject without teacher.")
                        else:
                            data = list(line.split())
                            if(len(data)>5):
                                data[5]+=","+str(self.user_id)
                                line = ' '.join(data)
                                line+='\n'
                            else:
                                line=line[:-1]+" "+str(self.user_id)+"\n"
                new_unit_data.append(line)
            file1 = open('data/unit.txt', 'w')
            file1.writelines([string for string in new_unit_data])
            file1.close()
        else:
            return 
        

    def __str__(self):
        print (str(self.user_id )+ ", "+  self.user_name + ", "+ self.user_password + ", "+  self.user_role + ", "+  self.user_status)
    
    def student_menu(self):
        print("\nStudent Menu.")
        print("1.List available units")
        print('2.List enrolled units')
        print('3.Enrol into a unit')
        print('4.drop a unit')
        print('5.Check score')
        print('6.Exit')
        choice = input("Enter your choice: ")

        if(choice =='1'):
            self.list_available_units()
        elif(choice == '2'):
            self.list_enrolled_units()
        elif(choice == '3'):
            code = input("please enter unit code: ")
            self.enrol_unit(code)
        elif(choice == '4'):
            code = input('enter the unit code: ')
            self.drop_unit(code)
        elif(choice == '5'):
            code = input('enter the unit code: ')
            self.list_enrolled_units(code)
        elif(choice == '6'):
            return False
        else:
            print("Please enter valid choice.")
        return True
    
    def list_available_units(self):
        file1 = open('data/unit.txt', 'r')
        Lines = file1.readlines()
        file1.close()
        for line in Lines:
            data = line.split()
            print(data[1])
        
    def list_enrolled_units(self):
        file1 = open('data/unit.txt', 'r')
        Lines = file1.readlines()
        file1.close()
        for line in Lines:
            if(str(self.user_id) in line):
                data = line.split()
                print(data[1])
        
    def enrol_unit(self,code):
        file1 = open('data/unit.txt', 'r')
        Lines = file1.readlines()
        file1.close()
        count=0
        for line in Lines:
            if(str(self.user_id) in line):
                count+=1
        if(count>=3):
            print("Maximum units allowed are 3.")
            return
        else:
            
            file1 = open('data/unit.txt', 'r')
            Lines = file1.readlines()
            file1.close()
            new_unit_data = []
            for line in Lines:
                if(code in line):
                    data = list(line.split())
                    if(len(data)>4):
                        data[5]+=","+str(self.user_id)
                        line = ' '.join(data)
                        line+='\n'
                    else:
                        line=line[:-1]+" "+str(self.user_id)+"\n"
                new_unit_data.append(line)
            file1 = open('data/unit.txt', 'w')
            file1.writelines([string for string in new_unit_data])
            file1.close()


    def drop_unit(self,code):
        file1 = open('data/unit.txt', 'r')
        Lines = file1.readlines()
        file1.close()
        new_unit_data = []
        for line in Lines:
            if(code in line):
                if(self.user_id in line):
                    data = list(line.split())
                    if(len(data)>5):
                        temp = data[5].split(',')
                        for i in range(len(temp)):
                            id = temp[i]
                            if(id == self.user_id):
                                temp.pop(i)
                                if(len(temp)==0):
                                    data[5]=''
                                elif(len(temp)==1):
                                    data[5] = temp[0]
                                else:
                                    data[5] = ','.join(temp)
                                line = ' '.join(data)+'\n'
                                break        
            new_unit_data.append(line)
        file1 = open('data/unit.txt', 'w')
        file1.writelines([string for string in new_unit_data])
        file1.close()

    def check_score(self, unit_code):
        return self.generate_score()

    def generate_score(self,unit_code):
        return random.randint(0,100)
