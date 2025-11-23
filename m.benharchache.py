# CLASS TRANSACTION
 
class Transaction:
    def __init__(self, ttype, amount, source=None, destination=None):
        self.type = ttype                   
        self.amount = amount               
        self.source = source                
        self.destination = destination     

    def __str__(self):
        if self.type == "credit":
            return f"Credited +{self.amount} DA"
        elif self.type == "debit":
            return f"Debited -{self.amount} DA"
        else:  
            return f"Transfer {self.amount} DA from Account {self.source.get_code()} to Account {self.destination.get_code()}"
        

 
#  CLASS CLIENT
 
class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.accounts = []

    def get_CIN(self): return self.__CIN
    def get_firstName(self): return self.__firstName
    def get_lastName(self): return self.__lastName
    def get_tel(self): return self.__tel
    def set_tel(self, tel): self.__tel = tel

    def display(self):
        print(f"CIN: {self.__CIN}, Name: {self.__firstName} {self.__lastName}, Tel: {self.__tel}")

    def displayAccounts(self):
        print(f"\nAccounts of {self.__firstName} {self.__lastName}:")
        if not self.accounts:
            print("This client has no accounts.")
        else:
            for acc in self.accounts:
                print(f"  -> Account {acc.get_code()} : {acc.get_balance()} DA")

 
# CLASS ACCOUNT
 
class Account:
    __nbAccounts = 0

    def __init__(self, owner):
        Account.__nbAccounts += 1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = owner

        self.__transactions = []    

        owner.accounts.append(self)

    def get_code(self): return self.__code
    def get_balance(self): return self.__balance
    def get_owner(self): return self.__owner

     
    # CREDIT
    
    def credit(self, amount, sourceAccount=None):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return

        self.__balance += amount

        if sourceAccount is None:
          
            t = Transaction("credit", amount, None, self)
        else:
             
            t = Transaction("transfer", amount, sourceAccount, self)

        self.__transactions.append(t)

    
    # DEBIT
    
    def debit(self, amount, destinationAccount=None):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return

        if self.__balance < amount:
            print("Error: Insufficient balance!")
            return

        self.__balance -= amount

        if destinationAccount is None:
            t = Transaction("debit", amount, self, None)
        else:
            t = Transaction("transfer", amount, self, destinationAccount)

        self.__transactions.append(t)

     
    # TRANSFER
    
    def transfer(self, amount, targetAccount):
        # Withdraw from source
        if self.__balance < amount:
            print("Error: Insufficient balance!")
            return

        # Debit (source)
        self.debit(amount, targetAccount)

        # Credit (destination)
        targetAccount.credit(amount, self)

   
    # DISPLAY ACCOUNT
     
    def display(self):
        print(f"Account Code : {self.__code}")
        print(f"Owner        : {self.__owner.get_firstName()} {self.__owner.get_lastName()}")
        print(f"Balance      : {self.__balance} DA")
        
    
    # DISPLAY TRANSACTIONS
    
    def displayTransactions(self):
        print(f"\nTransaction history of account {self.__code}:")
        if not self.__transactions:
            print("No transactions.")
        else:
            for t in self.__transactions:
                print(" -", t)

    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)