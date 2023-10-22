#creo una classe element che rappresenta un elemento della lista concatenata con puntatori
class element:
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None

#creo la classe della lista (la lista viene create vuota)
class linkedList:
    def __init__(self):
        self.head=None

    #inserimento elemento in testa alla lista
    def insert(self,x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    #ricerca di un elemento nella lista
    def search(self,k):
        #utilizzo x per scorrere la lista
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x

    # stampa tutte le chiavi degli elementi nella lista
    def printAll(self):
        keys = []  # array con le chiavi da stampare
        if self.head == None:
            print("Lista vuota")
        else:
            x = self.head
            while x != None:
                keys.append(x.key)
                x = x.next
        print(keys)

    #creo un metodo per sapere il conteggio di quante cose ho inserito nella lista
    def count(self):
        x = self.head
        count = 0
        while x != None:
            count += 1
            x = x.next
        return count