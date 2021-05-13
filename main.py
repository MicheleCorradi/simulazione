import sqlite3

#mi connetto al batabase
conn = sqlite3.connect('immobili.db')
#conn.execute('CREATE TABLE immobile (immobileid INTEGER PRIMARY KEY, propietario, indirizzo, prezzo, catalogo)')
#conn.execute('CREATE TABLE Catalogo (catalogoid INTEGER PRIMARY KEY, nome, prezzomin, prezzomax)')
curs = conn.cursor()
curs.execute('insert into immobile values (?,?, ?, ?, ?)', (1,"michele","via mincio",20000, "Catalogo_prestigio"))
#curs.execute('insert into Catalogo values (?, ?, ?)', ("di prestigio", 10000, 40000))
class Catalogo():

    def __init__(self,nome,prezzomin,prezzomax):
        self.nome = nome 
        self.prezzomin = prezzomin 
        self.prezzomax= prezzomax
        self.lista = []

    def inserisci(self,immobile):
        self.lista.append()
        print("L' immobile é stato aggiunto al catalogo")




class Immobile():

    def __init__(self,propietario,indirizzo,prezzo,catalogo):
        self.propietario = propietario
        self.indirizzo = indirizzo
        self.prezzo = prezzo
        self.catalogo = catalogo

    def inserimento(self, lista):
        lista.append(self)
        print("L'immobile é stato inserito!")


    def cancellazione(self,lista):
        lista.remove(self)
        print("L'immobile é stato rimosso!")

    def modifica(self):
        nuovo_prop = str(input("Inserisci il nuovo riferimento proprietario: "))
        if nuovo_prop != "":
            self.propietatio = nuovo_prop
        
        nuovo_indirizzo = str(input("Inserisci il nuovo indirizzo: "))
        if nuovo_indirizzo != "":
            self.indirizzo = nuovo_indirizzo
        
        nuovo_prezzo = str(input("Inserisci il nuovo prezzo: "))
        if nuovo_prezzo != "":
            self.prezzo = nuovo_prezzo
    
    def cancellazione(self, lista):
        lista.remove(self)
        print("L'immobile è stato rimosso con successo!\n")

    def stampa(self):
        print(f"Propietario :{self.propietario} \nIndirizzo :{self.indirizzo} \nPrezzo :{self.prezzo}")

    def ricerca(self):
        ric_indirizzo = str(input("Inserisci l'indirizzo dell'immobile:"))
        for imm in lista_immobili:
            if imm.indirizzo == ric_indirizzo:
                imm.stampa()
            else:
                print("L'immobile non é presente!")

lista_immobili = []

Catalogo_prestigio= Catalogo("di prestigio", 10000, 40000)
Catalogo_vacanza= Catalogo("vacanza", 30000, 50000)



mioImmobile= Immobile("michele","via mincio",20000, "Catalogo_prestigio")


mioImmobile.inserimento(lista_immobili)
#mioImmobile.modifica()

for i in lista_immobili:
    i.stampa()


mioImmobile.ricerca()        