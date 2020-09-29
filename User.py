
class User:
    def __init__(self, name_input, email_input):
        self.name = name_input
        self.email = email_input
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
        return self

guido = User("Guido van Rossum", "guido@python.com")
madison = User("Madison Parker Hanberry", "mhanberry@fakemail.nope")
cloud = User("Cloud Gooksu Hanberry", "cgooksu@pawmail.nope")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(50)
guido.display_user_balance()

madison.make_deposit(400)
madison.make_deposit(600)
madison.make_withdrawal(200)
madison.make_withdrawal(200)
madison.display_user_balance()

cloud.make_deposit(700)
cloud.make_withdrawal(100)
cloud.make_withdrawal(100)
cloud.make_withdrawal(100)
cloud.display_user_balance()
