def mijn_functie_2(a,b):
    print(a+b, a-b, a*b, a/b)

'''vraag 5'''
def aanbieding_1(smaak, prijs, korting):
    korting = prijs - (prijs * korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro"
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))

'''vraag 6 en 7'''
inkomsten = 220+430+125+160+205+90+345

def inkomsten_totaal(inkomsten):
    btw =float(0.09) * inkomsten
    uitvoer = f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden."
    return uitvoer

print(inkomsten)
print(inkomsten_totaal(inkomsten))

''' vraag 8'''
mijn_lijst = 220,430,125,160,205,90,345
def laag_en_hoog(mijn_lijst):
    uitvoer = max(mijn_lijst), min(mijn_lijst)
    return uitvoer
print(laag_en_hoog(mijn_lijst))

''' vraag 9 en 10 '''
mijn_lijst = 220 + 430 + 125 + 160 + 205 + 90 + 345
def gemiddelde(mijn_lijst):
    bedrag = mijn_lijst / 7
    uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    return uitvoer

print(gemiddelde(mijn_lijst))

''' vraag 11'''
invoer_lijst = 10, 5, 3, 2, 1, 2, 9
def meervoudig (invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer
print(meervoudig(invoer_lijst))

''' vraag 12'''
def combinatie(invoer_lijst):
    korte_lijst = laag_en_hoog(invoer_lijst)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie(invoer_lijst))
