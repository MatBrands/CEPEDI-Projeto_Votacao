import sys
sys.path.insert(1, '../')

import pickle
import os
from model.Menu import *
from model.Register import *
from model.Users import *
from model.Voting import *
from getpass import getpass
from hashlib import sha256

crud = Register()
PICKLE_PATH = "./controller/voting.pkl"

def set_menu(title: list = [], items: list = []):
    menu = Menu()
    menu.set_title(title)
    menu.set_items(items)
    option = menu.start_menu()
    return option

def start_system() -> bool:
    title = ([f'{"#"*60}\n', f'{"Bem Vindo Ao Sistema De Votação": ^60}\n',  f'{"#"*60}\n',
            f'{"Para navegar pelo menu utilize as setas do teclado": ^60}\n',
            f'{"E utilize a tecla Enter para interagir com os itens.": ^60}\n'])
    items = (['Efetuar Login', 'Sobre', 'Sair'])
    option = set_menu(title, items)

    if option == 0:
        while login_menu():
            continue
    elif option == 1:
        print('Este projeto tem como objetivo a conclusão da parte introdutória do curso Python Dados e Web cedido pela CEPEDI.')
        print('Ele consiste num sistema de votação, onde temos diferentes tipos de usuários (Candidato e Eleitor).')
        input('Apenas o criador da votação poderá encerrar e computar os votos, cada Eleitor poderá votar apenas 1 única vez.')
    elif option == 2:
        return False

    return True

def login_menu() -> bool:
    option = set_menu(items = ['Acessar sistema', 'Cadastrar', 'Retornar'])
    
    if option == 0:
        user = input('Digite o seu user: ')
        user_db = crud.read_user(user)
        
        if not user_db:
            input("Usuario não encontrado.")
            return True
        
        if not user_db['role']:
            user_db = Voter(user, user_db['password'], user_db['name'], user_db['age'])
        else:
            user_db = Candidate(user, user_db['password'], user_db['name'], user_db['age'], user_db['proposal'])
        
        password = sha256(getpass('Digite o sua senha:').encode('utf-8')).hexdigest()
        if not user_db.validate_password(password):
            input("Senha incorreta")
            return True
        
        while user_menu(user_db):
            continue
    elif option == 1:
        user = {}
        
        user_ = input('Digite um nome de usuário: \n')
        if not user_:
            input("Entrada inválida !\n")
            return True
        user['user'] = user_
        
        password = getpass('Digite uma senha: ')
        if not password:
            input("Entrada inválida !\n")
            return True
        user['password'] = sha256(password.encode('utf-8')).hexdigest()
        
        name = input('Digite seu nome: ')
        if not name:
            input("Entrada inválida !\n")
            return True
        user['name'] = name
        
        age = input('Digite sua idade: ')
        if age.isnumeric():
            user['age'] = int(age)
        else:
            input("Entrada inválida !\n")
            return True
        
        user['role'] = set_menu(items = ['Eleitor', 'Candidato'])
        if user['role']:
            proposal = input('Digite sua proposta: ')
            if not proposal:
                input("Entrada inválida !\n")
                return True
            user['proposal'] = proposal
        if crud.create_user(**user):
            input('Usuário criado com sucesso !\n')
        else:
            input('Usuário já se encontra cadastrado no sistema\n')
    elif option == 2:
        return False
    
    return True

def user_menu(user) -> bool:
    title = [f'Bem vindo {user.name}\n']
    items = ["Votação", "Dados cadastrais", "Retornar"]

    option = set_menu(title, items)
    
    if option == 0:
        while voting_menu(user):
            continue
    elif option == 1:
        print(f'Usuário: {user.user}')
        print(f'Nome: {user.name}')
        print(f'Idade: {user.age}')
    
        if isinstance(user, Candidate):
            print(f'Proposta: {user.proposal}')
    
        input('Para prosseguir digite alguma tecla:\n')

        edit_menu(user)
        
    elif option == 2:
        return False
    
    return True

def edit_menu(user) -> None:
    items = ['Usuário', 'Senha', 'Nome', 'Idade']
    if isinstance(user, Candidate):
        items.append('Proposta')
    items.append('Excluir usuário')
    items.append('Retornar')
        
    option = set_menu(items=items)
    
    print("Caso não queira modificar o campo, deixar em branco.\n")
    
    if option == 0:
        user = input("Digite um nome de usuário: ")
        if user:
            user.user = user
        else:
            return
    elif option == 1:
        password = getpass("Digite uma senha: ")
        if password:
            user.__password__ = sha256(password.encode('utf-8')).hexdigest()
        else:
            return
    elif option == 2:
        name = input("Digite um nome: ")
        if name:
            user.name = name
        else:
            return
    elif option == 3:
        age = input("Digite uma idade: ")
        if age and age.isnumeric():
            user.age = int(age)
        else:
            return
    elif option == 4 and isinstance(user, Candidate):
        proposal = input("Digite uma proposta: ")
        if proposal:
            user.proposal = proposal
        else:
            return
    elif option == 4 and isinstance(user, Voter):
        clear()
        if crud.delete_user(user.user):
            input("Usuário excluido com sucesso !")
            exit()
        else:
            input("Erro ao excluir usuário")
        return
    elif option == 5 and isinstance(user, Candidate):
        clear()
        if crud.delete_user(user.user):
            input("Usuário excluido com sucesso !")
            exit()
        else:
            input("Erro ao excluir usuário")
        return
    else:
        return
    
    user_dict = {
        "user": user.user,
        "password": user.password(),
        "name": user.name,
        "age": user.age,
    }

    if isinstance(user, Candidate):
        user_dict['proposal'] = user.proposal
        user_dict['role'] = 1
    else:
        user_dict['role'] = 0

    if crud.update_user(**user_dict):
        input("Alterações feitas com sucesso ! Aperte alguma tecla para continuar")
    else:
        input("Erro ao alterar dados")
    
    return

def voting_menu(user) -> bool:
    if os.path.exists(PICKLE_PATH):
        with open(PICKLE_PATH, 'rb') as file:
            voting = pickle.load(file)
    else:
        option = set_menu(["Nenhuma votação no momento, deseja iniciar uma ?"], ["Sim", "Não", "Sair"])
        if option == 0:
            voting = Voting(user.user)
            with open(PICKLE_PATH, "wb") as file:
                pickle.dump(voting, file)
            input("Criação concluida !")
            clear()
            return True
        elif option == 1:
            return False
        else:
            exit()
    
    if voting.is_owner(user.user):
        owner_voting(user, voting)
    else:
        title = [f'Bem vindo a votação organizada pelo usuário {voting.owner}.\n']

        if voting.voting_status():
            title.append("A votação ainda não foi iniciada.\n")
            set_menu(title, 'Retornar')
            return False

        option = set_menu(title, ['Votar', 'Retornar'])

        if option == 0:
            vote(user, voting)
            return True
    
    return False

def vote(user, voting: Voting) -> None:
    if user.user in voting.already_voted:
        input("Usuário já votou.\n")
    else:
        usr_name = []
        for item in voting.candidates:
            try:
                usr_name.append([ crud.read_user(item)['name'], crud.read_user(item)['proposal'] ])
            except:
                pass

        items = [f'Candidato: {name}\tProposta: {proposal}' for name, proposal in usr_name]
        option = set_menu(["Selecione o candidato que deseja votar"], items)

        voting.vote(option, user.user)
        input(f'Computado o voto no candidato {usr_name[option][0]} com sucesso')

        with open (PICKLE_PATH, "wb") as file:
            pickle.dump(voting, file)
    
    return

def owner_voting(user, voting: Voting) -> None:
    items = []
    if voting.voting_status():
        items.append("Iniciar a votação")
        items.append("Cadastrar candidatos")
    else:
        items.append('Votar')
        items.append("Encerrar a votação")
    items.append("Retornar")

    option = set_menu(["Votação acessada pelo seu organizador, funções extras disponíveis.\n"], items)
    
    if voting.voting_status():
        if option == 0:
            if len(voting.candidates) > 1:
                voting.start_voting()
                input("Votacão iniciada com sucesso.")
                with open (PICKLE_PATH, "wb") as file:
                    pickle.dump(voting, file)
            else:
                input("Número insuficiente de candidatos.")
        elif option == 1:
            voting.register_candidate(register_menu(voting))
    else:
        if option == 0:
            vote(user, voting)
        elif option == 1:
            close_voting_menu(user, voting)

def close_voting_menu(user, voting: Voting) -> None:
    if len(voting.already_voted) > 1:
        if voting.close_voting(user.user):
            winner, vote_count = voting.winner
            winner = crud.read_user(winner)
            input(f'Parabens {winner["name"]} venceu com {vote_count} voto(s) !')
            os.remove(PICKLE_PATH)
            exit()
        else:
            if voting.draw():
                input('Votação encerrada, houve um empate')
            else:
                input('Erro na votação')
            os.remove(PICKLE_PATH)
            exit()
    else:
        input("Não foi possível prosseguir a votação, apenas 1 voto feito.\n")
        return

def register_menu(voting: Voting) -> None:
    with open('./controller/database.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if len(voting.candidates) > 0:
        title = ["Candidatos já cadastrados no sistema:\n"]
    else:
        title = []

    candidatos_disp = []
    for i, item in data.items():
        if item['role'] == 1:
            if not i in voting.candidates:
                candidatos_disp.append([i, item['name'], item['proposal']])
            else:   
                title += [f'{item["name"]}\n']
                
    if len(voting.candidates) > 0:
        title += ["\n"]

    if len(candidatos_disp) > 0:
        title.append("Temos disponíveis esses candidatos.")
        item = [f'Candidato: {item[1]}\tProposta: {item[2]}' for item in candidatos_disp]
        selected = set_menu(title, item)
    else:
        print(''.join(title))
        input("Não temos disponíveis nenhum candidato.\n")
        return

    voting.register_candidate(candidatos_disp[selected][0])
    with open (PICKLE_PATH, "wb") as file:
        pickle.dump(voting, file)
    
    clear()
    input(f'Candidato {candidatos_disp[selected][1]} cadastrado no sistema com sucesso.')