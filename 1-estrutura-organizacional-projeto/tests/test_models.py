import sys
sys.path.append(".")
from src.models import pessoa

def test_concatenacao_nome_sobrenome():
    p1 = pessoa.Pessoa('Sidney', 'Sperandio', 22, '123456789')
    assert p1.nome_completo() == 'Sidney Sperandio'