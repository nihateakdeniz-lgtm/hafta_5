import pytest
from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri, sinirla, hafiza
from uzay_oyunu.komutlar import KOMUTLAR, komut

def test_sure_olc():
    @sure_olc
    def ornek_fonk(x):
        return x * 2

    res = ornek_fonk(5)
    assert res == 10
    assert ornek_fonk.__name__=="ornek_fonk"

def test_say():
    @say
    def faktoriyel(n):
        return 1 if n <= 1 else n * faktoriyel(n - 1)
    assert faktoriyel(4) == 24
    assert faktoriyel.cagri > 0

def test_sinirla():
    @sinirla(0, 100)
    def yakit_harca(miktar):
        return 100 - miktar
        assert yakit_harca(30) == 70
    with pytest.raises(ValueError):
        yakit_harca(150)

def test_komutlar():
    @komut("test_komutu", "test aciklama")
    def ornek_komut(durum):
        return "basarili"

    assert "test_komutu" in KOMUTLAR
    func, aciklama = KOMUTLAR["test_komutu"]
    assert aciklama == "test aciklama"
    assert func({}) == "basarili"

    with pytest.raises(ValueError):
        @komut("test_komutu", "tekrar")
        def mukerrer(durum):
            pass