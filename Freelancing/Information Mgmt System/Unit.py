import random
class Unit:
    unit_id  = ''
    unit_code = ''
    unit_name = ''
    unit_capacity = ''
    def __init__(self,code,name,capacity):
        
        self.units={}
        file1 = open('data/unit.txt', 'r')
        Lines = file1.readlines()
        file1.close()
        for line in Lines:
            if(code in line):
                return
            if(len(line.split())==4):
                [id1,name1,code1,capacity1] = line.split()
                self.units[id1] = [code1,name1,capacity1]
            elif(len(line.split())==5):
                [id1,name1,code1,capacity1,teachers] = line.split()
                self.units[id1] = [code1,name1,capacity1,teachers]
        
        self.unit_id = self.generate_unit_id()
        self.unit_code = code
        self.unit_name = name
        self.unit_capacity = capacity

        file1 = open("data/unit.txt", "a")  # append mode
        file1.write(str(self.unit_id)+" "+self.unit_name+" "+self.unit_code+" "+str(self.unit_capacity)+"\n")
        file1.close()

    def __str__(self) -> str:
        print( str(self.unit_id)+","+self.unit_code+"," +self.unit_name+"," +str(self.unit_capacity))
    
    def generate_unit_id(self):
        id = random.randint(1000000,9999999)
        while(id in list(self.units.keys())):
            id = random.randint(1000000,9999999)
        return id
        

