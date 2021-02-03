class Bank:

    def bal_enq(self):
        print("inside balance enquiry")
    def withdrawal(self):
        print("inside withdraw")

    def __deposit(self): #private method
        print("inside deposit")

# class Atm(Bank):
#     pass
# atm=Atm()
# atm.bal_enq()


obj=Bank()
obj._Bank__deposit()  # to call a private method
