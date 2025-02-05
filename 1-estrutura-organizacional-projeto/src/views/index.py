import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controllers.pessoa import PessoaController
from models.pessoa import Pessoa

while True:
    decisao =  int(input('Digite 1 para salvar e 2 para listar: '))

    if decisao == 1:
        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        idade = input('Idade: ')
        cpf = input('Cpf: ')

        p1 = Pessoa(nome=nome, sobrenome=sobrenome, idade=idade, cpf=cpf)
        PessoaController.salvar_pessoa(p1)

    elif decisao == 2:
        for i in PessoaController.listar_pessoa():
            print(f'Nome: {i.nome}')