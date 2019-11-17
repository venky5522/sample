class cust:
    cbname = "HDFC"
    def __init__(self,cname,cacno,cbal,caddr):
        self.cname = cname
        self.cacno = cacno
        self.cbal = cbal
        self.caddr = caddr
    def deposit(self,damt):
        self.cbal = self.cbal+damt
    def withdraw(self,wamt):
        self.cbal = self.cbal-wamt
    def display(self):
        print(self.cname)
        print(self.cacno)
        print(self.cbal)
        print(self.caddr)
        print(cust.cbname)
c1 = cust("venkatesh",101,10000,"bangalore")
print(c1)
c1.display()
c1.deposit(10000)
c1.display()
c1.withdraw(5000)
c1.display()