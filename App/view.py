"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def initCatalog():
    return controller.initCatalog()
def loadArts(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadArtist(catalog)
def loadObras(catalog):
    controller.loadArtworks(catalog)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronologicamente los artistas")
    print("3- Listar cronologicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalogo=initCatalog()
        loadArts(catalogo)
        loadObras(catalogo)
        print("Se cargo exitosamente la informacion")
        print("Artistas cargados: "+str(lt.size(catalogo["artist"])))
        print("Artworks cargados: "+str(lt.size(catalogo["artworks"])))

    elif int(inputs[0]) == 2:
        print("Los artistas ordenados cronologicamente son:")
    elif int(inputs[0]) == 3:
        print("Las adquisiciones ordenadas cronologicamente son:")
    elif int(inputs[0]) == 4:
        print("Las obras clasificadas de un artista por tecnica son:")
    elif int(inputs[0]) == 5:
        print("Las obras clasificadas por la nacionalidad de sus creadores son:")
    elif int(inputs[0]) == 6:
        print("Obras transportadas al departamento:")
    else:
        sys.exit(0)
sys.exit(0)
