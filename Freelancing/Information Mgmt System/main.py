from UserAdmin import UserAdmin
from Unit import Unit
from UserTeacher import UserTeacher
from UserStudent import UserStudent
from User import User

def main_menu():
    logged_in = None
    exit = False
    user = User("test","test",'test','test',False)

    while(not exit):
        if(logged_in is None):
            print("Please log in.")
            user_name = input("Enter username: ").lower()
            pwd = input("Enter password: ")
            role = user.login(user_name,pwd)
            if(role is not None):
                if(role == "AD"):
                    user = UserAdmin(user_name,pwd,True)
                    logged_in = user.user_role
                elif(role == "TA"):
                    user = UserTeacher(user_name,pwd,None,True)
                    logged_in = user.user_role
                elif(role == "ST"):
                    user = UserStudent(user_name,pwd,[],[],True)
                    logged_in = user.user_role
        else:
            if(logged_in == "AD"):
                choice = user.admin_menu()
                if(not choice):
                    exit = True
                
            if(logged_in == "TA"):
                choice = user.teacher_menu()
                if(not choice):
                    exit = True
            
            if(logged_in == "ST"):
                choice = user.student_menu()
                if(not choice):
                    exit = True




def generate_test_data():
    # 1 Admin, 3 units, 3 teachers - one per unit, 10 students - enrolled in all three units

    #Creating admin 
    admin = UserAdmin("admin1","adminpwd")

    # Creating 3 Units
    unit1 = Unit("SUBJ1",'Subject1',30)
    unit2 = Unit("SUBJ2",'Subject2',30)
    unit3 = Unit("SUBJ3",'Subject3',30)
    file1 = open('data/unit.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    # Creating 3 Teachers
    teacher1 = UserTeacher("teacher1","teacher1pwd",unit1)
    teacher2 = UserTeacher("teacher2","teacher2pwd",unit2)
    teacher3 = UserTeacher("teacher3","teacher3pwd",unit3)
    file1 = open('data/unit.txt', 'r')
    Lines = file1.readlines()
    file1.close()
    
    # Creating 10 Students
    student1 = UserStudent("student1","student1pwd",[unit1,unit2,unit3],[unit1,unit2])
    student2 = UserStudent("student2","student2pwd",[unit1,unit2,unit3],[unit1,unit2,unit3])
    student3 = UserStudent("student3","student3pwd",[unit1,unit2,unit3],[unit1,unit2,unit3])
    student4 = UserStudent("student4","student4pwd",[unit1,unit2,unit3],[unit1,unit2,unit3])
    student5 = UserStudent("student5","student5pwd",[unit1,unit2,unit3],[unit1,unit2,unit3])
    student6 = UserStudent("student6","student6pwd",[unit1,unit2,unit3],[unit1,unit2,unit3])
    student7 = UserStudent("student7","student7pwd",[unit1,unit2,unit3],[unit1,unit2,unit3])
    student8 = UserStudent("student8","student8pwd",[unit1,unit2,unit3],[unit1,unit2,unit3])
    student9 = UserStudent("student9","student9pwd",[unit1,unit2,unit3],[unit1,unit2,unit3])
    student10 = UserStudent("student10","student10pwd",[unit1,unit2,unit3],[unit1,unit2,unit3])
    
    main_menu()

def main():
    generate_test_data()

if __name__ == "__main__":
    main()