
class Bank:
    bank_name="SBI"
    def __init__(self,account_no,account_holder):
        self.account_no=account_no
        self.account_holder=account_holder
        self.balance=1000

    def display(self):
        print(f"Account no: {self.account_no}")
        print(f"Account name: {self.account_holder}")
        print(f"Current Balance: {self.balance}")

        
    def balance_enquiry(self):
        print(f"{self.account_holder} current balance is {self.balance}")
    
    def depposit(self):
        self.deposit=int(input("enter the deposit amount:"))
        self.balance=self.balance+self.deposit
        print(f"{self.account_holder} current balance is {self.balance}")
        
    def withdraw(self):
        self.draw=int(input("enter the withdrawal amount:"))
        if self.draw > self.balance:
            print("insufficient balance")
        else:
            self.balance=self.balance-self.draw
            print(f"{self.account_holder} current balance is {self.balance}")

    
b1=Bank(123348899,"anu")
while True:
        choice=int(input("Select the option\n1.Account Details\n2.Balance Enquiry\n3.Depposit\n4.Withdraw\n5.ExitEnter the choice:"))
        if choice==1:
                b1.display()
                print("----------------------------")
        elif choice==2:
                b1.balance_enquiry()
                print("----------------------------")
        elif choice==3:
                b1.depposit()
                print("----------------------------")
        elif choice==4:
                b1.withdraw()
                print("----------------------------")
        elif choice==5:
                print("Thank you")
                break
        else:
                print("Invalid choice")
                print("----------------------------")
print("bye")

                    
