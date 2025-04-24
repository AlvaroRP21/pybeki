# Crea la clase Contador, tendra una propiedad valor = 0
# Tendra un metodo llamado incrementar que sumara 1 a valor
# Tendra un metodo llamado decrementar que restara 1 a valor
# Tendra un metodo llamado mostrar que mostrara un mensaje de cuanto es nuestro valor
# Tendra un metodo llamado incrementar_aleatorio que sumara un numero aleatorio entre 1 y 6 a valor


class Contador:
    def __init__(self, incrementar, decrementar, mostrar, incrementar_aleatorio):
        self._incrementar = incrementar
        self._decrementar = decrementar
        self._mostrar = mostrar
        self._incrementar_aleatorio = incrementar_aleatorio
        

    @property
    def incrementar(self):
        return self._incrementar
    
    @property
    def decrementar(self):
        return self._decrementar
    
    @property
    def mostrar(self):
        return self._mostrar
    
    @property
    def incrementar_aleatorio(self):
        return self._incrementar_aleatorio
    

    @incrementar.setter
    def incrementar(self, incre):
        self._incrementar = incre

    @decrementar.setter
    def decrementar(self, decre):
        self._decrementar = decre

    @mostrar.setter
    def mostrar(self, mos):
        self._mostrar = mos

    @incrementar_aleatorio.setter
    def incrementar_aleatorio(self, inal):
        self._incrementar_aleatorio = inal

c = Contador(0, 0, )
c.incrementar = 4
c.decrementar = 
c.mostrar = 
c.incrementar_aleatorio = 
