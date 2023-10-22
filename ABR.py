#creo una classe che implementa un albero binario di ricerca (ABR)
class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

class ABR:
    def __init__(self):
            self.root = None

    #ricerca iterativa in albero binario

    def search(self,k):
        x = self.root
        while x != None and k != x.key:
            if k<x.key:
                print("visitato nodo con chiave", x.key)
                x = x.left
            else:
                print("visitato nodo con chiave", x.key)
                x = x.right
        return x

    def insert(self,z):
        x = self.root
        y = None
        while x != None:
            y = x
            if z.key < x.key:
                print("oltrepassato nodo con chiave", x.key)
                x = x.left
            else:
                print("oltrepassato nodo con chiave", x.key)
                x = x.right
        z.p = y
        if y == None: #l'albero era vuoto, allora z fa da radice
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        return z

    def treeMinimum(self,x):
        while x.left != None:
            x = x.left
        return x

    def inorderTreeWalk(self,x):
        if x != None:
            self.inorderTreeWalk(x.left)
            print(x.key)
            self.inorderTreeWalk(x.right)

    def count_nodes(self,x):
        # Caso base: se l'albero è vuoto (radice è None), il numero di nodi è 0.
        if x == None:
            return 0

        # Calcoliamo il numero di nodi nei sotto-alberi sinistro e destro.
        left_count = self.count_nodes(x.left)
        right_count = self.count_nodes(x.right)

        # Il numero totale di nodi nell'albero è la somma dei nodi nei sotto-alberi
        # sinistro e destro, più 1 (per contare il nodo corrente).
        return left_count + right_count + 1