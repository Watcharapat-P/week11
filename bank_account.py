class AccountDB:
    def __init__(self):
        self.account_database = []

    def search(self, account_num):
        for account in self.account_database:
            if account.num == account_num:
                return account
        print(f'{account_num} invalid account number; nothing to be shown for.')

    def insert(self, account):
        for a in self.account_database:
            if a.num == account.num:
                print(f'{account.num} account number {account.num} already exists.')
                return False
        self.account_database.append(account)

    def __str__(self):
        s = ''
        for account in self.account_database:
            s += str(account) + ", "
        return s

    def delete(self, account_num):
        for account in self.account_database:
            if account.num == account_num:
                self.account_database.remove(account)
                print(f'{account.num} deleted.')


class Account:
    def __init__(self, num, type, account_name, balance):
        self.num = num
        self.type = type
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Depositing", amount, "to", self.num)

    def withdraw(self, amount):
        if self.balance >= amount:
            print("Withdrawing", amount, "from", self.num)
            self.balance -= amount
        else:
            print("withdrawal amount", amount, "exceeds the balance of", self.balance, "for", self.num, "account.")

    def __str__(self):
        print(f'Showing details for {self.num}')
        return '{' + str(self.num) + ',' + str(self.type) + ',' + str(self.account_name) + ',' + str(self.balance) + '}'


account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0004", "saving", "David Wood", 4000)
my_account_DB = AccountDB()
my_account_DB.insert(account1)
my_account_DB.insert(account2)
my_account_DB.insert(account3)
my_account_DB.insert(account4)
my_account_DB.insert(account5)
print(my_account_DB)
my_account_DB.search("0003").deposit(50)
print(my_account_DB.search("0003"))
my_account_DB.search("0003").withdraw(25)
print(my_account_DB.search("0003"))
my_account_DB.delete("0003")
print(my_account_DB.search("0003"))

