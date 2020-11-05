import pytest
from lib_python_est.spam.modelos import Usuario


# @pytest.fixture(scope='module')


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Santos', email='santos212@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Santos', email='santos212@hotmail.com'),

        Usuario(nome='Silva', email='santos212@hotmail.com')

    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
