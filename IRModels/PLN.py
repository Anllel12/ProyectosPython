# Primero haremos PLN sobre los textos ya introducidos, lo que quiere decir que 
# tokenizaremos los textos, pasaremos a minusculas y quitaremos signos de puntuacion, guiones...
# ademas filtraremos los textos con un stopWord, para finalmente hacer un stemming

# Ángel Esquinas Puig
# angelesquinaspuig@gmail.com


# Carga de librerías
import nltk
import re
import string 

#nltk.download()
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

txt1 = 'El perro de San Roque no tiene rabo, - porque Ramón Ramírez se lo ha cortado.'
txt2 = 'Dicen que perro ladrador, poco mordedor.'
txt3 = 'Hay que comprarle un mordedor al perro porque es bueno para el dolor.'
txt4 = 'El labrador es un perro muy noble, no se considera mordedor.'
txt5 = 'El niño de Ramón es muy bueno.'
txt6 = 'La niña aprobó el examen.'
txt7 = 'Ese jugador es muy perro. No me parece bueno ese gesto.'
query = 'El perro coge el mordedor'

def lexicalAnalisys(txt):
    tokens = word_tokenize(txt) # Partimos el texto en tokens

    tokens = [w.lower() for w in tokens] # Recorremos las lista para pasar a minusculas las palabras

    words = [word for word in tokens if word.isalpha()] # Elimina guiones, comillas, puntos...

    stop_words = set(stopwords.words('spanish')) # Seleccionamos el español como palabras de parada
    filteredTxt = [w for w in words if not w in stop_words] # Vamos eliminando todas las palabras sobrantes
    return filteredTxt

    #porter = PorterStemmer()
    # stemmedTxt = [PorterStemmer().stem(word) for word in filteredTxt] # Stemmer de las diferentes palabras
    # print(stemmedTxt)

bagTxt = [] # Lista de listas para mayor dinamismo
bagTxt.append(lexicalAnalisys(txt1))
bagTxt.append(lexicalAnalisys(txt2))

query = lexicalAnalisys(query)

bagDocs = []
doc = []

for w in bagTxt:
    for t in query: # Creamos las lista de los terminos que aprecen
        if w.__contains__(t):
            doc.append(1)
        else:
            doc.append(0)
    bagDocs.append(doc)
    #doc.clear() 

print(bagDocs)