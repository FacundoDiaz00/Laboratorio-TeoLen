# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):

    result = re.sub(r'("tag": )"(.*)",', r'\1''"T",', texto, flags=0)
    result = re.sub(r'("patterns": \[\s+)".*",*(\s*".*",*)*', r'\1"P"', result, flags=0)
    result = re.sub(r'("responses": \[\s+)".*",*(\s*".*",*)*', r'\1"R"', result, flags=0)

    # O alternativamente:
    #result = re.sub(r'("patterns": \[\s+".*"),*(\s*".*",*)*', r'\1', texto, flags=0)
    #result = re.sub(r'("responses": \[\s+".*"),*(\s*".*",*)*', r'\1', result, flags=0)
    #result = re.sub(r'("patterns": \[\s+).*",*(\s*".*",*)*', r'\1''"P"', result, flags=0)
    #result = re.sub(r'("responses": \[\s+).*",*(\s*".*",*)*', r'\1''"R"', result, flags=0)
    return result




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
