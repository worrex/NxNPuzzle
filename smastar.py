from copy import deepcopy
import time
import Viewer
import sys

"set recursion limit because default limit is only 999"
sys.setrecursionlimit(50000)

solution = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


class ValidPosition(list):
    """Class for throwing exception if list index is negative"""

    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")

        return list.__getitem__(self, n)


"list for checking ,to avoid going back to previous step, steps have same index as their states of puzzles" \
" to which they belong "
redundant = ["null"]

"checked nodes"
closed_list = []

"considered nodes but not yet checked"
open_list = []

row = 0

column = 0

"setting true when solution is found"
checker = False


def heuristic_1(lis):
    global row, column
    "Misplaced Tiles"

    misplaced = 0
    for i in range(row):

        for j in range(column):

            if lis[i][j] != solution[i][j]:
                misplaced += 1
    return misplaced


def heuristic_2(lis):
    global row, column
    "Manhattan-Distance"

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


nodes = 0
"list for sequence backtracking"
track = []

"string for saving steps to solution"
str = ""

heuristic = 2
bound = 50


def a_star(lis):
    """A* algorithm"""

    global row, column, closed_list, checker, open_list, redundant, nodes, str, heuristic, solution, bound

    "append currently investigated list"
    closed_list.append(lis)

    "list for sequence backtracking (move and belonging state of puzzle appended) "
    track.append([lis[2], lis[-1]])

    "if input is already solution "
    if lis[-1] == solution:
        row = 0
        print("Sequence:")
        print("Length: -1")

    "Deep-copying currently investigated state of puzzle"
    list1 = deepcopy(closed_list[- 1][-1])
    list2 = deepcopy(closed_list[- 1][-1])
    list3 = deepcopy(closed_list[- 1][-1])
    list4 = deepcopy(closed_list[- 1][-1])

    "variable which saves current layer"
    layer = closed_list[-1][1] + 1

    "getting position of 0"
    for i in range(row):

        if checker or len(closed_list) == 0:
            break

        for j in range(column):

            if closed_list[-1][-1][i][j] == 0:

                help = 0

                try:
                    "avoiding left move if previous move was to the right"
                    if closed_list[-1][2] != "R":

                        "move left"
                        list1[i][j] = list1[i][j + 1]
                        list1[i][j + 1] = help

                        "using previously chosen heuristic for evaluating currently investigated list"
                        if heuristic == 2:
                            open_list.append([heuristic_2(list1) + layer, layer, "L", list1])
                        if heuristic == 1:
                            open_list.append([heuristic_1(list1) + layer, layer, "L", list1])

                        nodes += 1

                        if list1 == solution:
                            print("\nSolution Found ... ")
                            track.append(["L", list1])
                            try:
                                "method returns string which contains moves to solution"
                                str = Viewer.view_astar(track, track[-1], layer)
                            except Exception as e:
                                print(e)
                            checker = True

                            break

                except:
                    pass

                try:
                    "avoiding right move if previous move was to the left"
                    if closed_list[-1][2] != "L":

                        "throws an exception if index becomes negative "
                        negindex = ValidPosition(list2[i])

                        "move right"
                        list2[i][j] = list2[i][j - 1]
                        list2[i][j - 1] = help

                        if heuristic == 2:
                            open_list.append([heuristic_2(list2) + layer, layer, "R", list2])
                        if heuristic == 1:
                            open_list.append([heuristic_1(list2) + layer, layer, "R", list2])

                        nodes += 1

                        if list2 == solution:
                            print("\nSolution Found ... ")
                            track.append(["R", list2])
                            try:

                                str = Viewer.view_astar(track, track[-1], layer)
                            except Exception as e:
                                print(e)

                            checker = True

                            break

                except:
                    pass

                try:
                    "avoiding down move if previous move was up"
                    if closed_list[-1][2] != "D":

                        "move up"
                        list3[i][j] = list3[i + 1][j]
                        list3[i + 1][j] = help

                        if heuristic == 2:
                            open_list.append([heuristic_2(list3) + layer, layer, "U", list3])
                        if heuristic == 1:
                            open_list.append([heuristic_1(list3) + layer, layer, "U", list3])

                        nodes += 1

                        if list3 == solution:
                            print("\nSolution Found ... ")
                            track.append(["U", list3])
                            try:
                                str = Viewer.view_astar(track, track[-1], layer)
                            except Exception as e:
                                print(e)

                            checker = True

                            break

                except:
                    pass

                try:
                    "avoiding up move if previous move was down"
                    if closed_list[-1][2] != "U":

                        "throws an exception if index becomes negative "
                        negindex = ValidPosition(list4)
                        prob = negindex[i - 1]

                        "Move down"
                        list4[i][j] = list4[i - 1][j]
                        list4[i - 1][j] = help

                        if heuristic == 2:
                            open_list.append([heuristic_2(list4) + layer, layer, "D", list4])
                        if heuristic == 1:
                            open_list.append([heuristic_1(list4) + layer, layer, "D", list4])

                        nodes += 1

                        if list4 == solution:
                            print("\nSolution Found ... ")

                            track.append(["D", list4])
                            try:

                                str = Viewer.view_astar(track, track[-1], layer)
                            except Exception as e:
                                print(e)

                            checker = True

                            break

                except:
                    pass

                j = 0
                "checking open_list for the state of puzzle with the smallest heuristic value"
                for i in range(len(open_list)):

                    if open_list[j][0] > open_list[i][0]:
                        j = i

                help_list = deepcopy(open_list[j])
                open_list.remove(open_list[j])

                "Bounded Memory of open_list, if length exceeds 900, list with the biggest heuristic value is removed  "
                if len(open_list) > bound:

                    k = 0
                    for m in range(len(open_list)):

                        if open_list[k][0] < open_list[m][0]:
                            k = m

                    open_list.remove(open_list[k])

                "cancellation criteria"
                if nodes < 40000:

                    a_star(help_list)
                else:
                    print("No solution found ... ")
                    print("Sequence:")
                    print("Length: -1")

                    "clear closed_list to break out of loop"
                    closed_list.clear()

                break


def start(lis, r, c, h, b):
    start = time.time()

    global row, column, str, heuristic, bound
    "setting bound of open_list "
    bound = b
    "setting used heuristic"
    heuristic = h
    row = r
    column = c
    "contains initial state of puzzle, heuristic value, layer and belonging direction of the chosen move"
    liste = [0, 0, "0", lis]

    "start A*star algorithm "
    a_star(liste)

    end = time.time()
    result = end - start
    "checking if solution was found"
    if checker:
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
