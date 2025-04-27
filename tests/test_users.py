from models.user import User

def test_usuario_valido():
    u = User("Wachifr", "23976963@continental.edu.pe")
    assert user.to_dict()["email"] == "23976963@continental.edu.pe"

def test_email_invalido():
    try:
        User("usuario", "correo_invalido.com")
        assert False
    except ValueError:
        assert True
