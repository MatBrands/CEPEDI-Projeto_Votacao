# Projeto Votação em Python
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

Este projeto tem como objetivo a conclusão da parte introdutória do curso Python Dados e Web cedido pela CEPEDI.
Ele consiste num sistema de gerenciamento de votação, onde temos diferentes níveis de acesso (Criador, Candidato e Votante). Apenas o criador da votação poderá encerrar e computar os votos, cada pessoa poderá votar apenas 1 única vez.

Conteúdo:
- Recomendações
- Lista de requisitos a ser atendidos
- Funcionalidades e responsável
- Tecnologias
- Instalação
- Autores
- License

## Recomendações
- Cada desenvolvedor terá sua branch para ficar a vontade para inserir novas funcionalidades ao projeto.
- Ao desenvolver uma nova funcionalidade o dev deverá solicitar o Pull Request comentando o que foi feito.
- Em relação aos commits será utilizado um padrão
    - Commits de novas features. Ex: git commit -m "New: Controller de usuario"
    - Commits de correção. Ex: git commit -m "Fix: Correção do model"
    - Commits de updates. Ex: git commit -m "Update: Readme"
    - Commits de remoção. Ex: git commit -m "Removed: Cálculo do tempo de votação"

### Lista de requisitos a ser atendidos
- [x] Executar no Console
- [x] Pelo menos 1 menu de opções
- [ ] Pelo menos 1 CRUD
- [ ] Salvar e carregar informações em arquivos JSON
- [ ] Pelo menos 1 módulo/pacote
- [ ] Pelo menos 2 classes
- [ ] Pelo menos 1 herança entre Classes

## Funcionalidades e responsável

Para melhor controle será dividido o desenvolvimento em fragmentos que serão integrados ao projeto, onde cada dev será responsável por uma parte.

| Feature | Dev | Progresso
| ------ | ------ | ------ |
| Criação de menu dinâmico | Matheus Brandão | Conclusão
| ... | Luca Sacramento | Em desenvolvimento
| ... | Roberto Goes | Pendente

## Tecnologias

Esse projeto utiliza algumas bibliotecas:

- [termcolor] - Modificar a coloração do console
- [pynput] - Obter evento de keyboard

## Instalação

No desenvolvimento foi utilizado o [Python](https://www.python.org/) v3.10.6.

Para instalar as dependencias acesse o diretório do ambiente, ative-o e instale:

```sh
cd ENV
bin/activate
pip install -r ./dependencies/requirements.txt
```

Então apenas chame a main normalmente

```sh
python __init__.py
```

## Autores

Projeto desenvolvido com a colaboração dos Devs:

- [Luca Sacramento](https://github.com/lucasao98/)
- [Matheus Brandão](https://github.com/MatBrands)
- [Roberto Góes]()

## License

MIT