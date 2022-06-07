class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposite(self,amount):
        self.account_balance+=amount
   
    def make_withdrawal(self, amount):
        self.account_balance-=amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self, other_user, amount):
        other_user.account_balance+=amount
        self.account_balance-=amount


yahya=User("Yahya","Yahya@gmail.com")
bushra=User("Bushra","bushra@gmail.com")
talal=User("Talal","talal@gmail.com")

yahya.make_deposite(1000)
yahya.make_deposite(2000)
yahya.make_deposite(4000)
yahya.make_withdrawal(1000)
yahya.display_user_balance()


bushra.make_deposite(2000)
bushra.make_deposite(2500)
bushra.make_withdrawal(600)
bushra.make_withdrawal(150)
bushra.display_user_balance()


talal.make_deposite(5000)
talal.make_withdrawal(200)
talal.make_withdrawal(300)
talal.make_withdrawal(1000)
talal.display_user_balance()

yahya.transfer_money(talal,3000)
talal.display_user_balance()
yahya.display_user_balance()
