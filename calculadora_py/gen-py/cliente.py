from calculadora import Calculadora

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket("localhost", 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Calculadora.Client(protocol)

transport.open()

print("\n-------------------MENÚ DE LA CALCULADORA-------------------\n")
print("OPERACIONES BÁSICAS:                 '0'\n")
print("OPERACIONES TRIGONOMÉTRICAS:         '1'\n")
print("OTRAS OPERACIONES:                   '2'\n")
print("OPERACIONES CON VECTORES:            '3'\n")
print("OPERACIONES CON MATRICES:            '4'\n")
print("------------------------------------------------------------\n")

tipo_operacion = input("Introduzca el tipo de operación escogido: ")

# OPERACIONES BÁSICAS:
if tipo_operacion == "0":
    # MENÚ:
    print("\n------BIENVENIDO/A A LA OPCIÓN DE OPERACIONES BÁSICAS-------\n")
    print("A continuación, escoja una de las siguientes operaciones:\n")
    print("     [+] SUMA\n")
    print("     [-] RESTA\n")
    print("     [x] MULTIPLICACIÓN\n")
    print("     [/] DIVISIÓN\n")

    # LECTURA DEL OPERADOR:
    operador = input("Introduzca el operador seleccionado: ")

    while operador not in ["+", "-", "x", "/"]:
        print("\nERROR: El operador proporcionado por parámetro no es correcto.")
        operador = input("Introduzca el operador seleccionado: ")
    
    # LECTURA DEL PRIMER VALOR:
    lectura = input("\nIntroduzca el primer valor de la operación: ")
    num1 = float(lectura)

    # LECTURA DEL SEGUNDO VALOR:
    lectura = input("\nIntroduzca el segundo valor de la operación: ")
    num2 = float(lectura)
    
    # RESULTADO:
    if operador == "+":
        resultado = client.suma(num1, num2)
    elif operador == "-":
        resultado = client.resta(num1, num2)
    elif operador == "x":
        resultado = client.producto(num1, num2)
    else:
        if(num2 == 0):
            print("\nERROR: El divisor no puede ser 0.\n")
            exit()
        else:
            resultado = client.division(num1, num2)

    print("\nOPERACIÓN A REALIZAR: " + str(num1) + " " + operador + " " + str(num2) + " = " + str(resultado))

# OPERACIONES TRIGONOMÉTRICAS:
elif tipo_operacion == "1":
    # MENÚ:
    print("\n--BIENVENIDO/A A LA OPCIÓN DE OPERACIONES TRIGONOMÉTRICAS---\n")
    print("A continuación, escoja una de las siguientes operaciones:\n")
    print("     [SIN]  SENO\n")
    print("     [COS]  COSENO\n")
    print("     [TAN]  TANGENTE\n")
    print("     [ASIN] ARCOSENO\n")
    print("     [ACOS] ARCOCOSENO\n")
    print("     [ATAN] ARCOTANGENTE\n")

    # LECTURA DEL OPERADOR:
    op = input("Introduzca el operador seleccionado: ")
    operador = op.upper()

    while operador not in ["SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN"]:
        print("\nERROR: El operador proporcionado por parámetro no es correcto.")
        operador = input("Introduzca el operador seleccionado: ")
    
    # LECTURA DEL VALOR:
    lectura = input("\nIntroduzca el valor: ")
    num1 = float(lectura)
    
    # RESULTADO:
    if operador == "SIN":
        resultado = client.seno(num1)
    elif operador == "COS":
        resultado = client.coseno(num1)
    elif operador == "TAN":
        resultado = client.tangente(num1)
    elif operador == "ASIN":
        resultado = client.arcoseno(num1)
    elif operador == "ACOS":
        resultado = client.arcocoseno(num1)
    else:
        resultado = client.arcotangente(num1)

    print("\nOPERACIÓN A REALIZAR: " + operador + "( " + str(num1) + " ) = " + str(resultado))

# OTRAS OPERACIONES:
elif tipo_operacion == "2":
    # MENÚ:
    print("\n------BIENVENIDO/A A LA OPCIÓN DE OTRAS OPERACIONES--------\n")
    print("A continuación, escoja una de las siguientes operaciones:\n")
    print("     [SQRT]  RAÍZ\n")
    print("     [POW]   POTENCIA\n")
    print("     [LOG]   LOGARITMO\n")
    print("     [MOD]   MÓDULO\n")
    print("     [%]     PORCENTAJE\n")

    # LECTURA DEL OPERADOR:
    op = input("Introduzca el operador seleccionado: ")
    operador = op.upper()

    while operador not in ["SQRT", "POW", "LOG", "%", "MOD"]:
        print("\nERROR: El operador proporcionado por parámetro no es correcto.")
        operador = input("Introduzca el operador seleccionado: ")
    
    # LECTURA DE VALORES:
    lectura = input("\nIntroduzca el valor: ")
    num1 = float(lectura)
        
    # RESULTADO:
    if operador == "SQRT":
        resultado = client.raiz_cuadrada(num1)
        print("\nOPERACIÓN A REALIZAR: " + operador + "( " + str(num1) + " ) = " + str(resultado))
    elif operador == "POW":
        lectura = input("\nIntroduzca la potencia: ")
        num2 = float(lectura)
        resultado = client.potencia(num1, num2)
        print("\nOPERACIÓN A REALIZAR: " + operador + "( " + str(num1) + " , " + str(num2) + " ) = " + str(resultado))
    elif operador == "LOG":
        lectura = input("\nIntroduzca la base: ")
        num2 = float(lectura)
        resultado = client.logaritmo(num1, num2)
        print("\nOPERACIÓN A REALIZAR: " + operador + "( " + str(num1) + " , " + str(num2) + " ) = " + str(resultado))
    elif operador == "%":
        lectura = input("\nIntroduzca el total: ")
        num2 = float(lectura)
        resultado = client.porcentaje(num1, num2)
        print("\nOPERACIÓN A REALIZAR: (" + str(num1) + " / " + str(num2) + ") * 100 = " + str(resultado) +"%")
    elif operador == "MOD":
        lectura = input("\nIntroduzca el segundo valor: ")
        num2 = float(lectura)
        resultado = client.modulo(num1, num2)
        print("\nOPERACIÓN A REALIZAR: " + str(num1) + " % " + str(num2) + " = " + str(resultado))


# OPERACIONES CON VECTORES:
elif tipo_operacion == "3":
    # MENÚ:
    print("\n---BIENVENIDO/A A LA OPCIÓN DE OPERACIONES CON VECTORES---\n")
    print("A continuación, escoja una de las siguientes operaciones:\n")
    print("     [+]  SUMA\n")
    print("     [-]  RESTA\n")
    print("     [o]  PRODUCTO ESCALAR\n")
    print("     [x]  PRODUCTO VECTORIAL\n")
    print("     [/]  DIVISIÓN VECTOR/REAL\n")

    # LECTURA DEL OPERADOR:
    operador = input("Introduzca el operador seleccionado: ")

    while operador not in ["+", "-", "o", "x", "/"]:
        print("\nERROR: El operador proporcionado por parámetro no es correcto.")
        operador = input("Introduzca el operador seleccionado: ")
    
    # LECTURA DE VALORES DEL PRIMER VECTOR:
    v1 = list()
    print("\nIntroduzca los valores del primer vector, separados por un espacio.")
    print("En el momento en el que haya finalizado, pulse ENTER.")
    
    lectura = input()
    vector = lectura.split()
    
    for n in vector:
        v1.append(float(n))

    # LECTURA DE VALORES DEL SEGUNDO VECTOR:
    if operador != "/":
        v2 = list()
        print("\nIntroduzca los valores del segundo vector, separados por un espacio.")
        print("En el momento en el que haya finalizado, pulse ENTER.")
        
        lectura = input()
        vector = lectura.split()
        
        for n in vector:
            v2.append(float(n))
    else:
        lectura = input("\nIntroduzca el valor del divisor: ")
        v2 = float(lectura)
    
    # COMPROBACIÓN DE TAMAÑOS:
    if operador in ["+", "-", "o"] and len(v1) != len(v2):
        print("\nERROR: El tamaño de ambos vectores debe ser el mismo.")
        exit()
    elif operador == "x" and (len(v1) != 3 or len(v2) != 3):
        print("\nERROR: El tamaño de ambos vectores debe ser 3.")
        exit()
        
    # RESULTADO:
    if operador == "+":
        resultado = client.suma_vectores(v1, v2)
    elif operador == "-":
        resultado = client.resta_vectores(v1, v2)
    elif operador == "o":
        resultado = client.producto_escalar(v1, v2)
    elif operador == "x":
        resultado = client.producto_vectorial(v1, v2)
    else:
        resultado = client.division_vector_real(v1, v2)
    
    print("\nOPERACIÓN A REALIZAR: " + str(v1) + " " + operador + " " + str(v2) + " = " + str(resultado))

# OPERACIONES CON MATRICES:
elif tipo_operacion == "4":
    # MENÚ:
    print("\n---BIENVENIDO/A A LA OPCIÓN DE OPERACIONES CON MATRICES---\n")
    print("A continuación, escoja una de las siguientes operaciones:\n")
    print("     [+]  SUMA\n")
    print("     [-]  RESTA\n")
    print("     [x]  MULTIPLICACIÓN\n")
    print("     [/]  DIVISIÓN MATRIZ/REAL\n")

    # LECTURA DEL OPERADOR:
    operador = input("Introduzca el operador seleccionado: ")

    while operador not in ["+", "-", "/", "x"]:
        print("\nERROR: El operador proporcionado por parámetro no es correcto.")
        operador = input("Introduzca el operador seleccionado: ")
    
    # LECTURA DE VALORES DE LA PRIMERA MATRIZ:
    m1 = list(list())
    print("\nIntroduzca los valores de la primera matriz, separados por un espacio.")
    print("Para ello, se introducirán fila a fila.")
    print("En el momento en el que haya finalizado con la fila actual, pulse ENTER.")
    print("Cuando no quiera introducir más filas, escriba 'FIN'.")
    
    lectura = input()
    while lectura.upper() != "FIN":
        vector = lectura.split()
        v = list()
        for n in vector:
            v.append(float(n))
        m1.append(v)
        lectura = input()

    # COMPROBACIÓN DE TAMAÑOS DE LAS FILAS DE LA PRIMERA MATRIZ:
    iguales = True
    for i in range(1, len(m1)):
        if(len(m1[0]) != len(m1[i])):
            iguales = False

    if(not iguales):
        print("\nERROR: El tamaño de todas las filas debe ser el mismo.")
        exit()

    if operador != "/":
        # LECTURA DE VALORES DE LA SEGUNDA MATRIZ:
        m2 = list(list())
        print("\nIntroduzca los valores de la segunda matriz, separados por un espacio.")
        print("Para ello, se introducirán fila a fila.")
        print("En el momento en el que haya finalizado con la fila actual, pulse ENTER.")
        print("Cuando no quiera introducir más filas, escriba 'FIN'.")
        
        lectura = input()
        while lectura.upper() != "FIN":
            vector = lectura.split()
            v = list()
            for n in vector:
                v.append(float(n))
            m2.append(v)
            lectura = input()
        
        # COMPROBACIÓN DE TAMAÑOS DE LAS FILAS DE LA SEGUNDA MATRIZ:
        iguales = True
        for i in range(1, len(m2)):
            if(len(m2[0]) != len(m2[i])):
                iguales = False

        if(not iguales):
            print("\nERROR: El tamaño de todas las filas debe ser el mismo.")
            exit()
    else:
        lectura = input("\nIntroduzca el valor a dividir: ")
        num = float(lectura)

    # COMPARACIÓN DE TAMAÑOS DE AMBAS MATRICES:
    if operador in ["+", "-"] and (len(m1) != len(m2) or len(m1[0]) != len(m2[0])):
        print("\nERROR: El tamaño de ambas matrices debe ser el mismo.")
        exit()
    elif operador == "x" and (len(m1) != len(m2[0])):
        print("\nERROR: El número de columnas de la primera matriz debe ser igual al número de filas de la segunda.")
        exit()
        
    # RESULTADO:
    if operador == "+":
        resultado = client.suma_matrices(m1, m2)
    elif operador == "-":
        resultado = client.resta_matrices(m1, m2)
    elif operador == "x":
        resultado = client.multiplicacion_matrices(m1, m2)
    else:
        resultado = client.division_matriz_real(m1, num)
    
    print("\nOPERACIÓN A REALIZAR: " + operador)
    print("\nPrimera matriz:")
    for fila in m1:
        print(fila)

    if operador != "/":
        print("\nSegunda matriz: ")
        for fila in m2:
            print(fila)
    else:
        print("\nSegundo valor:" + str(num))
    
    print("\nMatriz resultado:")
    for fila in resultado:
        print(fila)
    

transport.close()
