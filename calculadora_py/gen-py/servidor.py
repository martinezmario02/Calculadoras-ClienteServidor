import glob
import sys
import math

from calculadora import Calculadora

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging

logging.basicConfig(level=logging.DEBUG)


class CalculadoraHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print("Me han hecho ping()")

    # OPERACIONES BÁSICAS:
    
    def suma(self, n1, n2):
        print("Sumando " + str(n1) + " con " + str(n2))
        return n1 + n2

    def resta(self, n1, n2):
        print("Restando " + str(n1) + " con " + str(n2))
        return n1 - n2
    
    def producto(self, n1, n2):
        print("Multiplicando " + str(n1) + " con " + str(n2))
        return n1 * n2

    def division(self, n1, n2):
        print("Dividiendo " + str(n1) + " con " + str(n2))
        return n1 / n2
    
    # OPERACIONES TRIGONOMÉTRICAS:
    
    def seno(self, n):
        print("Haciendo el seno de " + str(n))
        return math.sin(n*math.pi/180.0)
    
    def coseno(self, n):
        print("Haciendo el coseno de " + str(n))
        return math.cos(n*math.pi/180.0)

    def tangente(self, n):
        print("Haciendo el tangente de " + str(n))
        return math.tan(n*math.pi/180.0)

    def arcoseno(self, n):
        print("Haciendo el arcoseno de " + str(n))
        return math.asin(n)*180.0/math.pi

    def arcocoseno(self, n):
        print("Haciendo el arcocoseno de " + str(n))
        return math.acos(n)*180.0/math.pi

    def arcotangente(self, n):
        print("Haciendo el arcotangente de " + str(n))
        return math.atan(n)*180.0/math.pi
    
    # OTRAS OPERACIONES:
    
    def raiz_cuadrada(self, n):
        print("Haciendo la raiz de " + str(n))
        return math.sqrt(n)
    
    def potencia(self, n1, n2):
        print("Haciendo " + str(n1) + " elevado a " + str(n2))
        return math.pow(n1, n2)

    def logaritmo(self, n1, n2):
        print("Haciendo el logaritmo en base " + str(n2) + " de " + str(n1))
        return math.log(n1, n2)

    def porcentaje(self, n1, n2):
        print("Haciendo el porcentaje de " + str(n1) + " en función de " + str(n2))
        return (n1 / n2) * 100

    def modulo(self, n1, n2):
        print("Haciendo el modulo de " + str(n1) + " y " + str(n2))
        return n1 % n2
    

    # OPERACIONES CON VECTORES:

    def suma_vectores(self, v1, v2):
        print("Sumando " + str(v1) + " con " + str(v2))
        resultado = list()
        for i in range(0,len(v1)):
            resultado.append(v1[i]+v2[i])
        
        return resultado

    def resta_vectores(self, v1, v2):
        print("Restando " + str(v1) + " con " + str(v2))
        resultado = list()
        for i in range(0,len(v1)):
            resultado.append(v1[i]-v2[i])
        
        return resultado

    def producto_escalar(self, v1, v2):
        print("Haciendo el producto escalar de " + str(v1) + " con " + str(v2))
        resultado = 0
        for i in range(0,len(v1)):
            resultado += v1[i]*v2[i]
        
        return resultado

    def producto_vectorial(self, v1, v2):
        print("Haciendo el producto vectorial de " + str(v1) + " con " + str(v2))
        resultado = list()
        resultado.append(v1[1]*v2[2] - v1[2]*v2[1])
        resultado.append(v1[2]*v2[0] - v1[0]*v2[2])
        resultado.append(v1[0]*v2[1] - v1[1]*v2[0])
        
        return resultado

    def division_vector_real(self, v, num):
        print("Dividiendo " + str(v) + " con " + str(num))
        resultado = list()
        for i in range(0, len(v)):
            resultado.append(v[i] / num)
        
        return resultado

    # OPERACIONES CON MATRICES:
    
    def suma_matrices(self, m1, m2):
        print("Sumando " + str(m1) + " con " + str(m2))
        resultado = list(list())
        for i in range(0, len(m1)):
            vector = list()
            for j in range(0, len(m1[0])):
                vector.append(m1[i][j] + m2[i][j])
            resultado.append(vector)
        
        return resultado

    def resta_matrices(self, m1, m2):
        print("Restando " + str(m1) + " con " + str(m2))
        resultado = list(list())
        for i in range(0, len(m1)):
            vector = list()
            for j in range(0, len(m1[0])):
                vector.append(m1[i][j] - m2[i][j])
            resultado.append(vector)
        
        return resultado
    
    def multiplicacion_matrices(self, m1, m2):
        print("Multiplicando " + str(m1) + " con " + str(m2))
        resultado = list(list())
        for i in range(0, len(m1)):
            vector = list()
            for j in range(0, len(m2[0])):
                suma = 0
                for k in range(0, len(m1[0])):
                    suma += m1[i][k] * m2[k][j]
                vector.append(suma)
            resultado.append(vector)
        
        return resultado

    def division_matriz_real(self, m, num):
        print("Dividiendo " + str(m) + " con " + str(num))
        resultado = list(list())
        for i in range(0, len(m)):
            vector = list()
            for j in range(0, len(m[0])):
                vector.append(m[i][j] / num)
            resultado.append(vector)
        
        return resultado


if __name__ == "__main__":
    handler = CalculadoraHandler()
    processor = Calculadora.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("iniciando servidor...")
    server.serve()
    print("fin")
