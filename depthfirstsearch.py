from copy import deepcopy
import time
import Viewer

"Default Solution"
solution = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


class ValidPosition(list):
    """Class for throwing exception if list index is negative"""

    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")

        return list.__getitem__(self, n)


"states of puzzle"
liste = []
checker = False
"bool to check if solution was found"
solution_found = False
"number of checked nodes"
nodes = 0

row = 0
column = 0
help_list = []


def dfs(lis, depth):
    "depth first search algorithm"

    global checker, nodes, solution_found, liste, row, column, help_list
    nodes += 1

    if nodes > 1000000:
        liste.clear()
        print("No solution found ... ")
        print("Sequence:")
        print("Length: -1")
        checker = True
        depth = 0

    if lis == solution:
        nodes = 500000

    "return nothing if depth = 0 "
    if depth <= 0:
        return
    "Deepcopying of current state of puzzle for every of the 4 cases to not change the current state"
    list1 = deepcopy(lis)
    list2 = deepcopy(lis)
    list3 = deepcopy(lis)
    list4 = deepcopy(lis)

    "getting position of 0"
    for i in range(row):

        for j in range(column):

            if lis[i][j] == 0:
                help = lis[i][j]

                try:
                    "move to the left"
                    list1[i][j] = list1[i][j + 1]
                    list1[i][j + 1] = help

                    "checking if list1 is solution "
                    if list1 == solution:

                        solution_found = True

                        print("\nSolution Found ... ")

                        liste.append(list1)
                        "copying states of solution to help_list"
                        for k in liste:
                            help_list.append(k)

                        checker = True
                        nodes += 1

                        return
                    "if checker False so solution not yet found and list1 not yet in liste"
                    if checker is False:
                        if list1 not in liste:
                            liste.append(list1)
                            "start recursion new"
                            dfs(list1, depth - 1)
                            "removing list "
                            liste.remove(list1)
                except:
                    pass

                try:
                    "throws an exception if index becomes negative "
                    var = ValidPosition(list2[i])[j - 1]


                    "move to the right"
                    list2[i][j] = list2[i][j - 1]
                    list2[i][j - 1] = help

                    "checking if list2 is solution "
                    if list2 == solution:

                        solution_found = True

                        print("\nSolution Found ... ")
                        liste.append(list2)

                        for k in liste:
                            help_list.append(k)

                        checker = True
                        nodes += 1

                        return
                    "if checker False so solution not yet found and list2 not yet in liste"
                    if checker is False:
                        if list2 not in liste:
                            liste.append(list2)

                            dfs(list2, depth - 1)
                            liste.remove(list2)

                except:
                    pass

                try:
                    "move up"
                    list3[i][j] = list3[i + 1][j]
                    list3[i + 1][j] = help

                    "checking if list3 is solution "
                    if list3 == solution:

                        solution_found = True

                        print("\nSolution Found ... ")

                        liste.append(list3)

                        for k in liste:
                            help_list.append(k)

                        checker = True

                        return
                    "if checker False so solution not yet found and list3 not yet in liste"
                    if checker is False:
                        if list3 not in liste:
                            liste.append(list3)

                            dfs(list3, depth - 1)
                            liste.remove(list3)

                except:
                    o = 0

                try:
                    "throws an exception if index becomes negative "
                    negindex = ValidPosition(list4)[i - 1]

                    "move down"
                    list4[i][j] = list4[i - 1][j]
                    list4[i - 1][j] = help

                    "checking if list4 is solution "
                    if list4 == solution:

                        solution_found = True

                        print("\nSolution Found ... ")

                        liste.append(list4)

                        for k in liste:
                            help_list.append(k)
                        nodes += 1
                        checker = True

                        return
                    "if checker False so solution not yet found and list4 not yet in liste"
                    if checker is False:

                        if list4 not in liste:
                            liste.append(list4)

                            dfs(list4, depth - 1)
                            liste.remove(list4)

                except:
                    pass


def start__dfs(lis, depth, r, c):
    "pure depth first search"

    start = time.time()
    "Setting number of rows, columns"
    global row, column, liste, help_list, nodes

    row = r
    column = c
    liste.append(lis)
    "starting depth first search"
    dfs(lis, depth)

    end = time.time()
    result = end - start
    if solution_found:
        "generating solution sequence from states of puzzles in liste (previously copied to help_list) "
        str = Viewer.view_reverse(help_list, row, column)

        print("Sequence:", str)
        print("Length:", int(len(str) / 2))
        print("Nodes:", nodes)
        print("Duration:", result)

        "asking if user wants to see states of puzzle to solution "
        ask = input("Viewer (YES/NO):")
        if ask == "YES":
            Viewer.view(str, lis)
        else:
            print("TERMINATED")
    else:
        print("Duration:", result)


def start__idfs(lis, r, c):
    "iterative depth first search"

    start = time.time()

    global checker, liste, solution_found, row, column, help_list
    row = r
    column = c
    "Max depth of searching is 20"
    for i in range(20 + 1):
        "leaves loop when solution found"
        if solution_found or checker:
            break
        "removing all previous states"
        liste.clear()
        "appending initial state for next run"
        liste.append(lis)
        "starting depth first algorithm"
        dfs(lis, i)

    "generating solution sequence from states of puzzles in liste (previously copied to help_list) "
    str = Viewer.view_reverse(help_list, row, column)

    end = time.time()
    result = end - start
    if solution_found:
        print("Sequence:", str)
        print("Length:", int(len(str) / 2))
        print("Duration:", result)
        print("Nodes:", nodes)

        "asking if user wants to see states of puzzle to solution "
        ask = input("Viewer (YES/NO):")
        if ask == "YES":
            Viewer.view(str, lis)
        else:
            print("TERMINATED")
    else:
        print("Duration:", result)
