def validar_cpf(cpf):
    resultado = []
    lista=[]

    for i in cpf:
        lista.append(i)
    
    lista.remove(".")
    lista.remove(".")
    lista.remove("-")
    multiplicador = 10
    multiplicador2 = 11
    multiplicacao = 0
    multiplicacao2 = 0
    ver1 = 0
    ver2 = 0
    
    if lista[0]==lista[1] and lista[1]==lista[2] and lista[2]==lista[3]and lista[3]==lista[4]and lista[4]==lista[5]and lista[5]==lista[6] and lista[6]==lista[7] and lista[7]==lista[8] and lista[8]==lista[9] and lista[9]==lista[10]:
        return "Inválido"

    for d in range(len(lista)):    
        multiplicacao += int(lista[d]) * multiplicador
        multiplicador -= 1
        if multiplicador==1:
            ver1 = (multiplicacao * 10)%11
    
    for dd in range(len(lista)):
        multiplicacao2 += int(lista[dd]) * multiplicador2
        multiplicador2 -= 1
        if multiplicador2==1:
            ver2 = (multiplicacao2 * 10)%11
        
    if ver1 == int(lista[9]) and ver2 == int(lista[10]):
        return "Válido" 
    else:
        return "Inválido"
    
    
          
            
       

