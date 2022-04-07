from abc import ABC, abstractmethod

class estrategiaPago(ABC):

    @abstractmethod
    def pagar(self):
        pass

    @abstractmethod
    def getNumeroFactura(self):
        pass
