def conta_vogaisx(texto: str) -> int:
    texto_vogais = tuple(filter(lambda n: n in ('aeiouAEIOU'), texto))
    return (len(texto_vogais))
