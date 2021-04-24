import breadthfirstsearch, depthfirstsearch, bestfirst, astar, smastar


"@author Paul Peter Worrach, 15.12.2019"

"Main Module"


def inputs():

    global solution
    solution = []
    liste = []
    "Choosing Method to solve puzzle"
    method = eval(input("Method (1:BFS, 2:DFS, 3:IDFS, 4:BestFS, 5:A*S, 6:SMA*S):"))

    "Choosing number of rows and column of puzzle"
    row = eval(input("Rows:"))
    column = eval(input("Columns:"))
    checker = True
    print("\nDesired State of the Puzzle:")

    "Input of desired state of puzzle"
    try:
        for j in range(row):
            input3 = eval(input("Rows with brackets [...,...,...]: \n"))

            "if dimension of input doesnt match with columns, Error thrown"
            if len(input3) != column:

                print("ERROR: Input does not match with row and/or column... ")

                "set checker on false to make further code unreachable"
                checker = False
                break

            "append input3 for getting two-dimensional list"
            solution.append(input3)

        "Input of shuffled puzzle"
        if checker:
            print("\nGiven State of Puzzle:")
            for i in range(row):

                input2 = eval(input("Rows with brackets [...,...,...]: \n"))

                if len(input2) != column:
                    print("ERROR: Input does not match with row and/or column... ")
                    break
                "append input2 for getting two-dimensional list"
                liste.append(input2)

    except:

        print("ERROR... Try again!")

    "selecting previously chosen method"
    if len(liste) == row:

        if method == 1:
            "Execute bfs"
            breadthfirstsearch.bfs(liste, solution, row, column)

        if method == 2:
            "Setting solution in dfs"
            depthfirstsearch.solution = solution

            "Input of max. depth"
            depth = eval(input("Max. Depth:"))

            "Execute dfs"
            depthfirstsearch.start__dfs(liste, depth, row, column)

        if method == 3:
            "Setting solution in idfs"
            depthfirstsearch.solution = solution

            "Execute idfs"
            depthfirstsearch.start__idfs(liste, row, column)

        if method == 4:
            "Setting solution in bestfirst search"
            bestfirst.solution = solution
            heuristic = eval(input("Heuristic 1 (Misplaced Tiles) or Heuristic 2 (Manhattan Distance *recommended*) ?"))
            "only executing if valid number was input"
            if heuristic is 2 or 1:
                "Executing best first search"
                bestfirst.start(liste, row, column, heuristic)
            else:
                print("ERROR... Try again")

        if method == 5:
            "Setting solution in A* search"
            astar.solution = solution
            "choosing heuristic"
            heuristic = eval(input("Heuristic 1 (Misplaced Tiles) or Heuristic 2 (Manhattan Distance *recommended*) ?"))
            "only executing if valid number was input"
            if heuristic is 2 or 1:
                "Executing A* search"
                astar.start(liste, row, column, heuristic)
            else:
                print("ERROR... Try again")

        if method == 6:
            "Setting solution in SMA* search"
            smastar.solution = solution
            "choosing heuristic"
            heuristic = eval(input("Heuristic 1 (Misplaced Tiles) or Heuristic 2 (Manhattan Distance *recommended* ?"))
            "only executing if valid number was input"
            bound = eval(input("Bound of Open List (50-1000 recommended)"))
            if heuristic is 2 or 1:
                "Executing SMA* search"
                smastar.start(liste, row, column, heuristic, bound)


inputs()
