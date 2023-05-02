from User import User

class UserTeacher(User):
    units={}
    students={}
    def __init__(self,name,pwd,unit,logged=False):
       
        super().__init__(name,pwd,"TA","enabled",logged)
        if(not logged and not self.check_username_exists(name)):
            file1 = open('data/unit.txt', 'r')
            Lines = file1.readlines()
            file1.close()
            new_unit_data=[]
            for line in Lines:
                if(str(unit.unit_id) in line):
                    data = list(line.split())
                    if(len(data)>4):
                        data[4]+=","+str(self.user_id)
                        line = ' '.join(data)
                        line+='\n'
                    else:
                        line=line[:-1]+" "+str(self.user_id)+"\n"
                new_unit_data.append(line)
            file1 = open('data/unit.txt', 'w')
            file1.writelines([string for string in new_unit_data])
            file1.close()

    def __str__(self):
        print (str(self.user_id )+ ", "+  self.user_name + ", "+ self.user_password + ", "+  self.user_role + ", "+  self.user_status)
    
    def teacher_menu(self):
        print("\nTeacher Menu.")
        print('1.List all Units')
        print('2.Add a unit')
        print('3.Remove a unit')
        print('4.List all students')
        print('5.Exit')
        choice = input("Enter you choice: ")
        print("")
        if(choice == '1'):
            self.list_teach_units()
        elif(choice == '2'):
            code = input("please enter unit code: ")
            self.add_teach_unit(code)
        elif(choice == '3'):
            code = input('enter the unit code: ')
            self.delete_teach_unit(code)
        elif(choice == '4'):
            self.list_enrol_students()
        elif(choice == '5'):
            return False
        else:
            print("Please enter valid choice.")
        return True



    def list_teach_units(self):
        file1 = open('data/unit.txt', 'r')
        Lines = file1.readlines()
        file1.close()
        units = []
        for line in Lines:
            if(str(self.user_id) in line):
                data = line.split()
                units.append(data[1])
        if(len(units)==0):
            print("No units for the teacher")
        else:
            for unit in units:
                print(unit)
        
    def add_teach_unit(self,code):
        file1 = open('data/unit.txt', 'r')
        Lines = file1.readlines()
        file1.close()
        new_unit_data = []
        for line in Lines:
            if(code in line):
                data = list(line.split())
                if(len(data)>4):
                    data[4]+=","+str(self.user_id)
                    line = ' '.join(data)
                    line+='\n'
                else:
                    line=line[:-1]+" "+str(self.user_id)+"\n"
            new_unit_data.append(line)
        file1 = open('data/unit.txt', 'w')
        file1.writelines([string for string in new_unit_data])
        file1.close()

    
    def delete_teach_unit(self,code):
        file1 = open('data/unit.txt', 'r')
        Lines = file1.readlines()
        file1.close()
        new_unit_data = []
        for line in Lines:
            if(code in line):
                if(self.user_id in line):
                    data = list(line.split())
                    if(len(data)>4):
                        temp = data[4].split(',')
                        for i in range(len(temp)):
                            id = temp[i]
                            if(id == self.user_id):
                                temp.pop(i)
                                if(len(temp)==0):
                                    data[4]=''
                                elif(len(temp)==1):
                                    data[4] = temp[0]
                                else:
                                    data[4] = ','.join(temp)
                                line = ' '.join(data)+'\n'
                                break        
            new_unit_data.append(line)
        file1 = open('data/unit.txt', 'w')
        file1.writelines([string for string in new_unit_data])
        file1.close()

    def list_enrol_students(self):
        file1 = open('data/unit.txt', 'r')
        Lines = file1.readlines()
        file1.close()
        students = []
        for line in Lines:
            data = line.split()
            if(not len(data)<6):
                stus =list( data[5].split(','))
                students+=stus
        if(len(students)==0):
            print("No Students")
        else:
            print("")
            for stu in students:
                print(stu)