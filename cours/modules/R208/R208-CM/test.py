class Personne:

  race = "humain"

  def __init__(self, nom):
    self.nom = nom


p1 = Personne("Thibault")
p2 = Personne("Jean")

print(p1.nom, p2.nom, f"R1: {p1.race}, R2: {p2.race}, P-Gloabl: {Personne.race}")
