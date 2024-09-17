class informacion: 
    
    def mi_lista(self):
        lista_nomperros=["boby","dollar","fany"]
        for x in lista_nomperros:
            print(x)
        
    def mi_tupla(self):
        tupla_tenis = ("nike","jordan","adidas")
        for b in tupla_tenis:
            print(b)
        
    def mi_set(self):
        set_carros = {"mustang","camaro","bocho"}
        for a in set_carros:
            print(a)
        
    def mi_diccionario(self):
        thisdic = {
    "piña": "fresa",
    "limon": "platano",
    "mango": "manzana"
}
        for x,y in thisdic.items():
            print(x,y)    
        
#creando el objeto 

datos=informacion()
print("listado de nombre de perros")
datos.mi_lista()
print("")
print("tupla de marcas de tenis")
datos.mi_tupla()
print("")
print("conjunto de carros")
datos.mi_set()
print("")
print("mi diccionario de frutas")
datos.mi_diccionario()