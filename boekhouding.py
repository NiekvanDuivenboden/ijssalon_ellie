import helper
import presentatie
import csv

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

totaal_inkomsten = helper.som(inkomsten)

print(presentatie.presenteer(inkomsten, totaal_inkomsten))

with open('boekhouding.csv', 'w',newline='') as csvfile:
     for key, value in inkomsten.items():
     writer = csv.writer(csvfile, delimter=';')
     writer.writerow([key,value])