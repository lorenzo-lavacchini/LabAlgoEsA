#importo le librerie create
import time

from LinkedList import *
from ABR import *
from hashTable import *
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import os
import numpy as np

def traceTables(columns: list, headers: tuple, title: str):
    fig, ax = plt.subplots(figsize=(8, 10))

    # Dati per il plot della tabella (è necessario convertire in it is necessary to convert il tutto in un array numpyy)
    data = np.column_stack(columns)

    # Setta il titolo delle tabella
    ax.axis("off")
    table = ax.table(cellText=data, colLabels=headers, loc="center", cellLoc="center")
    table.auto_set_column_width(col=list(range(len(columns))))
    table.scale(1, 1.5)

    # Colora i titoli e le righe pari
    cell_colors = {
        cell: ("#ffd1d1", {"weight": "bold"})
        if table[cell].get_text().get_text() in headers
        else ("#ffe4e4", {})
        for cell in table._cells
        if cell[0] % 2 == 0
    }
    for cell, (color, text_props) in cell_colors.items():
        # setta il colore delle celle
        table[cell].set_facecolor(color)
        # set the text properties of the cell
        table[cell].set_text_props(**text_props)
        # ** used to expand the dictionary

    # save the plot as a png file
    fig.savefig(f"tables/{title}.png", dpi=300, bbox_inches="tight")
    # clear figure for the next plot
    plt.clf()
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
def totalTest(numTests, dimMax, numToInsert, numToSearch):
    resultInsertLinkedListTot = []
    resultSearchLinkedListTot = []
    resultInsertABRTot = []
    resultSearchABRTot = []
    resultInsertHashTableTot = []
    resultSearchHashTableTot = []

    for i in range (numTests):
        myList = linkedList()
        myTree = ABR()
        myTable = hashTable(dimMax)
        K = []
        for i in range (dimMax):
            K.append(i)
        alreadyInserted = []

        resultInsertLinkedList = []
        resultSearchLinkedList = []
        resultInsertABR = []
        resultSearchABR= []
        resultInsertHashTable = []
        resultSearchHashTable = []

        while len(alreadyInserted) < dimMax:
            keysToInsert = []
            keysToSearch = []
            # scelgo numToInsert chiavi da aggiungere all'albero prese a caso tra quelle disponibili in K
            for i in range(numToInsert):
                index = random.randint(0, len(K) - 1)
                keysToInsert.append(K[index])
                alreadyInserted.append(K[index])
                K.remove(K[index])
            # scelgo numToSearch chiavi da cercare nell'albero prese a caso tra quelle già inserite
            for i in range(numToSearch):
                index = random.randint(0, len(alreadyInserted) - 1)
                keysToSearch.append(alreadyInserted[index])

            startTimeStamp = time.perf_counter()
            for i in range(len(keysToInsert)):
                myList.insert(element(keysToInsert[i]))
            endTimeStamp = time.perf_counter()
            resultInsertLinkedList.append((endTimeStamp - startTimeStamp))

            startTimeStamp = time.perf_counter()
            for i in range(len(keysToInsert)):
                myList.search(keysToSearch[i])
            endTimeStamp = time.perf_counter()
            resultSearchLinkedList.append((endTimeStamp - startTimeStamp))

            startTimeStamp = time.perf_counter()
            for i in range(len(keysToInsert)):
                myTree.insert(node(keysToInsert[i]))
            endTimeStamp = time.perf_counter()
            resultInsertABR.append((endTimeStamp - startTimeStamp))

            startTimeStamp = time.perf_counter()
            for i in range(len(keysToInsert)):
                myTree.search(keysToSearch[i])
            endTimeStamp = time.perf_counter()
            resultSearchABR.append((endTimeStamp - startTimeStamp))

            startTimeStamp = time.perf_counter()
            for i in range(len(keysToInsert)):
                myTable.insert(keysToInsert[i])
            endTimeStamp = time.perf_counter()
            resultInsertHashTable.append((endTimeStamp - startTimeStamp))

            startTimeStamp = time.perf_counter()
            for i in range(len(keysToInsert)):
                myTable.search(keysToSearch[i])
            endTimeStamp = time.perf_counter()
            resultSearchHashTable.append((endTimeStamp - startTimeStamp))

        resultInsertLinkedListTot.append(resultInsertLinkedList)
        resultSearchLinkedListTot.append(resultSearchLinkedList)
        resultInsertABRTot.append(resultInsertABR)
        resultSearchABRTot.append(resultSearchABR)
        resultInsertHashTableTot.append(resultInsertHashTable)
        resultSearchHashTableTot.append(resultSearchHashTable)


    resultInsertLinkedListToDisplay = [0 for i in range(len(resultInsertLinkedListTot[0]))]
    for i in range(len(resultInsertLinkedListTot)):
        for j in range(len(resultInsertLinkedListTot[i])):
            resultInsertLinkedListToDisplay[j] += resultInsertLinkedListTot[i][j]

    for i in range(len(resultInsertLinkedListToDisplay)):
        resultInsertLinkedListToDisplay[i] = resultInsertLinkedListToDisplay[i] / numTests

    resultSearchLinkedListToDisplay = [0 for i in range(len(resultSearchLinkedListTot[0]))]
    for i in range(len(resultSearchLinkedListTot)):
        for j in range(len(resultSearchLinkedListTot[i])):
            resultSearchLinkedListToDisplay[j] += resultSearchLinkedListTot[i][j]

    for i in range(len(resultSearchLinkedListToDisplay)):
        resultSearchLinkedListToDisplay[i] = resultSearchLinkedListToDisplay[i] / numTests

    resultInsertABRToDisplay = [0 for i in range(len(resultInsertABRTot[0]))]
    for i in range(len(resultInsertABRTot)):
        for j in range(len(resultInsertABRTot[i])):
            resultInsertABRToDisplay[j] += resultInsertABRTot[i][j]

    for i in range(len(resultInsertABRToDisplay)):
        resultInsertABRToDisplay[i] = resultInsertABRToDisplay[i] / numTests

    resultSearchABRToDisplay = [0 for i in range(len(resultSearchABRTot[0]))]
    for i in range(len(resultSearchABRTot)):
        for j in range(len(resultSearchABRTot[i])):
            resultSearchABRToDisplay[j] += resultSearchABRTot[i][j]

    for i in range(len(resultSearchABRToDisplay)):
        resultSearchABRToDisplay[i] = resultSearchABRToDisplay[i] / numTests

    resultInsertHashTableToDisplay = [0 for i in range(len(resultInsertHashTableTot[0]))]
    for i in range(len(resultInsertHashTableTot)):
        for j in range(len(resultInsertHashTableTot[i])):
            resultInsertHashTableToDisplay[j] += resultInsertHashTableTot[i][j]

    for i in range(len(resultInsertHashTableToDisplay)):
        resultInsertHashTableToDisplay[i] = resultInsertHashTableToDisplay[i] / numTests

    resultSearchHashTableToDisplay = [0 for i in range(len(resultSearchHashTableTot[0]))]
    for i in range(len(resultSearchHashTableTot)):
        for j in range(len(resultSearchHashTableTot[i])):
            resultSearchHashTableToDisplay[j] += resultSearchHashTableTot[i][j]

    for i in range(len(resultSearchHashTableToDisplay)):
        resultSearchHashTableToDisplay[i] = resultSearchHashTableToDisplay[i] / numTests




    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, resultInsertLinkedListToDisplay, label="Linked List insert ", color="orange")
    plot1.plot(x_axis, resultInsertABRToDisplay, label="ABR insert ", color="green")
    plot1.plot(x_axis, resultInsertHashTableToDisplay, label="Hash Table insert ", color="blue")
    plot1.set_title("Risultati per Insert implementata con le 3 strutture dati")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione struttura dati")

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, resultSearchLinkedListToDisplay, label="Linked List search ", color="orange")
    plot1.plot(x_axis, resultSearchABRToDisplay, label="ABR search ", color="green")
    plot1.plot(x_axis, resultSearchHashTableToDisplay, label="Hash Table search ", color="blue")
    plot1.set_title("Risultati per Search implementata con le 3 strutture dati")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione struttura dati")

    # aggiungo a entrambi i grafici una piccola legenda visiva
    LinkedList_patch = mpatch.Patch(color='orange', label='Linked List')
    ABR_patch = mpatch.Patch(color='green', label='ABR')
    Hash_patch = mpatch.Patch(color='blue', label='Hash')
    plot1.legend(handles=[LinkedList_patch,ABR_patch,Hash_patch])
    plot1.legend(handles=[LinkedList_patch,ABR_patch,Hash_patch])

    plt.show()

def totalTestNew(numTests, dimMax, numToInsert, numToSearch):
    resultInsertLinkedListTot = []
    resultSearchLinkedListTot = []
    resultInsertABRTot = []
    resultSearchABRTot = []
    resultInsertHashTableTot = []
    resultSearchHashTableTot = []

    for i in range(numTests):
        myList = linkedList()
        myTree = ABR()
        myTable = hashTable(dimMax)
        K = []
        for i in range(dimMax):
            K.append(i)
        alreadyInserted = []

        resultInsertLinkedList = []
        resultSearchLinkedList = []
        resultInsertABR = []
        resultSearchABR = []
        resultInsertHashTable = []
        resultSearchHashTable = []

        while len(alreadyInserted) < dimMax:
            keysToInsert = []
            keysToSearch = []
            # scelgo numToInsert chiavi da aggiungere all'albero prese a caso tra quelle disponibili in K
            for i in range(numToInsert):
                index = random.randint(0, len(K) - 1)
                keysToInsert.append(K[index])
                alreadyInserted.append(K[index])
                K.remove(K[index])
            # scelgo numToSearch chiavi da cercare nell'albero prese a caso tra quelle già inserite
            for i in range(numToSearch):
                index = random.randint(0, len(alreadyInserted) - 1)
                keysToSearch.append(alreadyInserted[index])

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myList.insert(element(keysToInsert[i]))
            endTimeStamp = timer()
            resultInsertLinkedList.append((endTimeStamp - startTimeStamp) * 1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myList.search(keysToSearch[i])
            endTimeStamp = timer()
            resultSearchLinkedList.append((endTimeStamp - startTimeStamp) * 1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myTree.insert(node(keysToInsert[i]))
            endTimeStamp = timer()
            resultInsertABR.append((endTimeStamp - startTimeStamp) * 1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myTree.search(keysToSearch[i])
            endTimeStamp = timer()
            resultSearchABR.append((endTimeStamp - startTimeStamp) * 1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myTable.insert(keysToInsert[i])
            endTimeStamp = timer()
            resultInsertHashTable.append((endTimeStamp - startTimeStamp) * 1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myTable.search(keysToSearch[i])
            endTimeStamp = timer()
            resultSearchHashTable.append((endTimeStamp - startTimeStamp) * 1000)

        resultInsertLinkedListTot.append(resultInsertLinkedList)
        resultSearchLinkedListTot.append(resultSearchLinkedList)
        resultInsertABRTot.append(resultInsertABR)
        resultSearchABRTot.append(resultSearchABR)
        resultInsertHashTableTot.append(resultInsertHashTable)
        resultSearchHashTableTot.append(resultSearchHashTable)

    resultInsertLinkedListToDisplay = [0 for i in range(len(resultInsertLinkedListTot[0]))]
    for i in range(len(resultInsertLinkedListTot)):
        for j in range(len(resultInsertLinkedListTot[i])):
            resultInsertLinkedListToDisplay[j] += resultInsertLinkedListTot[i][j]

    for i in range(len(resultInsertLinkedListToDisplay)):
        resultInsertLinkedListToDisplay[i] = resultInsertLinkedListToDisplay[i] / numTests

    resultSearchLinkedListToDisplay = [0 for i in range(len(resultSearchLinkedListTot[0]))]
    for i in range(len(resultSearchLinkedListTot)):
        for j in range(len(resultSearchLinkedListTot[i])):
            resultSearchLinkedListToDisplay[j] += resultSearchLinkedListTot[i][j]

    for i in range(len(resultSearchLinkedListToDisplay)):
        resultSearchLinkedListToDisplay[i] = resultSearchLinkedListToDisplay[i] / numTests

    resultInsertABRToDisplay = [0 for i in range(len(resultInsertABRTot[0]))]
    for i in range(len(resultInsertABRTot)):
        for j in range(len(resultInsertABRTot[i])):
            resultInsertABRToDisplay[j] += resultInsertABRTot[i][j]

    for i in range(len(resultInsertABRToDisplay)):
        resultInsertABRToDisplay[i] = resultInsertABRToDisplay[i] / numTests

    resultSearchABRToDisplay = [0 for i in range(len(resultSearchABRTot[0]))]
    for i in range(len(resultSearchABRTot)):
        for j in range(len(resultSearchABRTot[i])):
            resultSearchABRToDisplay[j] += resultSearchABRTot[i][j]

    for i in range(len(resultSearchABRToDisplay)):
        resultSearchABRToDisplay[i] = resultSearchABRToDisplay[i] / numTests

    resultInsertHashTableToDisplay = [0 for i in range(len(resultInsertHashTableTot[0]))]
    for i in range(len(resultInsertHashTableTot)):
        for j in range(len(resultInsertHashTableTot[i])):
            resultInsertHashTableToDisplay[j] += resultInsertHashTableTot[i][j]

    for i in range(len(resultInsertHashTableToDisplay)):
        resultInsertHashTableToDisplay[i] = resultInsertHashTableToDisplay[i] / numTests

    resultSearchHashTableToDisplay = [0 for i in range(len(resultSearchHashTableTot[0]))]
    for i in range(len(resultSearchHashTableTot)):
        for j in range(len(resultSearchHashTableTot[i])):
            resultSearchHashTableToDisplay[j] += resultSearchHashTableTot[i][j]

    for i in range(len(resultSearchHashTableToDisplay)):
        resultSearchHashTableToDisplay[i] = resultSearchHashTableToDisplay[i] / numTests

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, resultInsertLinkedListToDisplay, label="LinkedList insert ", color="orange")
    plot1.plot(x_axis, resultSearchLinkedListToDisplay, label="LinkedList search ", color="green")
    plot1.set_title("Risultati per Insert e Search implementati con la Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione struttura dati")

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph2, plot2 = plt.subplots()
    plot2.plot(x_axis, resultInsertABRToDisplay, label="ABR insert ", color="orange")
    plot2.plot(x_axis, resultSearchABRToDisplay, label="ABR search ", color="green")
    plot2.set_title("Risultati per Insert e Search implementati con albero binario di ricerca")
    plot2.set_ylabel("tempo impiegato (millisecondi)")
    plot2.set_xlabel("dimensione struttura dati")

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph3, plot3 = plt.subplots()
    plot3.plot(x_axis, resultInsertHashTableToDisplay, label="Hash Table insert ", color="orange")
    plot3.plot(x_axis, resultSearchHashTableToDisplay, label="Hash Table search ", color="green")
    plot3.set_title("Risultati per Insert e Search implementati con Hash Table")
    plot3.set_ylabel("tempo impiegato (millisecondi)")
    plot3.set_xlabel("dimensione struttura dati")

    # aggiungo a entrambi i grafici una piccola legenda visiva
    Insert_patch = mpatch.Patch(color='orange', label='Insert')
    Search_patch = mpatch.Patch(color='green', label='Search')
    plot1.legend(handles=[Insert_patch, Search_patch])
    plot2.legend(handles=[Insert_patch, Search_patch])
    plot3.legend(handles=[Insert_patch, Search_patch])


    plt.show()

def totalTestUltimate(numTests, dimMax, numToInsert, numToSearch):
    resultInsertLinkedListTot = []
    resultSearchLinkedListTot = []
    resultInsertABRTot = []
    resultSearchABRTot = []
    resultInsertHashTableTot = []
    resultSearchHashTableTot = []

    for i in range(numTests):
        myList = linkedList()
        myTree = ABR()
        myTable = hashTable(dimMax)
        K = []
        for i in range(dimMax):
            K.append(i)
        alreadyInserted = []

        resultInsertLinkedList = []
        resultSearchLinkedList = []
        resultInsertABR = []
        resultSearchABR = []
        resultInsertHashTable = []
        resultSearchHashTable = []

        while len(alreadyInserted) < dimMax:
            keysToInsert = []
            keysToSearch = []
            # scelgo numToInsert chiavi da aggiungere all'albero prese a caso tra quelle disponibili in K
            for i in range(numToInsert):
                index = random.randint(0, len(K) - 1)
                keysToInsert.append(K[index])
                alreadyInserted.append(K[index])
                K.remove(K[index])
            # scelgo numToSearch chiavi da cercare nell'albero prese a caso tra quelle già inserite
            for i in range(numToSearch):
                index = random.randint(0, len(alreadyInserted) - 1)
                keysToSearch.append(alreadyInserted[index])

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myList.insert(element(keysToInsert[i]))
            endTimeStamp = timer()
            resultInsertLinkedList.append((endTimeStamp - startTimeStamp) * 1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myList.search(keysToSearch[i])
            endTimeStamp = timer()
            resultSearchLinkedList.append((endTimeStamp - startTimeStamp) * 1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myTree.insert(node(keysToInsert[i]))
            endTimeStamp = timer()
            resultInsertABR.append((endTimeStamp - startTimeStamp) * 1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myTree.search(keysToSearch[i])
            endTimeStamp = timer()
            resultSearchABR.append((endTimeStamp - startTimeStamp) * 1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myTable.insert(keysToInsert[i])
            endTimeStamp = timer()
            resultInsertHashTable.append((endTimeStamp - startTimeStamp) * 1000)

            startTimeStamp = timer()
            for i in range(len(keysToInsert)):
                myTable.search(keysToSearch[i])
            endTimeStamp = timer()
            resultSearchHashTable.append((endTimeStamp - startTimeStamp) * 1000)

        resultInsertLinkedListTot.append(resultInsertLinkedList)
        resultSearchLinkedListTot.append(resultSearchLinkedList)
        resultInsertABRTot.append(resultInsertABR)
        resultSearchABRTot.append(resultSearchABR)
        resultInsertHashTableTot.append(resultInsertHashTable)
        resultSearchHashTableTot.append(resultSearchHashTable)

    resultInsertLinkedListToDisplay = [0 for i in range(len(resultInsertLinkedListTot[0]))]
    for i in range(len(resultInsertLinkedListTot)):
        for j in range(len(resultInsertLinkedListTot[i])):
            resultInsertLinkedListToDisplay[j] += resultInsertLinkedListTot[i][j]

    for i in range(len(resultInsertLinkedListToDisplay)):
        resultInsertLinkedListToDisplay[i] = resultInsertLinkedListToDisplay[i] / numTests

    resultSearchLinkedListToDisplay = [0 for i in range(len(resultSearchLinkedListTot[0]))]
    for i in range(len(resultSearchLinkedListTot)):
        for j in range(len(resultSearchLinkedListTot[i])):
            resultSearchLinkedListToDisplay[j] += resultSearchLinkedListTot[i][j]

    for i in range(len(resultSearchLinkedListToDisplay)):
        resultSearchLinkedListToDisplay[i] = resultSearchLinkedListToDisplay[i] / numTests

    resultInsertABRToDisplay = [0 for i in range(len(resultInsertABRTot[0]))]
    for i in range(len(resultInsertABRTot)):
        for j in range(len(resultInsertABRTot[i])):
            resultInsertABRToDisplay[j] += resultInsertABRTot[i][j]

    for i in range(len(resultInsertABRToDisplay)):
        resultInsertABRToDisplay[i] = resultInsertABRToDisplay[i] / numTests

    resultSearchABRToDisplay = [0 for i in range(len(resultSearchABRTot[0]))]
    for i in range(len(resultSearchABRTot)):
        for j in range(len(resultSearchABRTot[i])):
            resultSearchABRToDisplay[j] += resultSearchABRTot[i][j]

    for i in range(len(resultSearchABRToDisplay)):
        resultSearchABRToDisplay[i] = resultSearchABRToDisplay[i] / numTests

    resultInsertHashTableToDisplay = [0 for i in range(len(resultInsertHashTableTot[0]))]
    for i in range(len(resultInsertHashTableTot)):
        for j in range(len(resultInsertHashTableTot[i])):
            resultInsertHashTableToDisplay[j] += resultInsertHashTableTot[i][j]

    for i in range(len(resultInsertHashTableToDisplay)):
        resultInsertHashTableToDisplay[i] = resultInsertHashTableToDisplay[i] / numTests

    resultSearchHashTableToDisplay = [0 for i in range(len(resultSearchHashTableTot[0]))]
    for i in range(len(resultSearchHashTableTot)):
        for j in range(len(resultSearchHashTableTot[i])):
            resultSearchHashTableToDisplay[j] += resultSearchHashTableTot[i][j]

    for i in range(len(resultSearchHashTableToDisplay)):
        resultSearchHashTableToDisplay[i] = resultSearchHashTableToDisplay[i] / numTests



    #Generazione dei 3 grafici con Insert/Search per ogni struttura dati
    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, resultInsertLinkedListToDisplay, label="LinkedList insert ", color="orange")
    plot1.plot(x_axis, resultSearchLinkedListToDisplay, label="LinkedList search ", color="green")
    plot1.set_title("Risultati per Insert e Search implementati con la Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione struttura dati")

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph2, plot2 = plt.subplots()
    plot2.plot(x_axis, resultInsertABRToDisplay, label="ABR insert ", color="orange")
    plot2.plot(x_axis, resultSearchABRToDisplay, label="ABR search ", color="green")
    plot2.set_title("Risultati per Insert e Search implementati con albero binario di ricerca")
    plot2.set_ylabel("tempo impiegato (millisecondi)")
    plot2.set_xlabel("dimensione struttura dati")

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph3, plot3 = plt.subplots()
    plot3.plot(x_axis, resultInsertHashTableToDisplay, label="Hash Table insert ", color="orange")
    plot3.plot(x_axis, resultSearchHashTableToDisplay, label="Hash Table search ", color="green")
    plot3.set_title("Risultati per Insert e Search implementati con Hash Table")
    plot3.set_ylabel("tempo impiegato (millisecondi)")
    plot3.set_xlabel("dimensione struttura dati")

    # aggiungo a entrambi i grafici una piccola legenda visiva
    Insert_patch = mpatch.Patch(color='orange', label='Insert')
    Search_patch = mpatch.Patch(color='green', label='Search')
    plot1.legend(handles=[Insert_patch, Search_patch])
    plot2.legend(handles=[Insert_patch, Search_patch])
    plot3.legend(handles=[Insert_patch, Search_patch])

    # crea la cartella per le tabelle se non esiste
    if not os.path.exists("tables"):
        os.makedirs("tables")

    #Generazione delle 3 tabelle che confrontano Inserimento e Ricerca su ogni struttura dati separatamente
    traceTables(
        *[
            [
                [i for i in range(0, dimMax, numToInsert)],
                ["{:.3e}".format(val) for val in resultInsertLinkedListToDisplay],
                ["{:.3e}".format(val) for val in resultSearchLinkedListToDisplay],
            ],
            (
                "Nr elementi",
                "Insert",
                "Search",
            ),
            "Inserimento e Ricerca eseguiti su Linked List",
        ]
    )

    traceTables(
        *[
            [
                [i for i in range(0, dimMax, numToInsert)],
                ["{:.3e}".format(val) for val in resultInsertABRToDisplay],
                ["{:.3e}".format(val) for val in resultSearchABRToDisplay],
            ],
            (
                "Nr elementi",
                "Insert",
                "Search",
            ),
            "Inserimento e Ricerca eseguiti su ABR",
        ]
    )

    traceTables(
        *[
            [
                [i for i in range(0, dimMax, numToInsert)],
                ["{:.3e}".format(val) for val in resultInsertHashTableToDisplay],
                ["{:.3e}".format(val) for val in resultSearchHashTableToDisplay],
            ],
            (
                "Nr elementi",
                "Insert",
                "Search",
            ),
            "Inserimento e Ricerca eseguiti su Hash Table",
        ]
    )

    # Generazione dell3 tabelle che confrontano prima Inserimento sulle 3 strutture dati, e poi la Ricerca
    traceTables(
        *[
            [
                [i for i in range(0, dimMax, numToInsert)],
                ["{:.3e}".format(val) for val in resultInsertLinkedListToDisplay],
                ["{:.3e}".format(val) for val in resultInsertABRToDisplay],
                ["{:.3e}".format(val) for val in resultInsertHashTableToDisplay],
            ],
            (
                "Nr elementi",
                "Linked List Insert",
                "ABR Insert",
                "Hash Table Insert",
            ),
            "Inserimento eseguito sulle 3 strutture dati",
        ]
    )
    traceTables(
        *[
            [
                [i for i in range(0, dimMax, numToInsert)],
                ["{:.3e}".format(val) for val in resultSearchLinkedListToDisplay],
                ["{:.3e}".format(val) for val in resultSearchABRToDisplay],
                ["{:.3e}".format(val) for val in resultSearchHashTableToDisplay],
            ],
            (
                "Nr elementi",
                "Linked List Search",
                "ABR Search",
                "Hash Table Search",
            ),
            "Ricerca eseguita sulle 3 strutture dati",
        ]
    )

    #Generazione dei 2 grafici con confronto di Insert per ogni struttura dati e Search per ogni struttura dati

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph4, plot4 = plt.subplots()
    plot4.plot(x_axis, resultInsertLinkedListToDisplay, label="Linked List insert ", color="orange")
    plot4.plot(x_axis, resultInsertABRToDisplay, label="ABR insert ", color="green")
    plot4.plot(x_axis, resultInsertHashTableToDisplay, label="Hash Table insert ", color="blue")
    plot4.set_title("Risultati per Insert implementata con le 3 strutture dati")
    plot4.set_ylabel("tempo impiegato (millisecondi)")
    plot4.set_xlabel("dimensione struttura dati")

    x_axis = [i for i in range(0, dimMax, numToInsert)]
    graph5, plot5 = plt.subplots()
    plot5.plot(x_axis, resultSearchLinkedListToDisplay, label="Linked List search ", color="orange")
    plot5.plot(x_axis, resultSearchABRToDisplay, label="ABR search ", color="green")
    plot5.plot(x_axis, resultSearchHashTableToDisplay, label="Hash Table search ", color="blue")
    plot5.set_title("Risultati per Search implementata con le 3 strutture dati")
    plot5.set_ylabel("tempo impiegato (millisecondi)")
    plot5.set_xlabel("dimensione struttura dati")

    # aggiungo a entrambi i grafici una piccola legenda visiva
    LinkedList_patch = mpatch.Patch(color='orange', label='Linked List')
    ABR_patch = mpatch.Patch(color='green', label='ABR')
    Hash_patch = mpatch.Patch(color='blue', label='Hash')
    plot4.legend(handles=[LinkedList_patch, ABR_patch, Hash_patch])
    plot5.legend(handles=[LinkedList_patch, ABR_patch, Hash_patch])

    plt.show()


if __name__ == '__main__':
    numTests = 1000
    dimMax = 100
    numToInsert = numToSearch = 10
    #testLinkedList(numTests, dimMax, numToInsert, numToSearch)
    #testABR(numTests, dimMax, numToInsert, numToSearch)
    #testHashTable(numTests, dimMax, numToInsert, numToSearch)
    totalTestUltimate(numTests, dimMax, numToInsert, numToSearch)


