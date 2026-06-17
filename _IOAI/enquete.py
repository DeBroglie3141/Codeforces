import pandas as pd

t_debut = 1296000
t_fin = 1299600

badges = badges.copy()
badges["etage"] = badges["porte"].str.split("-").str[0].astype(int)

badge_3e = badges[
    (badges["etage"] == 3) &
    (badges["timestamp"].between(t_debut, t_fin))
]
suspects_3e = set(badge_3e["employe_id"])

emails_suspects = emails[
    (emails["sujet"].str.contains("confidentiel", case=False, na=False)) &
    (emails["timestamp"].between(t_debut - 86400, t_debut))
]
suspects_email = set(emails_suspects["expediteur_id"])

badges_crime = badges[
    badges["timestamp"].between(t_debut, t_fin)
]

autres_etages = set(
    badges_crime[badges_crime["etage"] != 3]["employe_id"]
)

coupable = (
    set(suspects)
    & suspects_3e
    & suspects_email
) - autres_etages

print(next(iter(coupable)))