class Person:
    def __init__(self,fname,lname,email):
        self.fname=fname
        self.lname=lname
        self.email=email

    def print(self):
        print("FirstName-",self.fname)
        print("LastName-",self.lname)
        print("Email-",self.email)

    def fullname(self):
        return self.fname

class Customer(Person):
    def __init__(self,cno,fname,lname,email):
        Person.__init__(self,fname,lname,email)
        self.cno=cno

    def print(self):
        Person.print(self)
        print("Customernumber-",self.cno)

class Employee(Person):
    def __init__(self,PAN,fname,lname,email):
        Person.__init__(self, fname, lname, email)
        self.PAN=PAN

    def print(self):
        Person.print(self)
        print("PAN NO-",self.PAN)



def main():
    cusobj=Customer(1002,"JOHN","WICK","thewicked@gmail.com")
    empobj=Employee("GHX120210","JACKTHE","RIPPER","ripperjack@gmail.com")
    print("\n\n")
    print("customer")
    cusobj.print()
    print("-------------------------------")
    print("EMPLOYEE")
    empobj.print()



if __name__=="__main__":
    main()
