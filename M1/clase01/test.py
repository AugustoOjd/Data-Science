def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    if(numero < 0):
        return None
    
    lista_nro_binario = []
    lista_nro_enteros = []
    
    lista_nro_enteros.append(numero)

    for i in lista_nro_enteros:
        if i <= 0:
            break
        else:
            i//=2
            if i == 0:
                break
            else:
                lista_nro_enteros.append(i)
                
    lista_nro_enteros.reverse()
    for e in lista_nro_enteros:
        e%=2
        print(e)
        lista_nro_binario.append(e)

    return lista_nro_binario

print(NumeroBinario(82))