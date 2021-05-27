from os import system
from time import sleep
import sys

# Título da página
def title(titulo, subtitulo=''):
    print(f'\n\033[;7m{titulo.upper():^100}\033[m')
    print(f'{subtitulo}')
    print('\n')

# Texto de falha/erro
def titleErro(txt):
    print(f'\033[1;31m{txt}\033[m')

# Texto de dica
def titleDica(txt):
    print(f'\033[1;32m{txt}\033[m\n')

# Texto de alerta
def titleAlerta(txt):
    print(f'\033[1;33m{txt}\033[m')

# Opções gerais do sistema.
def options():
    try:
        print(2 * '\n')
        print('_' * 100)
        print(f'\033[;1m{"C-Contatos | N-Novo | E-Editar | A-Ajuda | Q-Sair":^100}\033[m')
        opt = str(input(f'{"→"}'))[0]

        if opt in 'Nn':
            novoContato()
        if opt in 'Cc':
            visualContato()
        if opt in 'Aa':
            ajuda()
        if opt in 'Qq':
            sair()
        if opt in 'Ee':
            titleAlerta('Esta opção ainda não está disponível.')
            sleep(2)
            telaInicial()
        else:
            titleAlerta(f'Atenção: "{opt}" não é uma opção válida!')
            sleep(2)
            telaInicial()
    except IndexError:
        titleAlerta('Opção inválida!')
        sleep(2)
        telaInicial()

# Opção para a criação de um novo contato.
def novoContato():
    system('clear')
    from lib.functions import title
    title('NOVO CONTATO', 'Informe abaixo os dados do contato.')
    titleDica('Dica: para desistir do registro, basta não salvar os dados ao final!')

    # informações básicas
    nome = str(input('Nome: '))
    tel = str(input('Telefone: '))
    email = str(input('E-mail: '))
    end = str(input('Endereço: '))
    obs = str(input('Observações: '))
    if nome == '':
        nome = '* contato sem nome *'

    # Confirmação de salvamento.
    try:
        while True:
            salvar = str(input('\033[;1mSalvar os dados informados? S/N\033[m')[0]).upper()

            if salvar not in 'SN':
                titleErro('Opção inválida!')
            elif salvar == 'N':
                telaInicial()
            else:
                from lib.functions import novoArqContato
                novoArqContato()
                seq_arq = open('lib/docs/meus_contatos/total.txt').read()
                file = open(f'lib/docs/meus_contatos/contato-{seq_arq}.txt', 'a')

                file.write(f'{seq_arq:<20}\033[;1m{nome:_>50}\033[m\n')
                file.write((f'{"Telefone:":<20}\033[;1m{tel:_>50}\033[m\n'))
                file.write((f'{"E-mail:":<20}\033[;1m{email:_>50}\033[m\n'))
                file.write((f'{"Endereço:":<20}\033[;1m{end:_>50}\033[m\n'))
                file.write((f'{"Observações:":<20}\033[;1m{obs:_>50}\033[m\n'))
                file.close()
                break
        telaInicial()
    except:
        titleAlerta('Nenhma opção foi informada, a entrada será cancelada.')
        sleep(3)
        exit(telaInicial())

# Tela de boas vindas.
def welcome():

    file = open('lib/docs/meus_contatos/total.txt', 'rt')

    if file.read() == '0':
        welc = open('lib/docs/welcome', 'r')
        print(welc.read())
        welc.close()
    else:
        titleDica('Você possue um ou mais contatos cadastrados, para visualizar basta entrar com a opção "C".')
        titleAlerta('Este programa está em teste e pode conter bugs.')
        titleAlerta('Utilize por sua conta e risco.')
        titleDica('Nos ajude melhorando e modificando este programa.')
        print('\n' * 5)

# Tela inicial do programa
def telaInicial():
    system('clear')
    title('PyBook v1.0.0')
    welcome()
    options()

# Cria os arquivos de cada contato.
def novoArqContato():
    # abre para leitura do valor atual
    arq_tot = open('lib/docs/meus_contatos/total.txt', 'r')
    att_total = int(arq_tot.read()) + 1
    arq_tot.close()

    # abre para atualizar o valor anterior
    arq_tot = open('lib/docs/meus_contatos/total.txt', 'w')
    arq_tot.write(str(att_total))
    arq_tot.close()

    # cria um novo arquivo de contato com base na sequencia.
    arq_tot = open('lib/docs/meus_contatos/total.txt').read()
    v = f'contato-{str(arq_tot)}.txt'
    novo_contato = open(f'lib/docs/meus_contatos/{v}', 'w')
    novo_contato.close()

# Exibe os contatos cadastrados.
def exibeNomeDosContatos():
    # verifica se tem contatos criados, se tiver leia a linha 1 de cada arquivo (nome).

    total = open('lib/docs/meus_contatos/total.txt').read()
    totall = int(total)

    for c in range(1, totall + 1):
        nomeContatos = open(f'lib/docs/meus_contatos/contato-{c}.txt', 'r')
        nomeContatos.seek(0)
        print(nomeContatos.readline())
        nomeContatos.close()

# Lista todos os contatos existentes
def exibeNomeDosContatos():
    # verifica se tem contatos criados, se tiver leia a linha 1 de cada arquivo (nome).
    total = open('lib/docs/meus_contatos/total.txt').read()
    totall = int(total)
    for c in range(1, totall + 1):
        nomeContatos = open(f'lib/docs/meus_contatos/contato-{c}.txt', 'r')
        nomeContatos.seek(0)
        print(nomeContatos.readline())
        nomeContatos.close()

# Busca informações do contato com base no ID.
def visualContato():
    from lib.functions import title, options
    system('clear')
    title('CONTATOS CADASTRADOS')
    titleDica('Dica: para visualizar todos os dados informe o ID do contato.')
    titleAlerta('Atenção: para cancelar a operação digite a tecla "0" zero.\n')
    print('-' * 100)
    exibeNomeDosContatos()
    try:
        while True:
            print('\n')
            opt = int(input('ID do contato: '))
            total = open('lib/docs/meus_contatos/total.txt').read()
            totall = int(total)

            if opt in range(1, totall + 1):
                system('clear')
                title('EXIBINDO DADOS DO CONTATO')
                titleDica('Dica 1: para visualizar dados de outros contatos, basta informar o ID.')
                titleDica('Dica 2: para sair pressione "0" zero.')
                print('-' * 100)
                contato = open(f'lib/docs/meus_contatos/contato-{opt}.txt').read()
                print(contato)
            elif opt == 0:
                system('clear')
                telaInicial()
            else:
                titleAlerta('ID não encontrado!')
                sleep(2)
                visualContato()
    except Exception:
        telaInicial()

def ajuda():
    while True:
        system('clear')
        title('CENTRAL DE AJUDA')
        help = open('lib/docs/help.txt').read()
        print(help)
        print('\n')
        print('[ q ] - Para sair da central de ajuda.')
        sair = str(input(''))

        if sair in 'Qq':
            exit(telaInicial())

def sair():
    system('clear')
    title('SAINDO DO SISTEMA')
    img = open('lib/docs/cat.txt').read()
    print(img)
    print('\n')
    try:
        while True:
            titleAlerta('Atenção: quer mesmo sair do sistema? y/n')
            opt = str(input(f'{"→"}')[0]).upper()
            if opt == 'N':
                exit(telaInicial())
            if opt == 'Y':
                system('clear')
                exit(sys.exit())
            else:
                titleAlerta('Atenção: nenhuma opção informada, retornando a tela inicial.')
                sleep(3)
                exit(telaInicial())
    except IndexError:
        titleAlerta('Voltando ao sistema!')
        sleep(2)
        telaInicial()

def mensagemDeErro():
    #system('clear')
    title('NOTIFICAÇÃO DE FALHA DO SISTEMA')
    img = open('lib/docs/cat.txt').read()
    print(img)
    print('\033[;1mCALMA!\033[m')
    print(f'\n\033[1;31mO sistema identificou alguma falha ao realizar o procedimento.\033[m')
    print('\033[1;31mTente novamente em seguida, ou contate o desenvolvedor.\033[m')
    print("""
    Erros comuns:
    - Falha na digitação ou algum caracter incorreto;
    - O usuário pressionou um tecla indevida;
    - O procedimento foi interrompido de alguma forma.
    """)
    while True:
        opt = str(input('\n\033[;1mPressione qualquer tecla para sair!\33[m'))
        if opt in 'Qq':
            exit(telaInicial())


def deleteContato():
    import os
    from time import sleep
    from lib.functions import title, titleAlerta, telaInicial, titleDica

    #title('REMOVER ARQUIVO DE CONTATO ESPECIFICO')
    #titleDica('Dica: pressione "0" zero para cancelar a operação.')
    #print('-' * 100)
    opt = int(input('Remover contato ID: '))

    # atualiza o contador de contatos
    if opt > 0:
        f = open('lib/docs/meus_contatos/total.txt').read()
        n = int(f) - 1
        nn = str(n)
        ff = open('lib/docs/meus_contatos/total.txt', 'r+')
        ff.write(nn)
        ff.close()

        # remove o arquivo de contatos
        os.remove(f'lib/docs/meus_contatos/contato-{opt}.txt')
        telaInicial()
    else:
        titleAlerta('A operação não foi finalizada.')
        sleep(2)
        telaInicial()