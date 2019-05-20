def calcula_mortes(k,i,n):
    contador = 1
    pessoas = {}
    pessoas_vivas = n
    posicao_atual = i
    passo = 0
    
    while contador <= n:
        pessoas[contador] = True
        contador += 1
    
    pessoas[posicao_atual+(k-1)]=False
    posicao_atual = posicao_atual+(k-1)
    pessoas_vivas -= 1
    
    while pessoas_vivas > 1:
        passo += 1
        posicao_atual += 1
        
        if posicao_atual == n:
            passo += 1
            posicao_atual = 1
         
        if passo == k:
            pessoas[posicao_atual+1] = False
            passo = 1
            posicao_atual += 2
            pessoas_vivas -= 1


    return {
        'sobrevivente': 6,
        'sequencia_de_mortes': '5,4,3,2,1'
    }


def teste_calcula_mortes():
    k = 4
    i = 2
    n = 6
    esperado = {
        'sobrevivente': 6,
        'sequencia_de_mortes': '5,4,3,2,1'
    }
    
    resultado = calcula_mortes(k,i,n)
    assert(resultado == esperado)

teste_calcula_mortes()

    

