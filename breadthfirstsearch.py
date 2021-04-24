from copy import deepcopy
import time
import Viewer

"Default solution"
solution = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


class ValidPosition(list):
    """Class for throwing exception if list index is negative"""

    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")

        return list.__getitem__(self, n)


"list for saving all steps "
sequence = []


def backtracking(position, poslist, layer):
    """Algorithm which backtracks sequence of steps to solution """

    k = 0

    f = 0

    counter = 0

    counter2 = 0

    counter3 = 0

    helpList = []

    "final returned sequence"
    sequenz = ""

    "saving number of clustered nodes in poslist[0] to poslist[layer-1] in k"
    for i in range(layer - 1):
        k += len(poslist[i])

    "number of clustered nodes in last layer "
    help = position - k

    "following only works for layer > 1"
    if layer > 1:

        "saving number of clustered nodes in poslist[0] to poslist[layer-2] in f"
        for m in range(layer - 2):
            f += len(poslist[m])

        for j in range(len(poslist[layer - 2])):
            "saving length of poslist[layer - 2] "
            counter2 += 1

            for k in range(len(poslist[layer - 2][j])):

                "appending all single moves from (layer-2)-Layer to helpList"
                helpList.append(poslist[layer - 2][j][k])

                "count number of added moves"
                counter += 1

                "if true, counter3 is position of predecessor of current added step "
                if counter == help:
                    counter3 = counter2 + f

        "steps to solution in reverse order; last step in helpList is step of solution sequence"
        sequence.append(helpList[help - 1])

    "if only one layer solution can be read off easily"
    if layer == 1:
        sequenz = " " + poslist[0][0][0]

        return sequenz

    "termination of algorithm and reversal of steps in sequence which is returned finally"
    if layer == 2:

        for step in sequence:
            sequenz = step + " " + sequenz

        return sequenz

    else:
        "Recursion starts again until layer is two"
        return backtracking(counter3, poslist, layer - 1)


def bfs(l, sol, s, t):
    """breadth first search algorithm"""

    start = time.time()
    global solution
    "Setting solution"
    solution = sol

    "list for saving all postList1's (all directions of checked nodes stored, first dimension is layer," \
    "second possible states, third exact move) "
    posList0 = []
    "list for saving all postList2's"
    posList1 = []
    "list for saving all possible states, resulting of current state of puzzle"
    posList2 = []
    "number of clustered nodes"
    position = 1

    "List for saving checked states of puzzles"
    liste = [l]
    "Current layer"
    layer = 1
    "Variable for checking number of checked nodes"
    nodes = 0
    m = ""
    "list for checking ,to avoid going back to previous step, steps have same index as their states of puzzles" \
    " to which they belong "
    redundant = ["0"]

    "Setting number of rows"
    row = s
    "Setting number of columns"
    column = t

    "if initial puzzle is solution, algorithm finished"
    if l == solution:
        print("Solution Found ... ")

        print("Sequence:")
        print("Length: -1")

        "Clear list to let algorithm end"
        liste.clear()

    "Checking if list is not empty"
    while len(liste) > 0:

        "variable which tracks number of states of puzzle in one layer"
        nodes_current_layer = 0

        "Going through every element of list, liste contains the states of puzzles of one layer"
        for pos in range(len(liste)):

            nodes_current_layer += 1

            "checking if liste is not empty to avoid exception"
            if len(liste) > 0:
                "Deep-copying of current state of puzzle for every of the 4 cases to not change the current state"
                list1 = deepcopy(liste[pos])
                list2 = deepcopy(liste[pos])
                list3 = deepcopy(liste[pos])
                list4 = deepcopy(liste[pos])

            "getting position of 0"
            for i in range(row):

                "when solution is found list gets cleared and interrupts algorithm"
                if len(liste) == 0:
                    break

                for j in range(column):

                    "if 0 found i is number of row, j number of column"
                    if liste[pos][i][j] == 0:
                        "Saves 0"
                        help = liste[pos][i][j]

                        try:
                            "avoiding left move if previous move was to the right"
                            if redundant[pos] != "R":

                                "move to the left"
                                list1[i][j] = list1[i][j + 1]
                                list1[i][j + 1] = help

                                "Adding new state to liste"
                                liste.append(list1)

                                "Checked nodes +1"
                                nodes += 1

                                "checking if list1 is solution "
                                if list1 == solution:

                                    print("\nSolution Found ... ")

                                    sequence.append("L")

                                    "if after one step solution is found"
                                    if position == 1:
                                        posList0.append([["L"]])

                                    "returns string which is the sequence to solution"
                                    m = backtracking(position, posList0, layer)

                                    print("Sequence:", m)
                                    print("Length:", int(len(m) / 2))

                                    "Clearing list for interrupting algorithm"
                                    liste.clear()

                                    break

                                redundant.append("L")

                                posList2.append("L")

                        except:
                            "if no left move possible nothing happens and algorithm continues"
                            pass

                        try:
                            "avoiding right move if previous move was to the left"
                            if redundant[pos] != "L":

                                "throws an exception if index becomes negative "
                                negindex = ValidPosition(list2[i])[j - 1]

                                "move to the right"
                                list2[i][j] = list2[i][j - 1]
                                list2[i][j - 1] = help

                                "Adding new state to liste"
                                liste.append(list2)

                                nodes += 1

                                "checking if list2 is solution "
                                if list2 == solution:

                                    print("\nSolution Found ... ")

                                    sequence.append("R")

                                    "if after one step solution is found"
                                    if position == 1:
                                        posList0.append([["R"]])

                                    "returns string which is the sequence to solution"
                                    m = backtracking(position, posList0, layer)

                                    print("Sequence:", m)
                                    print("Length:", int(len(m) / 2))

                                    "Clearing list for interrupting algorithm"
                                    liste.clear()

                                    break

                                redundant.append("R")

                                posList2.append("R")

                        except:
                            pass

                        try:
                            "avoiding down move if previous move was up"
                            if redundant[pos] != "D":

                                "move up"
                                list3[i][j] = list3[i + 1][j]
                                list3[i + 1][j] = help

                                "Adding new state to liste"
                                liste.append(list3)

                                nodes += 1

                                "checking if list3 is solution "
                                if list3 == solution:

                                    print("\nSolution Found ... ")

                                    sequence.append("U")

                                    "if after one step solution is found"
                                    if position == 1:
                                        posList0.append([["U"]])

                                    "returns string which is the sequence to solution"
                                    m = backtracking(position, posList0, layer)

                                    print("Sequence:", m)
                                    print("Length:", int(len(m) / 2))

                                    liste.clear()

                                    break

                                redundant.append("U")

                                posList2.append("U")

                        except:
                            pass

                        try:
                            "avoiding up move if previous move was down"
                            if redundant[pos] != "U":

                                "throws an exception if index becomes negative "
                                negindex = ValidPosition(list4)[i - 1]

                                "move down"
                                list4[i][j] = list4[i - 1][j]
                                list4[i - 1][j] = help

                                "Adding new state to liste"
                                liste.append(list4)

                                nodes += 1

                                "checking if list4 is solution "
                                if list4 == solution:

                                    print("\nSolution Found ... ")

                                    sequence.append("D")

                                    "if after one step solution is found"
                                    if position == 1:
                                        posList0.append([["D"]])

                                    "returns string which is the sequence to solution"
                                    m = backtracking(position, posList0, layer)

                                    print("Sequence:", m)
                                    print("Length:", int(len(m) / 2))

                                    "Clearing list for interrupting algorithm"
                                    liste.clear()

                                    break

                                redundant.append("D")

                                posList2.append("D")

                        except:
                            pass

                        "appending possible states of one puzzle to list of these in current layer"
                        helpList = deepcopy(posList2)
                        posList1.append(helpList)

                        position += 1
                        "clearing for next run through"
                        posList2.clear()

                        if nodes > 500000:
                            liste.clear()
                            print("No solution found ... ")
                            print("Sequence:")
                            print("Length: -1")

                        break

        "appending clustered possible states in one layer"
        helpList2 = deepcopy(posList1)
        posList0.append(helpList2)

        "clearing for next run through"
        posList1.clear()

        "checking length of list of states of puzzle to avoid exceptions"
        if len(liste) > 0:

            layer += 1

            "removing states of puzzles in checked layer as well as their belonging moves"
            for z in range(nodes_current_layer):
                liste.pop(0)

                redundant.pop(0)

    "getting time which algorithm needed"
    end = time.time()
    result = end - start

    print("Duration:", result)
    if len(m) > 1:
        print("Nodes:", nodes)

        "asking if user wants to see states of puzzle to solution "
        ask = input("Viewer (YES/NO):")

        if ask == "YES":
            Viewer.view(m, l)
        else:
            print("TERMINATED")
