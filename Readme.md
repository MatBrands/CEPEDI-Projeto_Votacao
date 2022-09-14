# Projeto Votação em Python
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

Este projeto tem como objetivo a conclusão da parte introdutória do curso Python Dados e Web cedido pela CEPEDI.
Ele consiste num sistema de gerenciamento de votação, onde temos diferentes níveis de acesso (Criador, Candidato e Votante). Apenas o criador da votação poderá encerrar e computar os votos, cada pessoa poderá votar apenas 1 única vez.

Conteúdo:
- Tecnologias
- Instalação
- Instruções
- Autores
- License

## Tecnologias

Esse projeto utiliza algumas bibliotecas:

- [termcolor] - Modificar a coloração do console
- [pynput] - Obter evento de keyboard
- [json] - Manipulação de jsons
- [hashlib] - Utilização de criptografias do tipo hash
- [getpass] - Utilização de inputs escondidos para senhas
- [pickle] - Importar objetos inteiros
- [os] - Limpar tela e excluir arquivos

## Instalação

No desenvolvimento foi utilizado o [Python](https://www.python.org/) v3.10.6.

Para instalar as dependencias recomenda-se o uso de um ambiente virtual, assim acesse o diretório do ambiente, ative-o e instale:

```sh
pip install virtualenv
virtualenv env
source env/bin/activate
pip freeze > ./tools/requirements.txt
```

Para desativar utilize:

```sh
deactivate
```

Então apenas chame a main normalmente

```sh
python __init__.py
```

## Instruções

O projeto foi desenvolvido de maneira interativa pelo terminal, ou seja, o usuário vai interagir diretamente com o terminal.
Para interagir com os menus é necessário utilizar as Setas para percorrer os itens e o Enter para acessar.
Para os itens de texto, será necessário apenas digitar os valores e dar Enter.

## Autores

Projeto desenvolvido com a colaboração dos Devs:

- [Luca Sacramento](https://github.com/lucasao98/)
- [Matheus Brandão](https://github.com/MatBrands)

## License

MIT
