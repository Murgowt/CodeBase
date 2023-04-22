class Bank:
    def takeMoney(self,money):
        self.BusienessLogic(money)
    
    def BusienessLogic(self,money):
        print(money+10)
    

SBI = Bank()

SBI.takeMoney(10)