from copy import deepcopy
import time
import Viewer

"default solution"
solution = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


class ValidPosition(list):
    """Class for throwing exception if list index is negative"""

    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")

        return list.__getitem__(self, n)


"saving move direction from current state of puzzle "
redundant = ["null"]

"saving all states of puzzles until solution is found"
liste = []

row = 0

column = 0
"Checking if solution found"
checker = False

heuristic = 2


def heuristic_1(lis):
    """Misplaced Tiles"""

    global row, column

    misplaced = 0
    for i in range(row):

        for j in range(column):

            if lis[i][j] != solution[i][j]:
                misplaced += 1
    return misplaced


def heuristic_2(lis):
    """Manhatthan-Distance"""

    global row, column

    distance = 0

    for i in range(row):

        for j in range(column):

            if lis[i][j] == 0:
                continue

            for k in range(row):

                for l in range(column):

                    if solution[k][l] == lis[i][j]:
                        z = abs(i - k)
                        y = abs(j - l)
                        distance += z + y
                        break

    return distance


list1 = []
list2 = []
list3 = []
list4 = []
"checked nodes"
nodes = 0


def best_first(lis, depth):
    """Best first algorithm"""

    global list1, list2, list3, list4, row, column, liste, checker, nodes, heuristic

    if depth <= 0:
        return

    "list for saving resulting states from current state of puzzle"
    help_list = []

    "list for saving move directions of resulting states from current state of puzzle"
    help_dir = []

    "appending current state to liste"
    liste.append(lis)

    "Deepcopying current state of puzzle for every of the 4 cases to not change the current state"
    list1 = deepcopy(lis)
    list2 = deepcopy(lis)
    list3 = deepcopy(lis)
    list4 = deepcopy(lis)

    "getting position of 0 in current state"
    for i in range(row):

        for j in range(column):

            if lis[i][j] == 0:
                "saves 0"
                help = lis[i][j]

                try:
                    "avoiding left move if previous move was to the right"
                    if redundant[0] != "R":

                        "move to the left"
                        list1[i][j] = list1[i][j + 1]
                        list1[i][j + 1] = help
                        help_list.append(list1)

                        help_dir.append("L")

                        if list1 == solution:
                            print("\nSolution Found ... ")

                            liste.append(list1)

                            nodes += 1

                            checker = True

                            return

                except:
                    pass

                try:
                    "avoiding right move if previous move was to the left"
                    if redundant[0] != "L":

                        "throws an exception if index becomes negative "
                        negindex = ValidPosition(list2[i])
                        prob = negindex[j - 1]

                        "move to the right"
                        list2[i][j] = list2[i][j - 1]
                        list2[i][j - 1] = help
                        help_list.append(list2)

                        help_dir.append("R")

                        if list2 == solution:
                            print("\nSolution Found ... ")

                            liste.append(list2)

                            nodes += 1

                            checker = True

                            return

                except:
                    pass

                try:
                    "avoiding up move if previous move was down"
                    if redundant[0] != "D":

                        "move up"
                        list3[i][j] = list3[i + 1][j]
                        list3[i + 1][j] = help

                        help_list.append(list3)

                        help_dir.append("U")

                        if list3 == solution:
                            print("\nSolution Found ... ")

                            liste.append(list3)

                            nodes += 1

                            checker = True

                            return

                except:
                    pass

                try:
                    "avoiding down move if previous move was up"
                    if redundant[0] != "U":

                        "throws an exception if index becomes negative "
                        negindex = ValidPosition(list4)
                        prob = negindex[i - 1]

                        "move to the down"
                        list4[i][j] = list4[i - 1][j]
                        list4[i - 1][j] = help

                        help_list.append(list4)

                        help_dir.append("D")

                        if list4 == solution:
                            print("\nSolution Found ... ")

                            liste.append(list4)

                            nodes += 1

                            checker = True

                            return

                except:
                    pass

                "list for saving costs of state of puzzle from help_list "
                distances = []

                "appending costs to distances if investigated state of puzzle not already in liste saved"
                if heuristic == 2:
                    for i in range(len(help_list)):
                        if help_list[i] not in liste:
                            distances.append(heuristic_2(help_list[i]))

                elif heuristic == 1:
                    for i in range(len(help_list)):
                        if help_list[i] not in liste:
                            distances.append(heuristic_1(help_list[i]))

                "checking if bigger than 0 to avoid exception"
                if len(distances) > 0:
                    "getting index of element with fewest cost"
                    min_distance = distances.index(min(distances))

                    redundant.clear()

                    "appending latest move direction"
                    redundant.append(help_dir[min_distance])
                else:
                    print("\nEndless Loop Detected ... Use another algorithm or change heuristic")
                    print("Sequence:")
                    print("Length: -1")
                    break

                "avoiding new recursion if solution was already found"
                if checker is False:
                    nodes += 1

                    "new recursion with list with fewest cost"
                    best_first(help_list[min_distance], depth - 1)

                break


def start(lis, r, c, h):
    "start of best first search"

    "getting start time"
    start = time.time()

    global row, column, nodes, heuristic
    "setting number of rows and columns"
    row = r
    column = c
    "setting heuristic"
    heuristic = h
    "starting best first search with max depth of 999"
    best_first(lis, 999)

    "getting end time and time needed"
    end = time.time()
    result = end - start

    "getting string of moves to solution by putting in states of puzzle to solution"
    str = Viewer.view_reverse(liste, row, column)

    if checker is True:
        print("Sequence:", str)
        print("Length:", int(len(str) / 2))
        print("Duration:", result)
        print("Nodes:", nodes)

        ask = input("Viewer (YES/NO):")
        if ask == "YES":
            Viewer.view(str, lis)
        else:
            print("TERMINATED")
    else:
        print("Duration:", result)
