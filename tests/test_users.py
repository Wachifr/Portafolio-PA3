from models.user import User

def test_usuario_valido():
    u = User("luis", "luis@correo.com")
    assert u.to_dict()["email"] == "luis@correo.com"

def test_email_invalido():
    try:
        User("ana", "anacorreo.com")
        assert False
    except ValueError as e:
        assert "no válido" in str(e)
