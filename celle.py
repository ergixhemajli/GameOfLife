class Celle :

#Celle-klasse med metoder som henter/sjekker/endrer status.
    def __init__(self) :
        self._status = 'død'

    def settDoed(self) :
        self._status = 'død'

    def settLevende(self) :
        self._status = 'levende'

    def erLevende(self) :
        if self._status == 'levende' :
            return True
        elif self._status == 'død' :
            return False

    def hentStatusTegn(self) :
        if self._status == 'levende' :
            return 'O'
        elif self._status == 'død' :
            return '.'
