from abc import ABC, abstractmethod

class Cloth(ABC):

    def __init__(self,param):
        self.param = param
    
    @abstractmethod
    def calculate_cloth(self):
        pass


class Coat(Cloth):
    @property
    def calculate_cloth(self):
        print(f'Для пальто размера {self.param} требуется {(self.param/6.5)+0.5:.2f} ткани')


class Suit(Cloth):
    @property
    def calculate_cloth(self):
        print(f'Для костюма для роста {self.param} требуется {(2 * self.param)+0.3:.2f} ткани')

coat = Coat(50)
coat.calculate_cloth
suit = Suit(175)
suit.calculate_cloth
