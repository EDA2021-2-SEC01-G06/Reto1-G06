"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import subList
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
    catalogo= {"artist" : None,
                "artworks": None,}
    catalogo["artist"]= lt.newList(datastructure='SINGLE_LINKED')
    catalogo["artworks"]= lt.newList(datastructure='SINGLE_LINKED')

    return catalogo 

def añadirArt(catalogo, artista):
    lt.addLast(catalogo["artist"], artista)
def añadirObras(catalogo, artwork):
    lt.addLast(catalogo["artworks"], artwork)

def cmpBirthDate(art1,art2):
    fecha1=art1["BeginDate"]
    fecha2=art2["BeginDate"]
    if fecha1<fecha2:
        return True
    else:
        return False 

def cmpDate(date1,date2):
    fecha1=date1["Date"]
    fecha2=date2["Date"]
    if fecha1<fecha2:
        return True
    else:
        return False


def sortArtistsByDate(catalogo):
    sublista=lt.subList(catalogo["artist"],1, lt.size(catalogo["artist"]))
    sublista=sublista.copy()
    lista_ord=""
    lista_ord=sa.sort(sublista, cmpBirthDate)
    return lista_ord 

def sortFecha(catalogo, size):
    sublista= lt.subList(catalogo["artworks"],1,size)
    sublista=sublista.copy()
    lista_ord=""
    lista_ord=sa.sort(sublista, cmpDate)
    return lista_ord



# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento