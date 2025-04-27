from models.post import Post

def test_post_valido():
    post = Post("Mi TDD", "Muy útil para software profesional", "Wachifr")
    assert post.resumen().startswith("Muy útil")

def test_post_titulo_corto():
    try:
        Post("Hey", "Texto", "Wachifr")
        assert False
    except ValueError:
        assert True
