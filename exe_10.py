#CRUD#
import msvcrt

usuarios = [];
id_inicial = -1
def adicionar_Usuario(id, name, idade, cpf):
    usuario = {"id": id, "nome": name, "idade":idade, "cpf":cpf}

    usuarios.append(usuario)

def remover_Usuario(name):
    for i in usuarios:
        if i["nome"] == name:
            usuarios.remove(i)
            break

def consultarUsuarios():
    for i in usuarios:
        print(f'{i}')    

def editar_Usuarios(name):
    for i in usuarios:
        if i["nome"] == name:
            print('\n' + '═' * 40)
            print(f'Escolha abaixo o que deseja editar de(a) {i["nome"]}')
            print('1 - Nome')
            print('2 - Idade')
            print('3 - cpf')


def input_cpf():
    cpf = ''
    formatado = ''
    print('CPF do usuário: ', end='', flush=True)

    while len(cpf) < 11:
        digito = msvcrt.getwch()

        if digito.isdigit():
            cpf += digito
            formatado += digito
            print(digito, end='', flush=True)

            if len(cpf) % 3 == 0 and len(cpf) < 11:
                formatado += '-'
                print('-', end='', flush=True)

    print()
    return formatado


#Iniciar o processo
init = input("Deseja inificar o processo ? (S/N)").lower()
control = True
if init  == 's':
    while control:
        print('\n' + '═' * 40)
        print('        🗂  GERENCIADOR DE USUÁRIOS')
        print('═' * 40)
        print('  1 - ➕  Adicionar usuário')
        print('  2 - ❌  Remover usuário')
        print('  3 - 🔍  Consultar usuários')
        print('  4 - ✏️  Editar')
        print('═' * 40)
        number  = int(input('Escolha:'))

        if number == 1:
            id_inicial+=1
            nome  = input('Nome do usuario:')

            if not nome.isalpha():
                print(' 😢 O nome contém numero! Tente novamente')
                continue

            try:
                idade = int(input('Idade do usuário:'))
            except ValueError:
                print(' 😢 Erro na idade! Digite apenas números. Tente novamente')
                continue
            
            cpf = input_cpf()

            adicionar_Usuario(id_inicial, nome, idade, cpf);

        if number == 2:
            nome = input('Nome do usuário:')
            remover_Usuario(nome);


        if number == 3:
            consultarUsuarios()

        if number == 4:
            nome = input('Nome do usuario:')
            editar_Usuarios(nome)



        #Finalizar o processo 
        finish = input('Deseja finalizar o processo ?').lower()
        if finish == 's':
            control = False





print('\n' + '═' * 40)
print('  ✔  Sistema encerrado com sucesso!')
print(f'  Usuários cadastrados: {len(usuarios)}')
print('  Obrigado por usar o sistema! Até logo 👋')
print('═' * 40 + '\n')