# Menu de principal del programa

# Ángel Esquinas Puig
# angelesquinaspuig@gmail.com

# Carga de librerias
import BooleanModel as bm
import PLN as pln
import FileSelection as fl

bagRawText = []

seguir = True

while seguir:
    num = int(input('---MENU---\n 1- Seleccionar textos\n 2- Modelo Booleano\n 3- Modelo Espacio Vectorial\n 4- Salir\n'))
    while num < 1 or num > 4: # Mientras meta un numero mayor o menos que los cursos posible se lo vuelve a preguntar
        print("\nAccion incorrecto vuelva a introducirlo \n")
        num = int(input('¿Que accion quieres consultar?: '))

    if num == 1:
        bagRawText = fl.listTxt()
    elif num == 2:
        query = input('Introduce la query: ')
        bagFiltered = pln.lexicalAnalisys(bagRawText)
        filteredQuery = pln.lexicalAnalisysQuery(query)
        result = bm.vector(bagFiltered, filteredQuery)
        print(bagFiltered)
    elif num == 3:
        print('Putooooo')
    else:
        seguir = False