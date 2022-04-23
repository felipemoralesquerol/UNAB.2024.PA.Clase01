from abc import ABC, abstractmethod

class AbstractClass(ABC):

  @abstractmethod
  def abstractMethod(self):
    return

class ConcreteClass(AbstractClass):
  def __init__(self):
    self.me = "me"
 
  def abstractMethod(self):
    print('definido')


# The following would raise a TypeError complaining 
# abstractMethod is not implemented

# Comentar para hacer pruebas
c = ConcreteClass()  
c.abstractMethod()

# Comentar para hacer pruebas
c = AbstractClass()  
c.abstractMethod()

