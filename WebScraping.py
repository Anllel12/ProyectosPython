import requests
from bs4 import BeautifulSoup

# WEB SCRAPING
page = requests.get("https://universidadeuropea.com/grado-ingenieria-informatica-madrid/")
html = BeautifulSoup(page.text, "html.parser")
tablas = html.find_all('table')

def seleccionarTabla(x):
    for row in tablas[x].tbody.find_all('tr'):
            info = row.find_all('td')
            print('Asignatura - ' + info[0].text.strip() + '  Créditos: ' + info[1].text.strip() + ' Tipo - ' + info[2].text.strip())


# MENU
def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entre el 1 y el 5 (5 para salir): "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

salir = False
opcion = 0
 
while not salir:
    print ("\n1. Primer curso")
    print ("2. Segundo curso")
    print ("3. Tercer curso")
    print ("4. Cuarto curso")
    print ("5. Salir")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Primero:")
        seleccionarTabla(1)
    elif opcion == 2:
        print ("Segundo:")
        seleccionarTabla(2)
    elif opcion == 3:
        print ("Tercero:")
        seleccionarTabla(3)
    elif opcion == 4:
        print ("Cuarto:")
        seleccionarTabla(4)
    elif opcion == 5:
        print ("Adios!")
        salir = True
    else:
        print ("Introduce un numero entre el 1 y el 5 (5 para salir): ")