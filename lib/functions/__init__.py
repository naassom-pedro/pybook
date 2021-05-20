# Título da página
def title(titulo, subtitulo=''):
    print(f'{titulo.upper()}')
    print(f'{subtitulo}')
    print('\n')


# Opções gerais do sistema.
def options():
    print(2 * '\n')
    print(f'C-Contatos | N-Novo | E-Editar | A-Ajuda')
    opt = str(input()).upper()
    if opt == 'N':
        novo()
    else:
        print('Escolha uma opção válida!')
        options()

# Opção para a criação de um novo contato.
def novo():
    from lib.functions import title
    title('NOVO CONTATO', 'Cadastre todos os contatos, e tenha todas as informações de forma completa')
    nome = str(input('Nome: ')).title()
    tel = str(input('Telefone: '))
    email = str(input('E-mail: '))

    # Confirmação de salvamento.
    while True:
        salvar = str(input('Salvar os dados informados? S/N'))[0].upper()
        if salvar != 'S' and salvar != 'N':
            print('Opção inválida.')
        elif salvar == 'N':
            telaInicial()
        else:
            file = open('lib/docs/contatos.txt', 'a')
            file.write(f'nome: {nome} ')
            file.write(f'tel: {tel} ')
            file.write(f'e-mail: {email} ')
            file.write('\n') # sempre deixar ao final uma quebra de linha.
            file.close()
            telaInicial()

    telaInicial()

# Cria um input do tipo 'str' e salva no arquivo de contatos.
def varStr(valor):
    var = str(input(f'{valor}: '))
    file = open('lib/docs/contatos.txt', 'a')
    file.write(var+';')
    file.close()

# Tela de bem vindo
def welcome():
    file = open('lib/docs/contatos.txt', 'r')
    if file.read() == '':
        welc = open('lib/docs/welcome', 'r')
        print(welc.read())
        welc.close()
    else:
        file = open('lib/docs/contatos.txt', 'r')
        total_linhas_arquivo = sum(1 for linha in file)
        for linha in range(0, total_linhas_arquivo):
            file.seek(0)
            print(f'{linha} - {file.readlines()[linha]}')
        file.close()




def telaInicial():
    title('TELA INICIAL', 'Veja e administre os seus contatos.')
    welcome()
    options()
