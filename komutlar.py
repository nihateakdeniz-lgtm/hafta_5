KOMUTLAR = {}
def komut(ad, aciklama=""):
    def dekorator(func):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten kayıtlı!")
        KOMUTLAR[ad]= (func, aciklama)
        return func
    return dekorator

@komut("yardim", "komutları listeler")
def komut_yardim(durum):
    cikti = []
    for ad, (func, aciklama) in KOMUTLAR.items():
        cikti.append(f"{ad}: {aciklama}")
    return "\n".join(cikti)
@komut("envanter", "envanter eşyalarını gösterir")
def komut_envanter(durum):
    return f"Credits: {durum.get('credits', 0)}, Engines: {durum.get('engines', [])}, Copilot: {durum.get('copilot', 'Yok')}"
@komut("harita", "gidebileceğin gezegenleri gösterir")
def komut_harita(durum):
    baglantilar = durum.get('baglantilar', [])
    return ", ".join(baglantilar)
