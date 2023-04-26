from io import open
from os import path

def escribir_archivo():
    #La w significa modo escritura, reemplaza los datos que tiene el  archivo por  lo nuevo que se le envia
    #En caso de no querer reemplazar habria que abrir el archivo en modo de lectura r
    archivo = open("texto.txt", "w")
    archivo.write("Hola mundo ")
    archivo.close()
    
def leer_archivo():
    if path.isfile("texto.txt") :
        archivo = open("texto.txt", "r")
        #recupero  la informacion que contiene el archivo
        #texto= archivo.read()
        #readline me  lee una sola linea
        #texto= archivo.readline()
        #readlines me  convierte el texxto en una lista
        texto= archivo.readlines()
        archivo.close()
        print(texto)
    else:
        print("no  existe el archivo")

def agregar_datos():
        if path.isfile("texto.txt") :
                #para actualizar el texto del archivo se utiliza  a
                archivo = open("texto.txt", "a")      
                archivo.write("\nHola mundooooooooooooooo 2")
                archivo.close()
        else:
            print("no  existe el archivo")
            
def modificar_datos():
        if path.isfile("texto.txt") :
                #Abrir en modo lectura y escrittura r+
                archivo = open("texto.txt", "r+")     
                texto=archivo.readlines() 
                texto[1]= "Hola mundooo modificado indice de la lista 1\n"
                #el seek me coloca el puntero en la posicion que quiero el 0 es el inicio
                archivo.seek(0)
                archivo.writelines(texto)
                archivo.close()
        else:
            print("no  existe el archivo")
            
def eliminar_datos():
    #abro el archivo y lo reescribo vacio
        archivo = open("texto.txt", "w")
        archivo.close()

#escribir_archivo()          
#leer_archivo()
#agregar_datos()
#modificar_datos()
eliminar_datos()