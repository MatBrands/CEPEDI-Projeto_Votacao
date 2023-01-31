# Projeto Votação
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

Este projeto tem como objetivo a conclusão da parte introdutória do curso Python Dados e Web cedido pela CEPEDI.
Ele consiste num sistema de gerenciamento de votação, onde temos diferentes níveis de acesso (Candidato e Votante). Apenas o criador da votação poderá encerrar e computar os votos, cada pessoa poderá votar apenas 1 única vez.

Conteúdo:
- Tecnologias
- Instalação
- Instruções
- Autores
- Organização do projeto
- License

## Tecnologias
Esse projeto utiliza algumas bibliotecas:

- getpass - Inputs escondidos para senhas
- hashlib - Criptografias do tipo hash para senhas
- json - Manipulação de jsons
- os - Limpar tela e excluir arquivos
- platform - Identificar o sistema operacional
- pickle - Importar objetos inteiros
- pynput - Obter evento de keyboard
- termcolor - Modificar a coloração do console

## Instalação
Foi utilizado o [Python](https://www.python.org/) v3.10.9.

### Conda
No desenvolvimento foi utilizado o gerenciador de pacotes e ambientes [Conda](https://conda.io/). Portanto para prosseguir necessita-se de sua [instalação](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
conda env create -f environment.yml
```

- Ativar
```sh
conda activate voting_system_venv
```

- Desativar
```sh
conda deactivate
```

### Requirements
Pode-se utilizar o arquivo requirements.txt para criar o ambiente virtual.

- Criar ambiente virtual
```sh
python -m venv voting_system_venv
```

- Ativar
```sh
source ./voting_system_venv/bin/activate
```

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
pip install -r requirements.txt
```

- Desativar
```sh
deactivate
```

### Inicializar projeto
- Navegar até a pasta de destino
```sh
cd voting_system
```

- Execute o programa
```sh
python __init__.py
```

## Instruções
O projeto foi desenvolvido de maneira interativa pelo terminal, ou seja, o usuário vai interagir diretamente com o terminal.
Para interagir com os menus é necessário utilizar as 'Setas' para percorrer os itens e o 'Enter' para acessar.
Para os itens de texto, será necessário apenas digitar os valores e dar 'Enter'.

## Autores
Projeto desenvolvido com a colaboração dos Devs:

- [Luca Sacramento](https://github.com/lucasao98/)
- [Matheus Miranda Brandão](https://github.com/MatBrands)

## Organização do projeto
```sh
├── CEPEDI-Projeto_Votacao
|   ├── License
|   ├── Readme.md
|   ├── utils
|   │   ├── environment.yml
|   │   └── requirements.txt
|   └── voting_system
|   |   ├── Readme.md
|   |   ├── __init__.py
|   |   ├── controller
|   |   │   └── database.json
|   |   ├── model
|   |   │   ├── Menu.py
|   |   │   ├── Register.py
|   |   │   ├── Users.py
|   |   │   └── Voting.py
|   |   └── view
|   |       └── interface.py
```

## License
MIT