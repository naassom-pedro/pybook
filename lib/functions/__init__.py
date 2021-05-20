# Título da página
def title(titulo, subtitulo=''):
    print(f'{titulo.upper()}')
    print(f'{subtitulo.title()}')
    print('\n')


# Opções gerais do sistema.
def options():
    print(2 * '\n')
    print(f'C-Contatos | N-Novo | E-Editar | A-Ajuda')
    opt = str(input()).upper()
    if opt == 'N':
        novo()

# Opção para a criação de um novo contato.
def novo():
    # cadastrar novo contato.
    from lib.functions import title
    title('NOVO CONTATO', 'Cadastre todos os contatos, e tenha todas as informações de forma completa')
    varStr('Nome')
    varStr('Telefone')
    varStr('E-mail')
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
        file = open('lib/docs/welcome')

def telaInicial():
    title('TELA INICIAL')
    welcome()
    options()
