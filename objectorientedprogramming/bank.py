from  datetime import datetime
class Bank:
    bank_name="sbi"
    def creat_account(self,acno,person_name,min_balance):
        self.acno=acno
        self.personname=person_name
        self.balance=min_balance
#self.bank_name=sbi, can be added if bank is different
    def deposit(self,amount):
        self.balance+=amount

        print(Bank.bank_name,"your ac", self.acno ,"has been credited with",amount,"on",datetime.today(),"available balance",self.balance)

    def withdrawal(self,amount):
        if self.balance>amount :
            self.balance-=amount
            print(Bank.bank_name,"your ac ",self.acno,"has been debited with amt",amount,"on",datetime.today(),"available balance",self.balance )
        else:
            print("transaction cancelled with error code")

    def balance_enquiry(self):
        print(self.balance)

obj=Bank()
obj.creat_account(10001,"sibin",3000)
obj.deposit(1000)
obj.withdrawal(10000)
obj.balance_enquiry()


