import sys
import pickle
# from Projeto_Votacao.votacao.interface.votacaoClass import *
# from Projeto_Votacao.votacao.interface.usersClass import *
sys.path.insert(1, '../')
from interface.usersClass import *
from interface.votacaoClass import *

if __name__ == '__main__':
    # user_1 = Eleitor('Matheus_Mbr', '123456', 'Matheus Brandão', 23)
    # user_2 = Eleitor('LucaSao', '123456', 'Luca Sacramento', 24)
    # user_3 = Candidato('Ericsx', '123456', 'Eric Soares', 'Bolsa Nega', 22)
    # user_4 = Candidato('zDarkness', '123456', 'Darley Sampaio', 'Bolsa DST', 42)
    # user_5 = Candidato('Abelhinha', '123456', 'Abelha Vesponilde', 'Bolsa Picada', 666)

    # votacao = Votacao(user_1)
    # print (votacao.organizador)
    # print (votacao.verificaOrganizador(1))
    # print (votacao.candidatos)

    # votacao.setCandidato(user_1)
    # votacao.setCandidato(user_2)
    # votacao.setCandidato(user_3)
    # # votacao.iniciarVotacao()
    # votacao.setCandidato(user_4)
    # votacao.setCandidato(user_5)
    # print ([item.getName() for item in votacao.candidatos])

    # votacao.iniciarVotacao()

    # votacao.votar (0, user_1)
    # votacao.votar (0, user_1)
    # votacao.votar (0, user_1)
    # votacao.votar (0, user_1)
    # votacao.votar (0, user_1)

    # with open ("test.pkl", "wb") as file:
    #     pickle.dump(votacao, file)

    # -------------------------------------------

    with open ("test.pkl", "rb") as file:
        votacao = pickle.load(file)

    print (votacao.organizador.getName())
    print (votacao.verificaOrganizador("Matheus_Mbr"))
    print ([item.getName() for item in votacao.candidatos])

    # print (votacao.encerrarVotacao("Matheus_Mbr"))
    
    # vencedor, votos = votacao.vencedor

    # print (vencedor, votos)