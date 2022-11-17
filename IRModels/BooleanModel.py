# Modelo Booleano sobre la recuperacion de informacion en textos
# o documentos en relacion a una query


# Ángel Esquinas Puig
# angelesquinaspuig@gmail.com

# Carga de librerias
import PLN as pln

def vector(): # Creamos los vectores
    bagDocs = []
    doc = []

    for w in bagTxt:
        for t in query: # Creamos las lista de los terminos que aparecen
            if w.__contains__(t):
                doc.append(1)
            else:
                doc.append(0)
        bagDocs.append(doc)
        #doc.clear()
