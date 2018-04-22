class Father():
    def name_father(self):
        print('name parent')


class Mother():
    def name_mother(self):
        print('name mother')

class Child(Father, Mother):
    #dont want to do anything
    pass

    #def name_child(self):
     #   print('child name')



v = Child()
v.name_father()
v.name_mother()
#v.name_child()