def decoder(message, decalage):
    resultat = ""
    for c in message:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultat += chr((ord(c) - base - decalage) % 26 + base)
        else:
            resultat += c
    return resultat
    
def decoder_message(message_code, decalage):
    """
    Décode un message où chaque mot a été :
    1. inversé
    2. décalé de 'decalage' positions
    Pour décoder : reculer les lettres, puis inverser chaque mot.
    """
    resultat = ""
    for mot in message_code.split():
        resultat += decoder(mot[::-1], decalage) + " "
    return resultat[:-1]