# # 2)
# class student:
#    def  __init__(self,rollno,name,mark1,mark2,mark3):
#        self.rollno=rollno
#        self.name=name
#        self.mark1=mark1
#        self.mark2=mark2
#        self.mark3=mark3
#        self.total=300
#        print("Student details are: \nName:{0} \nrollno:{1}\n marks={2},{3},{4}".format(self.name,self.rollno,self.mark1,self.mark2,self.mark3))
#    def percen(self):
#        self.percentage=((self.mark1+self.mark2+self.mark3)/self.total)*100
#        print("Percentage=",self.percentage)

# name=(input("enter your name:"))
# roll=int(input("enter your roll no: "))
# mark1,mark2,mark3=(int(x) for x in input("Enter your marks: ").split())
# student1=student(name,roll,mark1,mark2,mark3)
# student1.percen()

# # 1)
# class bank:
#     def details(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.amount=amount
#     def withdraw(self,cash):
#         self.cash=cash
#     def show_balance(self,money):
#         self.money=money
#     def display(self):
#         print("empolyee name is {0} and  balalnce in account is{1}".format(self.name,self.balance))
#         print("he deposited",self.amount)
#         print("he wthdrawed",self.cash)
#         print("his main balance is",self.money)
# b=bank()
# b.details('rahul',98000)
# b.deposit(1000)
# b.withdraw(35000)
# b.show_balance(76000)
# b.display()
# b1=bank()
# b1.details('snax',80000)
# b1.deposit(10000)
# b1.withdraw(85000)
# b1.show_balance(46000)
# b1.display()