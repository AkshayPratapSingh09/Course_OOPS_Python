class Bill:
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
        
class Flatmate:
    
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    def pays(self, bill):
        return bill.amount / 2

class pdfreport:
    
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, flatmate1, flatmate2, bill):
        pass
    
bill = Bill(amount=2500, period = "March 2021")
john = Flatmate(name="John", days_in_house = 10)
marry = Flatmate(name= "marry", days_in_house = 20)

        
    
print(john.pays(bill=bill))
        
# print(bill.amount)
# print(bill.period)