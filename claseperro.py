print("clases version 2 el constructor")
class perro: 
    def __init__(self, color, edad) -> None:
        self.color=color
        self.edad=edad

    def morder(self):
        print("ostia, el perro me ha mordido, ¡cojones!")
        
    def chatperro(self, mensaje):
        print(f"chat perro :{mensaje}")

    def chatperra(self, mensajepe):
        print(f"chat perra :{mensajepe}")

    def datos(self):
        print(f"color : {self.color} edad:{self.edad}")  
chihuas=perro("negro",2)
chihuas.datos()
chihuas.morder()
chihuas.chatperro("hola, canina")
chihuas.chatperra("hi, body")
chihuas.chatperro("quieres ser mi wouf, wouf?")
chihuas.chatperra("grrrrrr....")
