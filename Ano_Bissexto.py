'''
Lista 2

5. Escreva uma função chamada "verificar_ano_bissexto" que receba um número inteiro
como parâmetro e retorne True se o ano for bissexto, e False caso contrário.
Um ano é bissexto se for divisível por 4, mas não divisível por 100, exceto se for 
divisível por 400.

'''

def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    else:
        return False
        
    
def main():
    try:
        ano = int(input("Digite um ano: "))
        print((eh_bissexto(ano)))
    except:
        print("BURRO")
    finally:
        print("Blz cara, maldito homem que acredita no homem. >:[")
    
if __name__ == "__main__":
    main()