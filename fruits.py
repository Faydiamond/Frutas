class fruits:
    list=[]

    def add_fruits(self):
        self.fruit=input('Digite su fruta: ')
        self.list.append(self.fruit)
        self.more_fruits()


    def show(self):
        for my_fruits in self.list:
            print (my_fruits)


    def more_fruits(self):
        self.questionn=input('¿Quiere seguir agregando frutas? ')
        if (self.questionn=='si'):
            self.add_fruits()
        elif (self.questionn=='no'):
            self.show()
        else:
            print('Por favor digite si o no!')
            self.add_fruits()




f=fruits()
f.add_fruits()