# Exercise 7.10: HelloWorld.py


class HelloWorld:
    def __init__(self, g=None):
        self.g = g
                
    def __str__(self):
        return 'Hello, World!'




a = HelloWorld('dfadf')
print a