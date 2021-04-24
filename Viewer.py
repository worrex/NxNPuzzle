from copy import deepcopy


def view(sequence, base):
    """Input of steps to solution and the initial puzzle formation"""
    "Printing out initial formation"
    print(base, "\n")

    for j in sequence:

        k = 0

        "Searching for index of base which contains 0"
        while 0 not in base[k]:
            k += 1

        "Exact position of 0"
        l = base[k].index(0)

        "Changing and printing formations according to each step in sequence to the solution until end position reached"
        if j is "R":
            base[k][l] = base[k][l-1]
            base[k][l - 1] = 0
            print(base, "\n")

        if j is "L":

           base[k][l] = base[k][l + 1]
           base[k][l + 1] = 0
           print(base, "\n")

        if j is "U":
           base[k][l] = base[k+1][l]
           base[k+1][l] = 0
           print(base, "\n")

        if j is "D":
            base[k][l] = base[k-1][l]
            base[k-1][l] = 0
            print(base, "\n")


def view_reverse(liste, row, column):
    """Input of all states of puzzle of the solution sequence"""
    sequence = ""

    "Comparing n-list and n+1-list and adding letter to sequence according to the change of the position of 0"
    for pos in range(len(liste)):
        "Getting position of 0"
        for i in range(row):

            for j in range(column):

                if liste[pos][i][j] == 0:

                    for k in range(row):

                        for l in range(column):
                            "avoiding exception when last index of list reached"
                            if pos == (len(liste)-1):
                                break
                            if liste[pos+1][k][l] == 0:

                                if i-k == 1:
                                    sequence = sequence + " " + "D"

                                if i-k == -1:
                                    sequence = sequence + " " + "U"

                                if j-l == 1:
                                    sequence = sequence + " " + "R"

                                if j-l == -1:
                                    sequence = sequence + " " + "L"

    return sequence


sequence = []
checker = False

str = ""


def view_astar(collection, lis, layer):
    "input: all checked states of puzzles in collection, state of solution and move in lis, length of soltion in layer "
    global sequence, checker, str

    if layer <= 0:
        "if end reached converting sequence list into string"
        for l in sequence:
            str = l + " " + str

        checker = True
        return
    "if solution sequence not yet found"
    if not checker:
        "remove state of solution of puzzle from collection"
        collection.remove(lis)
        "copying state of solution"
        base = deepcopy(lis[-1])
        "saving move of copied state of solution"
        j = lis[0]

        "getting position of 0 of base"
        for k in range(len(base)):
            for l in range(len(base[k])):

                if lis[-1][k][l] == 0:
                    "due to the saved move, base gets changed to get its previous state, saving those moves in sequence"

                    if j is "L":
                        base[k][l] = base[k][l - 1]
                        base[k][l - 1] = 0
                        sequence.append("L")

                    if j is "R":
                        base[k][l] = base[k][l + 1]
                        base[k][l + 1] = 0
                        sequence.append("R")

                    if j is "D":
                        base[k][l] = base[k + 1][l]
                        base[k + 1][l] = 0
                        sequence.append("D")

                    if j is "U":
                        base[k][l] = base[k - 1][l]
                        base[k - 1][l] = 0
                        sequence.append("U")

        for i in range(len(collection)):
            if not checker:
                "getting index of changed base in the collection"
                if base == collection[i][-1]:
                    "new recursion with found element of collection"
                    view_astar(collection, collection[i], layer - 1)

    "return steps of solution"
    return str
