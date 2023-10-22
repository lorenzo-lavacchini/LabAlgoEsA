import LinkedList
from LinkedList import element
from LinkedList import linkedList
import numpy as np
import math


class hashTable:

    # m -> grandezza della tabella
    # n -> numero di chiavi da memorizzare nella tabella (cardinalità di K)
    # negli algoritmi, il valore NIL sarà sostituito dal valore -1 per comododità
    def __init__(self, n):
        self.m = math.ceil((n / 0.8))
        self.T = np.full(self.m, -1)

    def hashFunction(self, k, i):
        return ((k % self.m + i)) % self.m

    def insert(self, k):
        i = 0
        while i != self.m:
            j = self.hashFunction(k, i)
            if self.T[j] == -1:
                self.T[j] = k
                return j
            else:
                i = i + 1
        print("tavola piena, errore")

    def search(self, k):
        i = 0
        while i < self.m:
            j = self.hashFunction(k, i)
            if self.T[j] == k:
                return j
            i += 1
            if self.T[j] == -1:
                break
        print("non è stato trovata la chiave cercata")
        return -1

    def printHashTable(self):
        for i in self.T:
            print(self.T[i])
