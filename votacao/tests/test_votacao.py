import sys
# from Projeto_Votacao.votacao.interface.votacaoClass import *
# from Projeto_Votacao.votacao.interface.usersClass import *
sys.path.insert(1, '../interface')
from usersClass import *
from votacaoClass import *

if __name__ == '__main__':
    user_1 = Eleitor(1, 'Matheus_Mbr', '123456', 'Matheus Brandão')
    user_2 = Eleitor(2, 'LucaSao', '123456', 'Luca Sacramento')
    user_3 = Candidato(3, 'Ericsx', '123456', 'Eric Soares', 'Bolsa Nega')
    user_4 = Candidato(4, 'zDarkness', '123456', 'Darley Sampaio', 'Bolsa DST')
    user_5 = Candidato(5, 'Abelhinha', '123456', 'Abelha Vesponilde', 'Bolsa Picada')

    votacao = Votacao(user_1)
    print (votacao.organizador)
    print (votacao.verificaOrganizador(1))
    print (votacao.candidatos)

    votacao.setCandidato(user_1)
    votacao.setCandidato(user_2)
    votacao.setCandidato(user_3)
    # votacao.iniciarVotacao()
    votacao.setCandidato(user_4)
    votacao.setCandidato(user_5)
    print ([item.getName() for item in votacao.candidatos])

    votacao.iniciarVotacao()

    votacao.votar (0, user_1)
    votacao.votar (0, user_1)
    votacao.votar (0, user_1)
    votacao.votar (0, user_1)
    votacao.votar (0, user_1)

    print (votacao.candidatos[0].getContagem())

    votacao.encerrarVotacao(1)

    print(votacao.vencedor.getName())