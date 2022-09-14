import json
import hashlib
import getpass
import pickle
import os
from interface.menuClass import *
from interface.usersClass import *
from interface.votacaoClass import *
from models.module_CRUD import *

# Const
path = './database/database.json'

def parametros_menu(titulo: list, itens: list):
    menu = Menu()
    menu.setTitulo(titulo)
    menu.setItems(itens)
    option = menu.iniciarMenu()
    return option

def tela_inicial():
    title = (['#############################################\n', 
                '\tBem Vindo Ao Sistema De Votação\n', 
            '#############################################\n',
            'Para navegar pelo menu utilize as setas do teclado\n',
            'E utilize o "Enter" para interagir com os itens.\n'])
    items = (['Efetuar Login', 'Sobre', 'Sair'])
    option = parametros_menu(title, items)

    # Switch case
    if option == 0:
        tela_login()

    elif option == 1:
        print ('Este projeto tem como objetivo a conclusão da parte introdutória do curso Python Dados e Web cedido pela CEPEDI.')
        print ('Ele consiste num sistema de votação, onde temos diferentes tipos de usuários (Candidato e Eleitor).')
        print ('Apenas o criador da votação poderá encerrar e computar os votos, cada Eleitor poderá votar apenas 1 única vez.')
        input()
        tela_inicial()
    else:
        exit()

def tela_login():
    items = ['Acessar sistema', 'Cadastrar', 'Sair']
    option = parametros_menu([], items)

    if option == 0:
        print ('Digite o seu user:')
        user = input()
        print ('Digite o sua senha:')
        password = getpass.getpass()
        password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()

        user_db = readUser(path, user)
        if not user_db:
            print("Usuario não encontrado.")
            exit()

        if user_db['role'] == 0:
            user_db = Eleitor(user, user_db['password'], user_db['name'], user_db['age'])
        else:
            user_db = Candidato(user, user_db['password'], user_db['name'], user_db['age'], user_db['proposta'])

        if user_db.validarPassword(password):
            tela_usuario(user_db)
        else:
            print("Senha incorreta")
            exit()

    elif option == 1:
        user = {}
        user['user'] = input('Escolha um user:\n')
        password = getpass.getpass('Escolha uma senha:\n')
        user['password'] = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
        user['name'] = input('Digite seu nome:\n')
        user['age'] = input('Digite sua idade:\n')
        user['role'] = parametros_menu([], ['Eleitor', 'Candidato'])
        if user['role'] == 1:
            user['proposta'] = input('Digite sua proposta:\n')

        if createUser(path, **user):
            input('Usuário criado com sucesso !\n')
            tela_inicial()
        else:
            input('Usuário já se encontra cadastrado no sistema\n')
            tela_inicial()
    else:
        exit()
            
def tela_usuario(user_class):
    title = [f'Bem vindo {user_class.getName()}\n']
    items = ["Votação", "Dados cadastrais", "Sair"]

    option = parametros_menu(title, items)

    if option == 0:
        tela_votacao(user_class)
    
    elif option == 1:
        print (f'Usuário: {user_class.getUser()}')
        print (f'Nome: {user_class.getName()}')
        print (f'Idade: {user_class.getAge()}')
        
        if type(user_class) is Candidato:
            print (f'Proposta: {user_class.getProposta()}')

        input ('\nPara prosseguir digite alguma tecla:\n')

        tela_edit(user_class)

    else:
        exit()
    
def tela_edit(user_class):
    option = parametros_menu(['Deseja fazer alterações ?'], ["Sim", "Não", "Excluir Conta"])

    if option == 0:
        print ("Caso não queira modificar um dado, deixar em branco.\n")
        
        name = input("Digite um nome: ")
        if name:
            user_class.setName(name)

        age = input("Digite uma idade: ")
        if age:
            user_class.setAge(age)

        if type(user_class) is Candidato:
            proposta = input ("Digita uma proposta: ")
            if proposta:
                user_class.setProposta(proposta)

        user_dict = {
        "user": user_class.getUser(),
        "password": user_class.getPassword(),
        "name": user_class.getName(),
        "age": user_class.getAge(),
        }

        if type(user_class) is Candidato:
            user_dict['proposta'] = user_class.getProposta()
            user_dict['role'] = 1
        else:
            user_dict['role'] = 0

        if updateUser(path, **user_dict):
            input("Alterações feitas com sucesso ! Aperte alguma tecla para continuar")
            tela_usuario(user_class)
        else:
            print("Erro ao alterar dados")
            exit()

    elif option == 1:
        tela_usuario(user_class)
    else:
        deleteUser(path, user_class.getUser())
        print("Operação realizada com sucesso !")
        exit()

def tela_votacao(user_class):
    try:
        with open ("./database/votacao.pkl", "rb") as file:
            votacao = pickle.load(file)
    except:
        option = parametros_menu(["Nenhuma votação no momento, deseja iniciar uma ?\n"], ["Sim", "Não", "Sair"])
        if option == 0:
            votacao = Votacao(user_class)
            print ("Criação concluida !")
            with open ("./database/votacao.pkl", "wb") as file:
                pickle.dump(votacao, file)
            input ()
            os.system("clear")
        elif option == 1:
            tela_usuario(user_class)
        else:
            exit()

    if votacao.organizador.getUser() == user_class.getUser():
        tela_votacao_creator(user_class, votacao)

    title = [f'Bem vindo a votação organizada por {votacao.organizador.getName()}.\n']

    if votacao.getVotacaoDisp():
        title.append("A votação ainda não foi iniciada.\n")
        parametros_menu(title, ['Retornar'])
        tela_usuario(user_class)

    option = parametros_menu(title, ['Votar', 'Retornar'])

    if option == 0:
        votar(user_class, votacao)
        tela_votacao(user_class) 
    else:
        tela_usuario(user_class)

def votar(user_class, votacao):
    if not user_class.getUser() in votacao.getVotantes():
        usr_nome = []
        for item in votacao.getCandidatos():
            try:
                usr_nome.append([   item, readUser(path, item)['name'], readUser(path, item)['proposta']   ])
            except:
                pass

        items = [f'Candidato: {nome}\tProposta: {proposta}' for _, nome, proposta in usr_nome]
        option = parametros_menu(["Selecione o candidato que deseja votar"], items)

        votacao.votar(option, user_class.getUser())
        input(f'Computado o voto no candidato {usr_nome[option][1]} com sucesso')

        with open ("./database/votacao.pkl", "wb") as file:
            pickle.dump(votacao, file)
    else:
        input("Usuário já votou.\n")

def tela_votacao_creator(user_class, votacao):
    items = []
    if votacao.getVotacaoDisp():
        items.append("Iniciar a votação")
        items.append("Cadastrar candidatos")
    else:
        items.append('Votar')
        items.append("Encerrar a votação")
    items.append("Retornar")

    option = parametros_menu(["Votação acessada pelo seu organizador, funções extras disponíveis.\n"], items)

    if votacao.getVotacaoDisp():
        if option == 0:
            if len(votacao.getCandidatos()) > 1:
                input("Votacão iniciada com sucesso.")
                votacao.iniciarVotacao()
                with open ("./database/votacao.pkl", "wb") as file:
                    pickle.dump(votacao, file)
            else:
                input("Número insuficiente de candidatos.")
            tela_votacao(user_class)
        elif option == 1:
            votacao.setCandidato(cadastrar_users(votacao))
            tela_votacao(user_class)
        else:
            tela_usuario(user_class)
    else:
        if option == 0:
            votar(user_class, votacao)
            tela_votacao(user_class)  
        elif option == 1:
            encerrar_votacao(votacao, user_class)
        else:
            tela_usuario(user_class)

def encerrar_votacao(votacao, user_class):
    if len(votacao.getVotantes()) > 1:
        if votacao.encerrarVotacao(user_class.getUser()):
            vencedor, votos = votacao.getVencedor()
            vencedor = readUser(path, vencedor)
            input(f'Parabens {vencedor["name"]} venceu com {votos} voto(s) !')
            os.remove("./database/votacao.pkl")
            exit()
        else:
            if votacao.getEmpate():
                input('Votação encerrada, houve um empate')
            else:
                input('Erro na votação')
            os.remove("./database/votacao.pkl")
            exit()
    else:
        input("Não foi possível prosseguir a votação, apenas 1 voto feito.\n")
        tela_votacao(user_class)

def cadastrar_users(votacao):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    candidatos_cadastrados = []
    if len(votacao.getCandidatos()) > 0:
        candidatos_cadastrados = [item for item in votacao.getCandidatos()]
        title = ["Candidatos já cadastrados no sistema:\n"]
    else:
        title = []

    candidatos_disp = []
    for i, item in data.items():
        if item['role'] == 1:
            if not i in candidatos_cadastrados:
                candidatos_disp.append([i, item['name'], item['proposta']])
            else:   
                title += [f'{item["name"]}\n']
                
    if len(votacao.getCandidatos()) > 0:
        title += ["\n"]

    if len(candidatos_disp) > 0:
        title.append("Temos disponíveis esses candidatos.")
        item = [f'Candidato: {item[1]}\tProposta: {item[2]}' for item in candidatos_disp]
        selecionado = parametros_menu(title, item)
    else:
        print(''.join(title))
        input("Não temos disponíveis nenhum candidato.\n")
        return

    votacao.setCandidato(candidatos_disp[selecionado][0])
    with open ("./database/votacao.pkl", "wb") as file:
        pickle.dump(votacao, file)
    
    os.system("clear")
    input(f'Candidato {candidatos_disp[selecionado][1]} cadastrado no sistema com sucesso.')