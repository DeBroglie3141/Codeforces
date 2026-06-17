def decoder(message, decalage):
    """
    Décode un message en reculant chaque lettre de 'decalage' positions.
    Les espaces et la ponctuation ne changent pas.
    Les majuscules restent des majuscules.
    """
    resultat = ""

    for c in message:
        if 'a' <= c <= 'z':
            nouvelle_lettre = chr((ord(c) - ord('a') - decalage) % 26 + ord('a'))
            resultat += nouvelle_lettre

        elif 'A' <= c <= 'Z':
            nouvelle_lettre = chr((ord(c) - ord('A') - decalage) % 26 + ord('A'))
            resultat += nouvelle_lettre

        else:
            resultat += c

    return resultat