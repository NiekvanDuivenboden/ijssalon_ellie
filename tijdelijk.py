'''vraag 2'''
prijzen = {
    "Aardbei" : "3",
    "Vanille" : "4",
    "Chocolade" : "5"
}

'''vraag 3'''
aanbieding = 4 * 0.8

'''vraag 4'''
reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}")

'''vraag 5 '''
reclame_tekst2 =  reclame_tekst [:62]

'''vraag 6'''
reclame_tekst3 = reclame_tekst2.upper()

'''vraag 7'''
reclame_tekst4 = reclame_tekst3.split(" ")

'''vraag 8'''
el = reclame_tekst4

'''vraag 9 '''
for item in el:
    print(item.lower())

'''vraag 10'''
for item in el:
    if len(item)>=5:
        print(item.upper())
    else:
        print(item.lower())




