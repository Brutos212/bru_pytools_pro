def test_envio_de_spam():
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'fabio212@hotmail.com',
        'Curso Python Pro',
        'Confira os Modúlos fantásticos'
    )
