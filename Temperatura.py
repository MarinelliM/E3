class Registro:
    __temperatura= 0.0
    __humedad= 0.0
    __presion= 0.0

    def __init__(self, temperatura, humedad, presion_atmosferica) -> None:
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion_atmosferica
        pass

    def getvalores(self):
        return print('Los valores de temperatura son de {}, los de humedad son {} y los de presion son de {}' .format(self.__temperatura, self.__humedad, self.__presion))
    
    def getemp(self):
        return self.__temperatura
   
    def gethum(self):
        return self.__humedad
    
    def getpres(self):
        return self.__presion
