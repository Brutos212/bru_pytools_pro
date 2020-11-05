from unittest.mock import Mock

import pytest

from lib_python_est.spam.enviador_de_email import Enviador
from lib_python_est.spam.main import EnviadorDeSpam
from lib_python_est.spam.modelos import Usuario



@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Santos', email='santos212@hotmail.com'),
            Usuario(nome='Silva', email='santos212@hotmail.com')

        ],
        [
            Usuario(nome='Santos', email='santos212@hotmail.com')
        ],
    ]
)
# def test_envio_de_spam(sessao, usuarios):

def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'santos212@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Santos', email='santos212@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'silva212@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'silva212@hotmail.com',
        'santos212@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
