class Informacion:
    def mi_lista(self):
        lista_nomperro=["body", "dolar", "elvis"]
        for x in lista_nomperro:
            print(x)
        
    def mitupla(self):
        razasperre = ("pug", "chihuahua", "husky")
        for x in razasperre:
            print(x)
    def conjuperre(self):
        conperres ={"blanquito", "cafesito", "grisesito"}
        for x in conperres:
            print(x)
    def dicci(self):
        dict_perros = {
            "pug :": "Elvis Canserbero Miracomida",
            "chihuahua: ": "body",
            "husky: ": "dolar"
        }
        for x,y in dict_perros.items():
            print(x, y)

datos=Informacion()
print("listado de nombres---------------")
datos.mi_lista()
print("tuplas-----------------")
datos.mitupla()
print("conjuntos-----------------")
datos.conjuperre()
print("diccionarios-----------------")
datos.dicci()
