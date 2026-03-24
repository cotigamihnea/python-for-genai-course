import sys
import datetime

def task1():
    
    class Book:
        def __init__(self, title, author, year, pages, is_read = False):
            self.title = title
            self.author = author
            self.year = year
            self.pages = pages
            self.is_read = is_read
            
        def read(self):
            self.is_read = True
            
        def get_info(self):
            print("DETAILS:")
            print(f"Title: {self.title}")
            print(f"Author: {self.author}")
            print(f"Year: {self.year}")
            print(f"Pages: {self.pages}")
            print(f"Read: {'Yes' if self.is_read else 'No'}")
            
        def is_old(self):
            print(f"Book is: {'old' if datetime.datetime.now().year - self.year > 20 else 'new'}.")
            
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 218)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 281)
    book3 = Book("LolPython", "Myself", 2016, 328)

    book1.get_info()
    book2.get_info()
    book2.read()
    book2.get_info()
    book3.get_info()

    book1.is_old()
    book2.is_old()
    book3.is_old()

    pass


def task2():
    
    class BankAccount:
        def __init__(self, account_nr, owner_name, initial_balance = 0):
            self.account_nr = account_nr
            self.owner_name = owner_name
            self.balance = initial_balance

        def deposit(self, amount):
            self.balance += amount
            
        def withdraw(self, amount):
            if amount > self.balance:
                print("Insufficient balance.")
                pass
            self.balance -= amount
            print("Withdraw succesfull")
        
        def get_balance(self):
            print(f"Balance: {self.balance}")
            
        def transfer(self, account, amount):
            if self.balance < amount:
                print("Insufficient balance.")
                pass
            self.balance -= amount
            account.deposit(amount)
            
    account1 = BankAccount("123456789", "Alice", 1000)
    account2 = BankAccount("987654321", "Bob", 500)
    
    account1.get_balance()
    account1.deposit(200)
    account1.get_balance()
    account1.withdraw(150)
    account1.get_balance()
    account2.get_balance()
    account1.transfer(account2, 100)
    account1.get_balance()
    account2.get_balance()

    pass

def task3():

    pass

def task4():
            
    pass

def task5():
    
    pass

def task6():  
        
    pass

def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())