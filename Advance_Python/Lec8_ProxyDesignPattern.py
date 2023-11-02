from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        ''' Interface Method '''
    
class Person (IPerson):
    def person_method(self):
        print ("I am a person!")
        
class ProxyPerson (IPerson):
    def __init__(self):
        self.person = Person()
    def person_method(self):
        print("I am the proxy functionality!")
        self.person.person_method()