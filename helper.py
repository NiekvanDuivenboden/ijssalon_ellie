def decoreer(tekst=""):
    tekst="header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

    #bedrag: het totaalbedrag van alle fooi
    #personen: het aantal personen waarover het bedrag verdeeld moet worden
def fooi_pp(bedrag, personen):
      bedrag_pp = bedrag/personen
      return f"het bedrag per persoon is {bedrag_pp} euro"

def onderstreep(tekst=""):
     uit=[]
     uit.append(tekst)
     uit.append(len(tekst) * "=")
     return uit

def som(inkomsten):
    return(sum(inkomsten.values()))
