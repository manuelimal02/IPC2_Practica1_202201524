from Pieza import Pieza
from Nodo_Pieza import Nodo_Pieza

import sys
import os

class Lista_Pieza:
    def __init__(self):
        self.primero=None
        self.n_columnas=0
        self.m_filas=0
        self.contador_pieza=0

    def insertar_pieza(self,pieza):
        if self.primero is None:
            self.primero = Nodo_Pieza(pieza=pieza)
            self.contador_pieza+=1
        else:
            actual=self.primero
            while actual.siguiente:
                actual=actual.siguiente
            actual.siguiente = Nodo_Pieza(pieza=pieza)
            self.contador_pieza+=1

    def inicializar_tablero(self,m_fila,n_columna):
        for i in range(1,m_fila+1):
            for j in range(1,n_columna+1):
                self.insertar_pieza(Pieza(i,j,"|X|"))

    def imprimir_lista_tablero(self):
        actual=self.primero
        print("-------------------------------")
        while actual!= None:
            print("M_Fila:",actual.pieza.m_fila,"N_Columna:",actual.pieza.n_columna,"Color:",actual.pieza.color)
            actual=actual.siguiente
        print("-------------------------------")

    def actualizar_tablero(self,m_fila,n_columna,color):
        actual=self.primero
        while actual!=None:
            if actual.pieza.m_fila==m_fila and actual.pieza.n_columna==n_columna:
                actual.pieza.color=color
                print("Color Agregado a la Pieza Correctamente.")
                return
            actual=actual.siguiente
        print("ERROR: Posición de la pieza no encontrada.")

    def devolver_color(self,m_fila,n_columna):
        actual=self.primero
        while actual!=None:
            if actual.pieza.m_fila==m_fila and actual.pieza.n_columna==n_columna:
                return actual.pieza.color
            actual=actual.siguiente

    def devolver_color_grafica(self,m_fila,n_columna):
        actual=self.primero
        while actual!=None:
            if actual.pieza.m_fila==m_fila and actual.pieza.n_columna==n_columna:
                if actual.pieza.color=="|A|":
                    color="Blue"
                    return color
                elif actual.pieza.color=="|R|":
                    color="Red"
                    return color
                elif actual.pieza.color=="|V|":
                    color="Green"
                    return color
                elif actual.pieza.color=="|P|":
                    color="Purple"
                    return color
                elif actual.pieza.color=="|N|":
                    color="Orange"
                    return color  
            actual=actual.siguiente

    def imprimir_tablero(self):
        print("-----------------------------------------")
        for i in range(1,self.m_filas+1):
            for j in range(1,self.n_columnas+1):
                print(self.devolver_color(i,j),end="\t")
            print("")
        print("-----------------------------------------")
        print("")

    def graficar(self):
        f = open('g_tablero.dot','w')
        texto="digraph G {\n node [shape=plaintext];\nlabel=\"Colorealo Guatematel\";\nsome_node [\nlabel=<\n<table border=\"0\" cellborder=\"0\" cellspacing=\"0\" width=\"100%\" height=\"100%\">\n"
        for i in range(1, self.m_filas + 1):
            texto+="<tr>\n"
            for j in range(1, self.n_columnas + 1):
                texto+="<td bgcolor=\""+str(self.devolver_color_grafica(i,j))+"\" width=\"1\" height=\"1\">"+str(self.devolver_color(i,j))+"</td>\n"
            texto+="</tr>\n"
        texto+="</table>>\n];\n}"
        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng g_tablero.dot -o Tablero.png')
        print("Gráfica Generada Correctamente.")



