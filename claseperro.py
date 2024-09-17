print ("clases version 2 el constructor")

class perro:
    def __init__(self,color,edad):
    # funcion constructor
        self.color=color
        self.edad=edad
    # funciones creadas por el usuario
    def muerde(self):
            print("chale el perro me mordio")
    def chatperro(self,mensaje):
            print(f"chat perro: {mensaje}")
    def chatperra(self,mensajepe):
            print(f"chat perra: {mensajepe}")
    def datos(self):
            print(f"color {self.color} edad {self.edad}")    
# crear el objeto
chihuas=perro("negro",2)
# llamadas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("hola canina")
chihuas.chatperra("hola boby")
chihuas.chatperro("quieres ser mi pickashu ?")
chihuas.chatperra("grrrrrru........")