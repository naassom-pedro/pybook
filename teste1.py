from teste2 import Cadastro
from time import sleep

while 1:
    print('[ 1 ] Cadastrar | [ 2 ] Sair | [ 3 ] Imprmir')
    opt = int(input('==>'))

    if opt == 1:
        nome = str(input('Nome: ').strip()).lower()
        idade = int(input('Idade: ').strip())
        email = str(input('E-mail: ').strip()).lower()

        p1 = Cadastro(nome, idade, email)

    if opt == 3:
        print('Imprimindo...')
        sleep(2)
        print(p1.nome)
        print(p1.idade)
        print(p1.email)

    if opt == 2:
        print('Saindo do sistema...')
        break