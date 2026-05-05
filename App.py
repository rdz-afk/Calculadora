def sus():
    i=int(input('Escolha um número inteiro: '))
    ii=i+1
    iii=i-1
    print(' O número escolhido foi {}, o seu sucessor é {}, e seu antecessor é {}'.format(i,ii,iii))


def mais():
    n1= float(input('Escolha o primeiro número: '))
    n2= float(input('Escolha o Segundo número: '))
    m=float(n1+n2)
    print('O resultado da adição é igual a {:.2f}'.format(m))

def menos():
    n1= float(input('Escolha o primeiro número: '))
    n2= float(input('Escolha o Segundo número: '))
    m=float(n1-n2)
    print('O resultado da subtração é igual a {:.2f}'.format(m))

def multi():
    n1= float(input('Escolha o primeiro número: '))
    n2= float(input('Escolha o Segundo número: '))
    m=float(n1*n2)
    print('O resultado da multiplicação é igual a {:.2f}'.format(m))

def div():
    n1= float(input('Escolha o primeiro número: '))
    n2= float(input('Escolha o Segundo número: '))
    m=float(n1/n2)
    print('O resultado da  é igual a {:.2f}'.format(m))

def pares():
    i=int(input('Escolha um número inteiro: '))
    c=i%2

    if c==0:
        print('este número é par!!')
    elif c>0:
        print('Este número é ímpar!!')
    else:
        print('Este resultado não existe!!')

def conf():
    print('Nesta operação será testado se X>Y.')

    x=float(input('X=Escoha um número qualquer:'))
    y=float(input('Y=Escolha qualque outro: '))

    if x>y :
        print('{} é maior que {}!').format(x,y)
    elif x<y:
        print(' {} não é maior que {}!')
    else:
        print('Os valores são iguais!')


while True:
    print('Seja bem-vindo, o que você gostaria de fazer?')
    print('1)Adição \n2)subtraçaão \n3)Multiplicação \n4)Divisão \n5)Pares \n6)Comparação \n7)Contagem \n8)Sair')
    esc= int(input('Escolha um número de 1 a 8: '))
    print()


    match esc:
       case 1:
           mais()
           print()

       case 2:
           menos()
           print()

       case 3:
           multi()
           print()

       case 4:
           div()
           print()

       case 5:
           pares()
           print()

       case 6:
           conf()
           print()

       case 7:
           sus()
           print()

       case 8:
            print('Encerrando a calculadora, obrigado pelo uso!')
            break

       case _:
          print(' Resultado não encontrado, escolha uma operação que exista!')
          print()
