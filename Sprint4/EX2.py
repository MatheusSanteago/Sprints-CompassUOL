def conta_vogaisx(texto: str) -> int:
    vogais = ('aeiouAEIOU')
    texto_vogais = tuple(filter(lambda n: n in vogais, texto))
    return (len(texto_vogais))
