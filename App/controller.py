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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def initCatalog():
    catalogo=model.newCatalog()
    return catalogo 

def loadData(catalogo):
    loadArtist(catalogo)
    loadArtworks(catalogo)
    sortArtistsByBirth(catalogo)
    sortArtworksByDate(catalogo)    

def loadArtist(catalogo):
    artsfile= cf.data_dir +"archivoA.csv"
    input_file= csv.DictReader(open(artsfile, encoding="utf-8"))
    for artist in input_file:
        model.añadirArt(catalogo, artist)

def loadArtworks(catalogo):
    artworkfile= cf.data_dir +"archivoO.csv"
    input_file= csv.DictReader(open(artworkfile, encoding="utf-8"))
    for artwork in input_file:
        model.añadirArt(catalogo, artwork)
        
def sortArtistsByBirth(catalogo):
    model.sortArtistsByDate(catalogo)

def sortArtworksByDate(catalogo,size):
    model.sortFecha(catalogo,size)
# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
