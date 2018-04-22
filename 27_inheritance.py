class Parent():
    def print_last_name(self):
        print('Roberts')

class Child(Parent):
    def print_first_name(self):
        print('my first name is Vinh')

        #override the parent function
    def print_last_name(self):
        print('last name of child')

v = Child()
v.print_first_name()
v.print_last_name()