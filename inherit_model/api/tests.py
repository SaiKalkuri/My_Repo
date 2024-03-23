class Learn:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def action(self):
        print('mention address')
        print(self.name)
    def set_name(self):
        self.name='ram'

obj=Learn('ravan',65)

obj.action()
obj.set_name()


