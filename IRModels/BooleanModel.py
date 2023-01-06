# Modelo Booleano sobre la recuperacion de informacion en textos
# o documentos en relacion a una query

# Ángel Esquinas Puig
# angelesquinaspuig@gmail.com

# Carga de librerias

def vector(_bagFiltered, _filteredQuery): # Creamos los vectores
    bagDocs = []
    doc = []

    for w in _bagFiltered:
        for t in _filteredQuery: # Creamos las lista de los terminos que aparecen
            if w.__contains__(t):
                doc.append(1)
            else:
                doc.append(0)
        bagDocs.append(doc)
        #doc.clear() # Se me borra bagDocs tbn ns porque
        doc = []
    return bagDocs

def txtRecom(_result):
    recom = []
    for w in range(_result.__len__()):
        print(w)
        # if _result[w].count(1) > _result[w+1].count(1):
        #     recom.insert(0, "texto" + str(w))
        # else:
        #     recom.append("texto" + w)
    # print(recom)