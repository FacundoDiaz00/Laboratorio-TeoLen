# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    tag = re.findall(r'"tag": "(.*)",', texto)
    aux=""
    pat = re.findall(r'"patterns": (\[\s*.*?\s*\])', texto, flags=re.DOTALL) # Otra solucion(sin utiliar DOTALL):("patterns": \[\s(\s*".*",*\s)*\s*\]) 
    res = re.findall(r'"responses": (\[\s*.*?\s*\])', texto, flags=re.DOTALL) # ("responses": \[\s(\s*".*",*\s)*\s*\])
    
    tagResult = str(len(tag))

    aux = "".join(pat)
    patResult = str(len(re.findall(r'"(.*)"', aux)))
    
    aux = "".join(res)
    respResult = str(len(re.findall(r'"(.*)"', aux)))

    return tagResult + " " + patResult + " " + respResult

    """ for i in pat:
        if it<len(pat)-1:
            patterns=re.split('",\n',i)
            num_pat=num_pat+len(patterns)
            responses=re.split('",\n',res[it])
            num_responses=num_responses+len(responses)
            aux=aux+tag[it]+" "+str(num_pat)+" "+str(num_responses)+"\n"
            it=it+1
        else:
            patterns=re.split('",\n',i)
            num_pat=num_pat+len(patterns)
            responses=re.split('",\n',res[it])
            num_responses=num_responses+len(responses)
            it=it+1

    return str(it)+" "+str(num_pat)+" "+str(num_responses) """
    


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
