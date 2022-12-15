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

def lexicalAnalisysText(_bagTxt):
    _bagFiltered = []
    for txt in _bagTxt:
        tokens = word_tokenize(txt) # Partimos el texto en tokens

        tokens = [w.lower() for w in tokens] # Recorremos las lista para pasar a minusculas las palabras

        words = [word for word in tokens if word.isalpha()] # Elimina guiones, comillas, puntos...

        stop_words = set(stopwords.words('spanish')) # Seleccionamos el español como palabras de parada
        filteredTxt = [w for w in words if not w in stop_words] # Vamos eliminando todas las palabras sobrantes
        _bagFiltered.append(filteredTxt)

        #porter = PorterStemmer()
        # stemmedTxt = [PorterStemmer().stem(word) for word in filteredTxt] # Stemmer de las diferentes palabras
    return _bagFiltered

def lexicalAnalisysQuery(txt):
    tokens = word_tokenize(txt) # Partimos el texto en tokens

    tokens = [w.lower() for w in tokens] # Recorremos las lista para pasar a minusculas las palabras

    words = [word for word in tokens if word.isalpha()] # Elimina guiones, comillas, puntos...

    stop_words = set(stopwords.words('spanish')) # Seleccionamos el español como palabras de parada
    filteredTxt = [w for w in words if not w in stop_words] # Vamos eliminando todas las palabras sobrantes


    #porter = PorterStemmer()
    # stemmedTxt = [PorterStemmer().stem(word) for word in filteredTxt] # Stemmer de las diferentes palabras
    return filteredTxt