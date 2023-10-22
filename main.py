#importo le librerie create
from LinkedList import *
from ABR import *
from hashTable import *
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

def testLinkedList(numTests,dimMax,numToInsert,numToSearch):
    resultInsertLinkedListTot = []
    resultSearchLinkedListTot = []
    for i in range (numTests):
        myList = linkedList()
        K = []
        for i in range (dimMax):
            K.append(i)
        alreadyInserted = []

        resultInsertLinkedList = []
        resultSearchLinkedList = []

        while myList.count() < dimMax:
            keysToInsert = []
            keysToSearch = []
            #scelgo numToInsert chiavi da aggiungere alla lista prese a caso tra quelle disponibili in K
            for i in range (numToInsert):
                index = random.randint(0,len(K)-1)
                keysToInsert.append(K[index])
                alreadyInserted.append(K[index])
                K.remove(K[index])
            #scelgo numToSearch chiavi da cercare nella lista prese a caso tra quelle già inserite
            for i in range (numToSearch):
                index = random.randint(0,len(alreadyInserted)-1)
                keysToSearch.append(alreadyInserted[index])

            startTimeStamp = timer()
            for i in range (len(keysToInsert)):
                myList.insert(element(keysToInsert[i]))
            endTimeStamp = timer()
            resultInsertLinkedList.append((endTimeStamp - startTimeStamp)*1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myList.search(keysToSearch[i])
            endTimeStamp = timer()
            resultSearchLinkedList.append((endTimeStamp - startTimeStamp)*1000)

        resultInsertLinkedListTot.append(resultInsertLinkedList)
        resultSearchLinkedListTot.append(resultSearchLinkedList)


    resultInsertToDisplay = [0 for i in range (len(resultInsertLinkedListTot[0]))]
    for i in range (len(resultInsertLinkedListTot)):
        for j in range (len(resultInsertLinkedListTot[i])):
            resultInsertToDisplay[j]+= resultInsertLinkedListTot[i][j]

    for i in range (len(resultInsertToDisplay)):
        resultInsertToDisplay[i] = resultInsertToDisplay[i]/numTests

    resultSearchToDisplay = [0 for i in range(len(resultSearchLinkedListTot[0]))]
    for i in range(len(resultSearchLinkedListTot)):
        for j in range(len(resultSearchLinkedListTot[i])):
            resultSearchToDisplay[j] += resultSearchLinkedListTot[i][j]

    for i in range (len(resultSearchToDisplay)):
        resultSearchToDisplay[i] = resultSearchToDisplay[i]/numTests

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, resultInsertToDisplay, label="LinkedList insert ", color="orange")
    plot1.plot(x_axis, resultSearchToDisplay, label="LinkedList search ", color="green")
    plot1.set_title("Risultati per Insert e Search implementati con la Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione struttura dati")
    plt.show()
def testABR(numTests, dimMax, numToInsert, numToSearch):
    resultInsertABRTot = []
    resultSearchABRTot = []
    for i in range (numTests):
        myTree = ABR()
        K = []
        for i in range (dimMax):
            K.append(i)
        alreadyInserted = []

        resultInsertABR = []
        resultSearchABR= []

        while myTree.count_nodes(myTree.root) < dimMax:
            keysToInsert = []
            keysToSearch = []
            #scelgo numToInsert chiavi da aggiungere all'albero prese a caso tra quelle disponibili in K
            for i in range (numToInsert):
                index = random.randint(0,len(K)-1)
                keysToInsert.append(K[index])
                alreadyInserted.append(K[index])
                K.remove(K[index])
            #scelgo numToSearch chiavi da cercare nell'albero prese a caso tra quelle già inserite
            for i in range (numToSearch):
                index = random.randint(0,len(alreadyInserted)-1)
                keysToSearch.append(alreadyInserted[index])

            startTimeStamp = timer()
            for i in range (len(keysToInsert)):
                myTree.insert(node(keysToInsert[i]))
            endTimeStamp = timer()
            resultInsertABR.append((endTimeStamp - startTimeStamp)*1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myTree.search(keysToSearch[i])
            endTimeStamp = timer()
            resultSearchABR.append((endTimeStamp - startTimeStamp)*1000)

        resultInsertABRTot.append(resultInsertABR)
        resultSearchABRTot.append(resultSearchABR)


    resultInsertToDisplay = [0 for i in range (len(resultInsertABRTot[0]))]
    for i in range (len(resultInsertABRTot)):
        for j in range (len(resultInsertABRTot[i])):
            resultInsertToDisplay[j]+= resultInsertABRTot[i][j]

    for i in range (len(resultInsertToDisplay)):
        resultInsertToDisplay[i] = resultInsertToDisplay[i]/numTests

    resultSearchToDisplay = [0 for i in range(len(resultSearchABRTot[0]))]
    for i in range(len(resultSearchABRTot)):
        for j in range(len(resultSearchABRTot[i])):
            resultSearchToDisplay[j] += resultSearchABRTot[i][j]

    for i in range (len(resultSearchToDisplay)):
        resultSearchToDisplay[i] = resultSearchToDisplay[i]/numTests

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, resultInsertToDisplay, label="ABR insert ", color="orange")
    plot1.plot(x_axis, resultSearchToDisplay, label="ABR search ", color="green")
    plot1.set_title("Risultati per Insert e Search implementati con albero binario di ricerca")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione struttura dati")
    plt.show()

def testHashTable(numTests, dimMax, numToInsert, numToSearch):
    resultInsertHashTableTot = []
    resultSearchHashTableTot = []
    for i in range (numTests):
        myTable = hashTable(dimMax)
        K = []
        for i in range (dimMax):
            K.append(i)
        alreadyInserted = []

        resultInsertHashTable = []
        resultSearchHashTable= []

        while len(alreadyInserted) < dimMax:
            keysToInsert = []
            keysToSearch = []
            #scelgo numToInsert chiavi da aggiungere all'albero prese a caso tra quelle disponibili in K
            for i in range (numToInsert):
                index = random.randint(0,len(K)-1)
                keysToInsert.append(K[index])
                alreadyInserted.append(K[index])
                K.remove(K[index])
            #scelgo numToSearch chiavi da cercare nell'albero prese a caso tra quelle già inserite
            for i in range (numToSearch):
                index = random.randint(0,len(alreadyInserted)-1)
                keysToSearch.append(alreadyInserted[index])

            startTimeStamp = timer()
            for i in range (len(keysToInsert)):
                myTable.insert(keysToInsert[i])
            endTimeStamp = timer()
            resultInsertHashTable.append((endTimeStamp - startTimeStamp)*1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myTable.search(keysToSearch[i])
            endTimeStamp = timer()
            resultSearchHashTable.append((endTimeStamp - startTimeStamp)*1000)

        resultInsertHashTableTot.append(resultInsertHashTable)
        resultSearchHashTableTot.append(resultSearchHashTable)


    resultInsertToDisplay = [0 for i in range (len(resultInsertHashTableTot[0]))]
    for i in range (len(resultInsertHashTableTot)):
        for j in range (len(resultInsertHashTableTot[i])):
            resultInsertToDisplay[j]+= resultInsertHashTableTot[i][j]

    for i in range (len(resultInsertToDisplay)):
        resultInsertToDisplay[i] = resultInsertToDisplay[i]/numTests

    resultSearchToDisplay = [0 for i in range(len(resultSearchHashTableTot[0]))]
    for i in range(len(resultSearchHashTableTot)):
        for j in range(len(resultSearchHashTableTot[i])):
            resultSearchToDisplay[j] += resultSearchHashTableTot[i][j]

    for i in range (len(resultSearchToDisplay)):
        resultSearchToDisplay[i] = resultSearchToDisplay[i]/numTests

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, resultInsertToDisplay, label="Hash Table insert ", color="orange")
    plot1.plot(x_axis, resultSearchToDisplay, label="Hash Table search ", color="green")
    plot1.set_title("Risultati per Insert e Search implementati con Hash Table")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione struttura dati")
    plt.show()

if __name__ == '__main__':
    numTests = 1000
    dimMax = 1000
    dimToInsert = dimToSearch = 20
    #testLinkedList(numTests, dimMax, dimToInsert, dimToSearch)
    #testABR(numTests, dimMax, dimToInsert, dimToSearch)
    testHashTable(numTests, dimMax, dimToInsert, dimToSearch)



