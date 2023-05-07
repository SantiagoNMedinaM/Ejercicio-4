class Ventana:
    __titulo=""
    __ejeXsi=0
    __ejeYsi=0
    __ejeXid=0
    __ejeYid=0
    
    def __init__(self, titulo="",ejexsi=0,ejeysi=0,ejexid=100,ejeyid=100):
        self.__titulo = titulo
        self.__ejeXsi = max(0,ejexsi)
        self.__ejeYsi = max(0,ejeysi)
        self.__ejeXid = min(500,ejexid)
        self.__ejeYid = min(500,ejeyid)

    def getTitulo(self):
        return self.__titulo
    def mostrar(self):
        print("Ventana: {}, con ejes superiores izquierdos X: {} e Y: {} y con ejes inferiores derechos X: {} e Y: {}".format(self.__titulo, self.__ejeXsi, self.__ejeYsi, self.__ejeXid, self.__ejeYid))
    def alto(self):
        h = self.__ejeYid - self.__ejeYsi
        return h
    def ancho(self):
        anc = self.__ejeXid - self.__ejeXsi
        return anc
    def moverDerecha(self,v):
        if self.__ejeXid + v > 500:
            v = 500 - self.__ejeXid
        self.__ejeXid += v
        self.__ejeXsi += v
    def moverIzquierda(self,p):
        if self.__ejeXsi - p < 0:
            p = self.__ejeXsi
        self.__ejeXid -= p
        self.__ejeXsi -= p  
    def bajar(self, b=0):
        if self.__ejeYid + b >500:
            b = 500 - self.__ejeYid
        self.__ejeYid += b
        self.__ejeYsi += b
    def subir(self,s=0):
        if self.__ejeYsi - s < 0:
            s = self.__ejeYsi
        self.__ejeYsi -= s
        self.__ejeYid -= s
