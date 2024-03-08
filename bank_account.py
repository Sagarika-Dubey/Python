#bank account problem
class bank_account():
    def info(self, balance=0):
        self.balance=balance

    def deposit(self, amount):
        if(amount>0):
            self.balance=self.balance+amount
            print(f"You have deposited {amount} ruppes in your bank account")
        else:
            print("Deposit an amount greater than 0")
    
    def withdraw(self,amount):
        if (0<amount<=self.balance):
            self.balance=self.balance-amount
            print(f"Withdraw Amount {amount} Rs. \nAnd current balance: {self.balance}Rs.")
        else:
            print("Sorry withdraw value 0 or greater than current balance")

    def chkbal(self):
        print("Current Balance in you account is:",self.balance)

print("Welcome to your Bank😁")
xx=bank_account()
balance=int(input("Enter the balance in your bank account: "))
xx.info(balance)

while True:
    choice=int(input("\nEnter the choices according to the actions 2which you want to perform:\n1.Deposit \n2.Withdraw \n3.Check bank balance \n4.Exit \n"))
    if choice==1:
        amount=int(input("Enter the amount that you want to deposit: "))
        xx.deposit(amount)
    elif choice==2:
        amount=int(input("Enter the amount that you want to withdraw: "))
        xx.withdraw(amount)
    elif choice==3:
        xx.chkbal()
    elif choice==4:
        print("Thank you😊❤️ \nDo visit our bank again")
        break
    else:
        print("Invalid entry. Please enter a correct choice")

        
