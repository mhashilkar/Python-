#class & object

class Person:
    __name =''
    __email = ''

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

brad = Person()
brad.set_name('Suranjan')
brad.set_email('suranjanrock12@gmail.com')

print(brad.get_name())
print(brad.get_email())
