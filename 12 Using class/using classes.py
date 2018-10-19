class mainclass:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

    def __repr__(self):
        return '{}  {}'.format(self.Name,self.Age)

emplyee = mainclass('johnny','21')
ceo = mainclass('luther', '34')


