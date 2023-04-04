# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    tag = re.findall(r'"tag": "(.*)",', texto)
    it=0
    aux=""
    pat = re.findall(r'"patterns": (\[\s*.*?\s*\])', texto, flags=re.DOTALL)
    for i in pat:
        if it<len(pat)-1:
            patterns=re.split('",\n',i)
            num_pat=len(patterns)
            aux=aux+tag[it]+" "+str(num_pat)+"\n"
            it=it+1
        else:
            patterns=re.split('",\n',i)
            num_pat=len(patterns)
            aux=aux+tag[it]+" "+str(num_pat)
            it=it+1
    return aux
    


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)      # ejecutar er
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
