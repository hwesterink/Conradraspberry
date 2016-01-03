import random
getal = random.randrange(1000); tip = 0; i = 0
while tip != getal:
    tip = input("Jouw keuze:")
    if getal < tip:
        print "Het gezochte getal is kleiner dan ", tip
    if getal > tip:
        print "Het gezochte getal is groter dan ", tip
    i += 1
print "Je hebt het getal bij de ",i," keuze geraden!"

        
