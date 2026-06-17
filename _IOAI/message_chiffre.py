def frequences(texte):
    """
    Retourne un dictionnaire {lettre: nombre} pour chaque lettre
    présente dans le texte (en minuscule, lettres uniquement).
    """
    freq = {}
    for c in texte:
        if c.isalpha():
            c = c.lower()
            if c in freq:
                freq[c] +=1
            else:
                freq[c] = 1
    return freq
