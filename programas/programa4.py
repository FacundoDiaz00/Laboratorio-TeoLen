# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    ''''tag = re.findall(r'"tag": "(.*)",', texto)
    it=0
    result=""
    #("tag": )"(.*)",\s*("patterns": \[\s+)".*",*(\s*".*",*)*\s*],\s*("responses": \[\s+)".*",*(\s*".*",*)*
    #"tag"(.|\s)*?"context_set": ""
    aux = re.findall(r'"tag"(.|\s)*?"context_set": ""', texto, flags=0)
    for i in aux:

        pat = re.findall(r'("patterns": \[\s+)".*",*(\s*".*",*)*', str(i), flags=0)
        pat = re.findall(r'\s*".*",*', str(pat), flags=0)

        res = re.findall(r'("responses": \[\s+)".*",*(\s*".*",*)*', str(i), flags=0)
        res = re.findall(r'\s*".*",*', str(res), flags=0)

        result = result + tag[it] + " " + str(len(pat)) + " " + str(len(res)) + "\n"
    return result''''

    pat = re.findall(r'"patterns": (\[\s*.*?\s*\])', texto, flags=re.DOTALL)
    res = re.findall(r'"responses": (\[\s*.*?\s*\])', texto, flags=re.DOTALL)
    for i in pat:
        if it<len(pat)-1:
            patterns=re.split('",\n',i)
            num_pat=len(patterns)
            responses=re.split('",\n',res[it])
            num_responses=len(responses)
            aux=aux+tag[it]+" "+str(num_pat)+" "+str(num_responses)+"\n"
            it=it+1
        else:
            patterns=re.split('",\n',i)
            num_pat=len(patterns)
            responses=re.split('",\n',res[it])
            num_responses=len(responses)
            aux=aux+tag[it]+" "+str(num_pat)+" "+str(num_responses)
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
