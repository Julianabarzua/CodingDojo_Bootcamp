import Ninja as nj
import Pet as pt

roque = pt.Dog("Roque", "dog", "meatballs")
jose = nj.Ninja("Jose Pablo", "Severin", 5, "meatballs", roque)

belu = pt.Cat("Beluga", "cat", "fish")
marti = nj.Ninja("Martina","Knitle", 15, "vegan", belu)

jose.walk()
jose.feed()
jose.bath()

marti.walk()
marti.feed()
marti.bath()

print(roque.energy, roque.health)
print(belu.energy, belu.health)