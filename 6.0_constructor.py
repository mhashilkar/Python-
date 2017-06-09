#class & object
# with constructor

class Person:
    __name =''
    __email = ''

    def __init__(self,name,email):# constructor
        self.__name = name
        self.__email = email


    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def toString(self):
        return '{} can be contacted at {}'.format(self.__name,self.__email)

#brad = Person('Suranjan Mhashilkar','suranjanrock12@gmail.com')
#print(brad.toString())

class Customer(Person): # inheritans Person is inherited
    __balance = 0

    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def toString(self):
        return '{} has a balance of {} can be contacted by {}'.format(self.__name,self.__balance,self.__email)

john = Customer('Suranjan Mhashilkar','suranjanrock12@gamil.com',20000)
 # to change the balance
john.set_balance(400)
print(john.toString())
