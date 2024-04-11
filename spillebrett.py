from random import randint
from celle import Celle

class Spillebrett :

    def __init__(self, rader, kolonner) :
    #Setter en variabel _generasjonsnr lik 0 for utskrift senere
        self._generasjonsnr = 0
        self._rader = rader
        self._kolonner = kolonner
        self._brett = []
    #Skal lage en liste for hver rad hvor vi deretter legger objekter lik mengde
    #som antall kolonner
        for antall in range(self._rader) :
            self._noste = []
            for tall in range(self._kolonner) :
                cellen = Celle()
                self._noste.append(cellen)
    #Legger til objekter i nostet liste, også listene inn i hovedliste
            self._brett.append(self._noste)
    #Kaller deretter på generer for å få tilfeldig seed
        self._generer()

    def tegnBrett(self) :
    #Tømmer brettet med 10 linjer
        for p in range(10) :
            print()

    #Nostede for-lokker som printer objektene i et rutenett
        for alleListene in self._brett :
            print("")
            for objektene in alleListene :
                tegn = objektene.hentStatusTegn()
                print(tegn, end=" ")

    #Printer noen linjeskift for pen utskrift, og deretter info om brettet
        print("")
        print("")
        print("Generasjon:", self._generasjonsnr, "Antall levende:", self.finnAntallLevende())

    def oppdatering(self) :
    #Oppretter to lister som skal oppdateres, deretter bruker to for-lokker for
    #å iterere gjennom koordinater
        self._snartLevende = []
        self._snartDod = []
        for rad in range(self._rader) :
            for kolonne in range(self._kolonner) :
    #Oppretter nabo-variabel og teller for hvert koordinat
                naboer = self.finnNabo(rad, kolonne)
                teller = 0
    #Sjekk for levende celler. Kunne nok droppet å inkludere is True, siden den
    #allerede returnerer True. Øker teller for hver levende nabo.
                if (self._brett[rad][kolonne]).erLevende() is True :
                    for sjekk in naboer :
                        if sjekk.erLevende() is True :
                            teller +=1
    #Hvis antall levende naboer ikke er 2 eller 3 legges det i listen for oppdatering
                    if teller != (2 or 3) :
                        self._snartDod.append((self._brett[rad][kolonne]))
    #Sjekk for døde celler, med samme fremgangsmåte som overfor
                if (self._brett[rad][kolonne]).erLevende() is False :
                    for sjekk in naboer :
                        if sjekk.erLevende() is True :
                            teller += 1
                    if teller == 3 :
                        self._snartLevende.append((self._brett[rad][kolonne]))
    #Oppdaterer objekter som skal dø/leve, printer deretter info om generasjon
        for celle in self._snartDod :
            celle.settDoed()
        for celle in self._snartLevende :
            celle.settLevende()
        self._generasjonsnr += 1
        print("Generasjon:", self._generasjonsnr, "Antall levende:", self.finnAntallLevende())

    def finnAntallLevende(self) :
    #Finner antall levende ved å iterere
        antallLevende = 0
        for l in self._brett :
            for celle in l :
                if celle.erLevende() is True :
                    antallLevende += 1
        return antallLevende

    def _generer(self) :
    #Random seed ved nostede lokker
        for l in self._brett :
            for dodcell in l :
                sannsynlighet = randint(0,3)
                if sannsynlighet == 3 :
                    dodcell.settLevende()

    def finnNabo(self, rader, kolonner) :
    #Ved å sette opp "koordinater" for naboene finner man at koordinatene varierer
    #1 opp og 1 ned, så derfor den rangen.
        self._naboer = []
        for lister in range(-1, 2) :
            for celler in range(-1, 2) :
    #Iterer og oppretter to variabler
                naboA = rader + lister
                naboB = kolonner + celler
    #To if-sjekker for å fastsette at nabo ikke er seg selv, og ikke utenfor
    #brettet.
                if (naboA == rader and naboB == kolonner) is False :
                    if (naboA < 0 or naboA > (self._rader-1) or naboB < 0 or naboB > (self._kolonner-1)) is False :
                        self._naboer.append(self._brett[naboA][naboB])
        return self._naboer
