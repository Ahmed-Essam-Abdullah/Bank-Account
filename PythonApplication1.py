import random

class BankAccount:
    def  __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
        
    def checkBalance(self):
        print(f"{self.name}, your current balance is {self.balance:.4f} L.E")
        
    def deposit(self,amount):
      if amount < 0:
        print("Sorry sir,please enter a positive amount.")
        return
      self.balance += amount
      print("Deposit successfully")
      self.checkBalance()
      
    def withdraw(self,amount):
      if amount < 0:
        print("Sorry sir, please enter a positive amount.")
      elif amount > self.balance:
        print("Not enough funds to withdraw, please work much harder to get enough money.")
      else:
        self.balance -= amount
        print("Withdrawal successfully")
        self.checkBalance()
           
def generateBankName():
    names = ["Masr","Al-Ahly","CIB"]
    return random.choice(names)

def showOurMenu():
    print("**Main Menu:**")
    print("1: Check Balance")
    print("2: Deposit")
    print("3: Withdraw")
    print("4: Exit") 
    
def main():
    print("Welcome sir to", generateBankName())
    name = input("Please enter your name: ")
    balance = float(input("Please enter your balance:"))
    
    a_account=  BankAccount(name, balance)

    while True:
        showOurMenu()
        
        c= input("Please enter your choice (1-4): ")

        if c=="1":
            a_account.checkBalance()
        elif c=="2":
            amount = float(input("Please enter an amount to deposit: "))
            a_account.deposit(amount)
        elif c=="3":
            amount = float(input("Please enter an amount to withdraw: "))
            a_account.withdraw(amount)
        elif c=="4":
            print(f"Thanks,see you again soon {name}")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4")

main()
