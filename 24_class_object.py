class Enemy:
    life = 3
    #self means
    def attack(self):
        print('ouch!')
        self.life -= 1
    def checkLife(self):
        if self.life <= 0:
            print('i am dead')
        else:
            print(str(self.life) + ' life left')



#object define
enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()

enemy2 = enemy1
enemy2.checkLife()