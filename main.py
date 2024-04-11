from spillebrett import Spillebrett

def main() :
#Starter med å spørre om størrelse på brettet
    rad = int(input("Hvor mange rader vil du ha? "))
    kolonne = int(input("Hvor mange kolonner vil du ha? "))
    brettet = Spillebrett(rad, kolonne)
#Tegner brettet før vi går inn i en loop hvor man kan trykke enter for å fortsette
    brettet.tegnBrett()
    nesteSteg = input("Trykk enter for å fortsette, eller 'q' for å avslutte ")
    while nesteSteg == ("" and not "q") :
        oppdatering = brettet.oppdatering()
        brettet.tegnBrett()
        nesteSteg = input("Trykk enter for å fortsette, eller 'q' for å avslutte ")

main()
