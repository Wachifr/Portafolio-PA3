from models.post import Post

def test_post_valido():
    post = Post("Mi TDD", "Muy útil para software profesional", "carlosv")
    assert post.resumen().startswith("Muy útil")

def test_post_titulo_corto():
    try:
        Post("Hey", "Texto", "carlosv")
        assert False
    except ValueError:
        assert True
