import re
palabras = [["Pixel", "Civil", "Paco", "Hijo", "Toxico", "Camion", "Clave", "Ximena", "Damian", "Lili", "Claudia", "Medallon", "Clima"],
            [0,0,0,0,0,0,0,0,0,0,0,0,0]]
simbolos = [["I", "V", "X", "L", "C", "D", "M"],
            [1,5,10,50,100,500,1000]]
palabrasFiltradas = []
def filtrarPalabras():
    #Dejar solamente los caracteres romanos de cada palabra
    for palabra in palabras[0]:
        palabra = palabra.upper()
        palabrasFiltradas.append("".join([c for c in palabra if c in simbolos[0]]))

def esRomano(str):
    # Expresion regular para numeros romanos validos
    patron = re.compile(r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
    
    # Comprobar si el string coincide con el patron
    return bool(patron.match(str))

def masDeTresSimbolos(str):
    #checar si un string tiene 3 o mas duplicados consecutivos
    consecutivos = 0
    c_ant = ""
    for c in str:
        if c_ant == c:
            consecutivos += 1
        else:
            consecutivos = 0
            c_ant = c
    return consecutivos > 2

def evaluarPalabras():
    restasValidas = ["IV","IX","XL","XC","CD","CM"] 
    for i,palabra in enumerate(palabrasFiltradas):
        subActual = ""
        letraSig = ""
        sumaActual = 0

        for j,letra in enumerate(palabra):
            subActual += letra
            # print(f"Suma Antes: {sumaActual}")
            # print(f"{subActual} Romano? {esRomano(subActual)}")
            valorLetra = simbolos[1][simbolos[0].index(letra)]
            if j == 0 and esRomano(letra):
                sumaActual += valorLetra
            if j < len(palabra)-1:
                letraSig = palabra[j+1]
                valorLetraSig = simbolos[1][simbolos[0].index(letraSig)]
            if j < len(palabra)-1 and esRomano(subActual+letraSig):
                # Suma
                if valorLetra > valorLetraSig:
                    sumaActual += valorLetraSig
                # Resta
                letra = "I"
                letraSig = "X"
                if valorLetraSig > valorLetra and (letra + letraSig) in restasValidas:
                    sumaActual -= valorLetra
                    sumaActual += valorLetraSig - valorLetra
                # Suma si no van mas de 3 simbolos iguales seguidos
                if valorLetra == valorLetraSig and not masDeTresSimbolos(subActual.join(letraSig)):
                    sumaActual += valorLetraSig
            # print(f"Suma After: {sumaActual}")
            palabras[1][i] = sumaActual        
            
def detectarRomanos():
    filtrarPalabras()
    evaluarPalabras()
    for i,palabra in enumerate(palabras[0]):
        print(f"{palabra} -> {palabrasFiltradas[i]} -> {palabras[1][i]}")

detectarRomanos()