import json
import hashlib
import getpass
import pickle
import os
from interface.menuClass import *
from interface.usersClass import *
from interface.votacaoClass import *
from models.module_CRUD import *

def parametros_menu(titulo: list, itens: list):
    menu = Menu()
    menu.setTitulo(titulo)
    menu.setItems(itens)
    option = menu.iniciarMenu()
    return option

def tela_login():
    title = []
    items = ['Acessar sistema', 'Cadastrar', 'Sair']
    option = parametros_menu(title, items)

    path = './database/database.json'

    if option == 0:
        print ('Digite o seu user:')
        user = input()
        print ('Digite o sua senha:')
        password = getpass.getpass()
        password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()

        user_db = readUser(path, user)

        if user_db == False:
            print("Usuario não encontrado.")
            exit(2)

        if user_db['role'] == 0:
            user_db = Eleitor(user, user_db['password'], user_db['name'], user_db['age'])
        else:
            user_db = Candidato(user, user_db['password'], user_db['name'], user_db['age'], user_db['proposta'])

        if (user_db.validarPassword(password)):
            tela_usuario(user_db)
        else:
            print("Senha incorreta")
            exit()

    elif option == 1:
        user = {}
        print ('Escolha um user:')
        user['user'] = input()
        print ('Escolha uma senha:')
        password = getpass.getpass()
        user['password'] = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
        print ('Digite seu nome:')
        user['name'] = input()

        print ('Digite sua idade:')
        user['age'] = input()
        user['role'] = parametros_menu([], ['Eleitor', 'Candidato', 'Cancelar'])
        if user['role'] == 1:
            print ('Digite sua proposta:')
            user['proposta'] = input()
        elif user['role'] == 2:
            exit()
        create = createUser(path, **user)

        if create:
            print('Usuário criado com sucesso !')
        else:
            print('Usuário já se encontra cadastrado no sistema')

        exit()
            
def tela_usuario(user_db):
    title = [f'Bem vindo {user_db.getName()}\n']
    items = ["Verificar votações", "Observar/Modificar dados cadastrais", "Sair"]

    option = parametros_menu(title, items)

    if option == 0:
        tela_votacao(user_db)
    elif option == 1:
        print (f'Usuário: {user_db.getUser()}')
        print (f'Nome: {user_db.getName()}')
        print (f'Idade: {user_db.getAge()}')
        
        if type(user_db) is Candidato:
            print (f'Proposta: {user_db.getProposta()}')

        input ('Para prosseguir digite alguma tecla: ')

        tela_edit(user_db)

    else:
        exit()
    
def tela_edit(user_db):
    title = ['Deseja fazer alterações ?']
    items = ["Sim", "Não", "Excluir Conta"]
    option = parametros_menu(title, items)
    path = './database/database.json'

    if option == 0:
        print ("Caso não queira modificar, deixar em branco.")
        
        name = input("Digite um nome: ")
        if name:
            user_db.setName(name)

        age = input("Digite uma idade: ")
        if age:
            user_db.setAge(age)

        if type(user_db) is Candidato:
            proposta = input ("Digita uma proposta: ")
            if proposta:
                user_db.setProposta(proposta)

        user_dict = {
        "user": user_db.getUser(),
        "password": user_db.getPassword(),
        "name": user_db.getName(),
        "age": user_db.getAge(),
        }

        if type(user_db) is Candidato:
            user_dict['proposta'] = user_db.getProposta()
            user_dict['role'] = 1
        else:
            user_dict['role'] = 0

        if updateUser(path, **user_dict):
            input("Alterações feitas com sucesso ! Aperte alguma tecla para continuar")
            tela_usuario(user_db)
        else:
            print ("Erro ao alterar dados")
            exit()

    elif option == 1:
        tela_usuario(user_db)
    else:
        deleteUser(path, user_db.getUser())
        print ("Operação realizada com sucesso !")
        exit()

def tela_votacao(user_db):
    try:
        with open ("./database/votacao.pkl", "rb") as file:
            votacao = pickle.load(file)
    except:
        option = parametros_menu(["Nenhuma votação no momento, deseja iniciar uma ?\n"], ["Sim", "Não", "Sair"])
        if option == 0:
            votacao = Votacao(user_db)
            print ("Criação concluida !")
            input ()
            os.system("clear")
        elif option == 1:
            tela_usuario(user_db)
        else:
            exit()

    title = []
    items = []

    if not votacao.getVotacaoDisp():
        items.append('Votar')
    
    if votacao.organizador.getUser() == user_db.getUser():
        title.append("Votação acessada pelo seu organizador, funções extras disponíveis.\n")
        if votacao.getVotacaoDisp():
            items.append("Iniciar a votação")
            items.append("Cadastrar candidatos")
        else:
            items.append("Encerrar a votação")
    else:
        title.append(f'Bem vindo a votação organizada por {votacao.organizador.getName()}.')

    items.append("Retornar")

    if votacao.getVotacaoDisp():
        title.append("\nA votação ainda não foi iniciada.")

    option = parametros_menu(title, items)

    if not votacao.getVotacaoDisp() and votacao.organizador.getUser() == user_db.getUser() and option == 1:
        encerrar_votacao(votacao, user_db)

    with open ("./database/votacao.pkl", "wb") as file:
        pickle.dump(votacao, file)

    if votacao.getVotacaoDisp():
        if len(items) == 1:
            tela_usuario(user_db)
        else:
            if option == 0:
                if len(votacao.getCandidatos()) > 1:
                    input("Votacão iniciada com sucesso.")
                    votacao.iniciarVotacao()
                    with open ("./database/votacao.pkl", "wb") as file:
                        pickle.dump(votacao, file)
                else:
                    input("Número insuficiente de candidatos.")

            elif option == 1:
                votacao.setCandidato(cadastrar_users(votacao))
                with open ("./database/votacao.pkl", "wb") as file:
                    pickle.dump(votacao, file)

        tela_usuario(user_db)

    else:
        if user_db.getUser() in votacao.getVotantes():
            input("Usuário já votou")
            exit()

        title = ["Selecione o candidato que deseja votar"]

        usr_nome = []
        for item in votacao.getCandidatos():
            try:
                usr_nome.append([   item, readUser('./database/database.json', item)['name'], readUser('./database/database.json', item)['proposta']   ])
            except:
                pass

        items = [f'Candidato: {nome}\tProposta: {proposta}' for _, nome, proposta in usr_nome]
        option = parametros_menu(title, items)

        votacao.votar(option, user_db.getUser())
        input(f'Computado o voto no candidato {usr_nome[option][1]} com sucesso')

        with open ("./database/votacao.pkl", "wb") as file:
            pickle.dump(votacao, file)

        exit()

    return

def encerrar_votacao(votacao, user_db):
    if votacao.encerrarVotacao(user_db.getUser()):
        vencedor, votos = votacao.getVencedor()
        vencedor = readUser('./database/database.json', vencedor)
        input(f'Parabens {vencedor["name"]} venceu com {votos} voto(s) !')
        os.remove("./database/votacao.pkl")
        exit()
    else:
        if votacao.getEmpate():
            input('Erro, houve empate')
        else:
            input('Erro')

        os.remove("./database/votacao.pkl")

        exit()

def cadastrar_users(votacao):
    path = './database/database.json'
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    candidatos_cadastrados = []
    if len(votacao.getCandidatos()) > 0:
        candidatos_cadastrados = [item for item in votacao.getCandidatos()]

    candidatos_disp = []
    for i, item in data.items():
        if item['role'] == 1:
            if not i in candidatos_cadastrados:
                candidatos_disp.append([i, item['name'], item['proposta']])

    if len(candidatos_disp) > 0:
        title = ["Temos disponíveis esses candidatos."]
        item = [f'Candidato: {item[1]}\tProposta: {item[2]}' for item in candidatos_disp]
        selecionado = parametros_menu(title, item)
    else:
        input("Não temos disponíveis nenhum candidato.\n")
        return

    return candidatos_disp[selecionado][0]

if __name__ == '__main__':
    title = (['#############################################\n', 
                '\tBem Vindo Ao Sistema De Votação\n', 
            '#############################################\n',
            'Para navegar pelo menu utilize as setas do teclado\n',
            'E utilize o "Enter" para interagir com os itens.'])
    items = (['Efetuar Login', 'Sobre', 'Sair'])
    tela_inicial = parametros_menu(title, items)

    # Switch case
    if tela_inicial == 0:
        tela_login()     

    elif tela_inicial == 1:
        print ('Este projeto tem como objetivo a conclusão da parte introdutória do curso Python Dados e Web cedido pela CEPEDI.')
        print ('Ele consiste num sistema de gerenciamento de votação, onde temos diferentes tipos de usuários (Candidato e Eleitor).')
        print ('Apenas o criador da votação poderá encerrar e computar os votos, cada Eleitor poderá votar apenas 1 única vez.')
    else:
        exit(1)