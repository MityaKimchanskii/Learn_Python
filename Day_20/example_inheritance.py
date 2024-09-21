class Animal:
    def __init__(self):
        self.num_eyes = 3

    def breathe(self):
        print('Breathe animal')



class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print('hello nemo')

nemo = Fish()
nemo.swim()
nemo.breathe()