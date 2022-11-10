# Script para recrear un modelo Booleano sobre la recuperacion de informacion
# en textos o documentos en relacion a una query
# Primero haremos PLN sobre los textos ya introducidos, lo que quiere decir que 
# tokenizaremos los textos, pasremos a minusculas y quitaremos signos de puntuacion, guiones...
# ademas filtraremos los textos con un stopWord, para finalmente hacer un stemming


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

tokensTxt1 = word_tokenize(txt1) # Partimos el texto en tokens

# for words in tokensTxt1: # No funciona ns porque
#     tokensTxt1 = words.lower()

tokensTxt1 = [w.lower() for w in tokensTxt1] # Recorremos las lista para pasar a minusculas las palabras
print(tokensTxt1)

words = [word for word in tokensTxt1 if word.isalpha()] # Elimina guiones, comillas, puntos...
print(words)

stop_words = set(stopwords.words('spanish')) # Seleccionamos el español como palabras de parada
filteredTxt1 = [w for w in words if not w in stop_words] # Vamos eliminando todas las palabras sobrantes
print(filteredTxt1)

#porter = PorterStemmer()
stemmedTxt1 = [PorterStemmer().stem(word) for word in filteredTxt1] # Stemmer de las diferentes palabras
print(stemmedTxt1)