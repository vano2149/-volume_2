"""
"""
def sudoku(puzzle):

    def vaild(puzzle):
        for m in range(9):
            if puzzle[m][j]==puzzle[i][j] and m!= i:
                return False

        for n in range(9):
            if puzzle[i][n]==puzzle[i][j] and n!= j:
                return False

        for m in range(3):
            for n in range(3):
                if puzzle[int(i/3)*3+m][int(j/3)*3+n]==puzzle[i][j] and m!= i and n!= j and int(i/3)*3+m != i and int(j/3)*3+n!=j:
                    return False

        return True

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for d in range(1,10):
                    puzzle[i][j] = d
                    if vaild(puzzle):
                        if sudoku(puzzle):
                            return puzzle
                        else:
                            puzzle[i][j] = 0
                    else:
                        puzzle[i][j] = 0

                return False 

    return puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)


def box_values(x, y, puzzle):
    """ Returns a list of integers
    By using two coordinates, x and y, from a sudoku (puzzle), find the values
    in the sudoku belonging to the square region.
    """
    square_template = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    
    row = [value for chunk in square_template for value in chunk if x in chunk]
    col = [value for chunk in square_template for value in chunk if y in chunk]
    
    find_rows = [puzzle[r] for r in row]
    box_array = [find_rows[r][c] for r, v in enumerate(find_rows) for c in col]
    return box_array

def sudoku(puzzle):
    """ Returns a list of lists of integers
    Solves the sudoku, by performing the following steps:
        1) Determines the untouchable values, the ones that are not 0 in the
           initial sudoku. Its a list of tuples(x,y).
        2) Defines an horizontal and vertical list of lists of the sudoku
        3) With a while loop, stopping when there are not 0's in the sudoku (solved):
            3.1) Iterates through vertical and horizontal, getting the coordinates
                 and values.
            3.2) Checks if the coordinate tuple(x,y) is not untouchable.
            3.3) Determines the box array
            3.4) Determines the possible solutions by...
                 set(1..2..9) - set(horizontal line) - set(vertical line) - set(box square)
            3.5) If there is only a single solution, it horizonal and vertical list of lists
                 are edited using this value
        4) One there is no 0's in the puzzle, it returns the final solution.
    """
    untouchable = [tuple([x,y]) for x, array in enumerate(puzzle) 
                                for y, value in enumerate(array) if value > 0] #step 1
    
    horizontal, vertical = puzzle, [list(x) for x in zip(*puzzle)] #step 2
    
    while any(0 in sublist for sublist in horizontal): #step 3
        for x, x_array in enumerate(horizontal): #step 3.1
            for y, number in enumerate(x_array):
                y_array = vertical[y]
                coordinate = tuple([x,y])
                if not coordinate in untouchable: #step 3.2
                    box_array = box_values(x, y, puzzle) #step 3.3
                    possible_solutions = sorted(list(
                                         set(range(1,10)) - 
                                         set(x_array + y_array + box_array))) #step 3.4  
                    if len(possible_solutions) == 1: # step 3.5
                        horizontal[x][y] = possible_solutions[0]
                        vertical[y][x] = possible_solutions[0]
    return puzzle #step 4


# This is a implementation of this algorithm: Exact-Cover-Problem with dancing links 'https://www.cs.mcgill.ca/~aassaf9/python/sudoku.txt'.
# It was simplified and commented in German for a project I did with some friends during my apprenticeship, hence some additional functions
# I wont bother to remove...
    
from itertools import product

def validate_input_string(sudoku_string):

    if len(sudoku_string) == 81:
        rows = [sudoku_string[i:i+9] for i in range(0, 81, 9)]
        grid = [list(row) for row in rows]

        for row_index, row in enumerate(grid):
            for column_index, value in enumerate(row):
                if value != ".":
                    # Check row
                    for i in range(9):
                        if grid[row_index][i] == value and i != column_index:
                            print(f"Fehler! Die Zahl {value} kommt in Zeile {row_index+1} öfter als 1-mal vor!")
                            fehler = [value,row_index, "Zeile"]
                            return fehler
                    # Check column
                    for i in range(9):
                        if grid[i][column_index] == value and i != row_index:
                            print(f"Fehler! Die Zahl {value} kommt in Spalte {column_index+1} öfter als 1-mal vor!")
                            fehler = [value, column_index, "Spalte"]
                            return fehler
                    # Check Box
                    boxes = [
                    [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)],
                    [(1,4), (1,5), (1,6), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6)],
                    [(1,7), (1,8), (1,9), (2,7), (2,8), (2,9), (3,7), (3,8), (3,9)],
                    [(4,1), (4,2), (4,3), (5,1), (5,2), (5,3), (6,1), (6,2), (6,3)],
                    [(4,4), (4,5), (4,6), (5,4), (5,5), (5,6), (6,4), (6,5), (6,6)],
                    [(4,7), (4,8), (4,9), (5,7), (5,8), (5,9), (6,7), (6,8), (6,9)],
                    [(7,1), (7,2), (7,3), (8,1), (8,2), (8,3), (9,1), (9,2), (9,3)],
                    [(7,4), (7,5), (7,6), (8,4), (8,5), (8,6), (8,4), (8,5), (8,6)],
                    [(7,7), (7,8), (7,9), (8,7), (8,8), (8,9), (9,7), (9,8), (9,9)]
                    ]
                    box_number = (row_index // 3) * 3 + (column_index // 3)
                    for tile in boxes[box_number]:
                        if grid[tile[0]-1][tile[1]-1] == value and tile != (row_index+1, column_index+1):
                            print(f"Fehler! Die Zahl {value} kommt in Box {box_number+1} öfter als 1-mal vor!")
                            fehler = [value, box_number, "Box"]
                            return fehler
        return True
    else:
        print("String length is not 81 but " + str(len(sudoku_string)))
        return False

def solve_sudoku_from_input_string(sudoku_string):                              # Wandelt das Input-String-Format in ein Grid (List of Lists) um, löst das Sudoku und gibt einen

    if len(sudoku_string) == 81:
                                                                                # Output-String im gleichen Format zurück.
        rows = [sudoku_string[i:i+9] for i in range(0, 81, 9)]                  # Input-String in die einzelnen Zeilen (9 Werte je Zeile) aufteilen
        grid = [list(row) for row in rows]                                      # Und dann in einzelne Werte in Sub-Listen aufteielen.
        for row_index, row in enumerate(grid):                                  #
            for column_index, value in enumerate(row):                          #
                if value == ".":                                                # Punkte '.' im Input-String in '0' konvertieren
                    grid[row_index][column_index] = 0                           #
                else:                                                           #
                    grid[row_index][column_index] = int(value)                  # Konvertieren in Integer.
                                                                                #
        for solution in solve_sudoku(grid):                                     #
            grid = solution                                                     # Löse das Sudoku,
                                                                                #
        output_string = ""                                                      # generiere den Output-String
        for row in grid:                                                        #
            for value in row:                                                   #
                output_string += str(value)                                     #
        return output_string                                                    # und gebe ihn zurück.
    else:
        print("String length is not 81 but " + str(len(sudoku_string)))

def solve_sudoku(grid):
    # Spalten (Constraints, Bedingungen) der Exact-Cover-Matrix
    x_matrix = ([("rc", rc) for rc in product(range(9), range(9))] +            # Genau ein Wert pro Zelle (also pro Schnitt von Row und Column --> rc)
                [("rn", rn) for rn in product(range(9), range(1, 10))] +        # Jeder Wert von 1-9 genau einmal in einer Zeile (--> rn; n: Wert)
                [("cn", cn) for cn in product(range(9), range(1, 10))] +        # Jeder Wert von 1-9 genau einmal in einer Spalte (--> cn)
                [("bn", bn) for bn in product(range(9), range(1, 10))])         # Jeder Wert von 1-9 genau einmal in einer Box (--> bn)
                                                                                # d.h.:
                                                                                # 9 Spalten * 9 Zeilen = 81 [Jedes Feld genau einen Wert]
                                                                                # 9 Spalten * 9 Werte = 81 [Jeder Wert kommt in jeder Spalte genau einmal vor]
                                                                                # 9 Zeilen * 9 Werte = 81 [Jeder Wert kommt in jeder Zeile genau einmal vor]
                                                                                # 9 Boxen * 9 Werte = 81 [Jeder Wert kommt in jeder Box genau einmal vor]
                                                                                # = 324 Bedingungen
                                                                                # Beispiel:
                                                                                # Wert 1 in Zelle (0, 0) erfüllt die Bedingungen
                                                                                #   - genau ein Wert in Zelle (0, 0),
                                                                                #   - Wert 1 in Zeile 0 vorhanden,
                                                                                #   - Wert 1 in Spalte 0 vorhanden,
                                                                                #   - Wert 1 in Box 0 vorhanden.
                                                                                # Ansonsten wird keine weitere Bedingung erfüllt.
                                                                                # Erfüllte Bedingungen für einen Eintrag im Sudoku werden mit einer 1
                                                                                # in der Matrix markiert, unerfüllte Bedingungen mit einer 0.
                                                                                # D.h. der Eintrag von 1 in Zelle(0, 0) erfüllt bereits 4 von 324 Bedingungen.
                                                                                # Wird jede Bedingung EXAKT 1-mal erfüllt, liegt ein gültiges Sudoku vor.
                                                                                # (Logik: Jeder Eintrag erfüllt 4 Bedingungen, keine Bedingung darf doppelt)
                                                                                # (erfüllt werden; bei 81 Feldern macht das 81 * 4 = 324 erfüllte Bedingungen)

    # Zeilen (Sets) der Exact-Cover-Matrix -->  Eine Zeile für jede mögliche Zahl in jedem möglichen Feld:
    #                                           9 [Spalten] * 9 [Zeilen] * 9 [Werte] = 729 Zeilen (Sets) der Matrix
    y_matrix = dict()
    for row, column, number in product(range(9), range(9), range(1, 10)):
        box = (row // 3) * 3 + (column // 3)
        # Berechnet die Box-Nummer:
        # 0|1|2         Beispiel:
        # 3|4|5         Row-Nummerierung von 0-8 - Column-Nummerierung von 0-8 - Box-Nummerierung von 0-8 (siehe links)
        # 6|7|8         row = 5, column = 8 --> (5 // 3) * 3 + (8 // 3) = 1 * 3 + 2 = 5

        # Jedes Set enthält die Bedingungen, die es erfüllt
        y_matrix[(row, column, number)] = [("rc", (row, column)), ("rn", (row, number)), ("cn", (column, number)), ("bn", (box, number))]

    # Herstellen der Verknüpfungen von Einträgen und Bedingungen
    x_matrix, y_matrix = exact_cover(x_matrix, y_matrix)

    for row_index, row in enumerate(grid):                                      # Reduziert die Matrix basierend auf dem Input-grid
        for column_index, value in enumerate(row):                              #
            if value:                                                           # Für jede Zahl != 0 reduziere
                select(x_matrix, y_matrix, (row_index, column_index, value))    # die Matrix entsprechend.

    for solution in solve(x_matrix, y_matrix, []):                              # Löse das Sudoku rekursiv.
        for (row, column, value) in solution:                                   #
            grid[row][column] = value                                           # Vervollständige das Spielfeld basierend auf der Lösung und
        yield grid                                                              # gebe das Spielfeld zurück

def exact_cover(x_matrix, y_matrix):
    # Für jede Bedingung in der Excat-Cover-Matrix wird ein leeres Set hinterlegt (Umwandlung der List "x_matrix" in ein Dictionary)
    x_matrix = {constraint:set() for constraint in x_matrix}

    # Jede mögliche Zahl in einer Zelle (entry) erfüllt mehrere Bedingungen (constraints)
    for entry, constraints in y_matrix.items():
        # Jede Bedingung (constraint) wird nun mit jedem Eintrag verknüpft, der sie erfüllt
        for constraint in constraints:
            x_matrix[constraint].add(entry)

    # Zurückgegeben werden zwei miteinander verknüpfte Dictionarys:
    # "x_matrix" --> KEY ist die Bedingung (z.B. Wert 1 in Spalte 0 vorhanden) und VALUES sind alle Einträge,
    # die diese Bedingung erfüllen (z.B. Wert 1 in Zelle (0, 0), Wert 1 in Zelle (1, 0), Wert 1 in Zelle (2, 0), usw.)
    # "y_matrix" --> KEY ist der Eintrag (z.B. Wert 1 in Zelle (0, 0)) und VALUES sind alle Bedingungen,
    # die dieser Eintrag erfüllt (genau 1 Wert in Zelle (0, 0), Wert 1 kommt in Spalte 0 vor, Wert 1 kommt in Zeile 0 vor, Wert 1 kommt in Box 0 vor)
    return x_matrix, y_matrix

def select(x_matrix, y_matrix, entry):                                          # Übergabe eines Wertes in einer Zelle (entry) (Einfachhalber: Protagonist)
                                                                                # Protagonist wird für die finale Lösung "ausgewählt" --> "select"
                                                                                # (Jede Bedingung darf nur einmal erfüllt sein, d.h. alle Bedinungen, die der
                                                                                # Protagonist erfüllt, darf nicht mehr von anderen Einträgen (Antagonisten)
                                                                                # erfüllt werden; diese können also nicht mehr auftreten und somit aus den
                                                                                # Verknüpfungen entfernt werden --> Ist keine Bedingung mehr mit einem
                                                                                # Antagoniten verknüpft, so ist er gewissermaßen nicht mehr vorhanden)
    removed_entries = []                                                        #
    for constraint in y_matrix[entry]:                                          # Für jede Bedingung, die der Protagonist erfüllt,
        for each_entry in x_matrix[constraint]:                                 # finde zusätzlich alle anderen Antagonisten, die die gleiche Bedingung erfüllen und
            for other_constraint in y_matrix[each_entry]:                       # finde alle anderen Bedingungen, die jeder dieser Einträge erfüllt
                if constraint != other_constraint:                              # [<-- Einträge werden durch pop() entfernt unt sollen zwischengespeichert werden --> kein remove() erwünscht für "cosntraint"]
                    x_matrix[other_constraint].remove(each_entry)               # und entferne den Eintrag aus jeder der Bedinungen, die er erfüllt.
        removed_entries.append(x_matrix.pop(constraint))                        # Die Bedingung (constraint) wird nun nur noch einmal - und zwar vom Protagonisten
                                                                                # erfüllt und kann somit aus der Matrix entfernt werden. Zum späteren Reaktivieren
                                                                                # einer Bedingung mit ihren Einträgen, wird jeder Eintrag, der eine eine Bedingung
                                                                                # erfüllt in einer Liste (List of Lists) zwischenspeichert
    return removed_entries                                                      # und diese zurückgegeben.

def deselect(x_matrix, y_matrix, entry, removed_entries):                       # Protagonist wird aus der finalen Lösung entfernt --> "deselect"
    for constraint in reversed(y_matrix[entry]):                                # Für jede Bedingung, die der Protagonist erfüllt,
        x_matrix[constraint] = removed_entries.pop()                            # reaktiviere die Bedingung und füge den Protagonist und alle Antagonisten
                                                                                # wieder zu dieser Bedingung hinzu.
                                                                                # Warum reversed()? --> Die Reihenfolge der Bedingungen eines Protagonisten
                                                                                # ist wie folgt:
                                                                                #
                                                                                # Wert vorhanden? --> Wert in Zeile? --> Wert in Spalte? --> Wert in Box?
                                                                                #
                                                                                # In der removed_entries-Liste sind die zugehörigen Einträge auch in dieser
                                                                                # Reihenfolge gespeichert.
                                                                                # pop() gibt nun jedoch zuerst die Einträge für "Wert in Box?" zurück und würde
                                                                                # diese somit in die Liste der Einträge für die Bedingung "Wert vorhanden?" speichern,
                                                                                # was eine falsche Zuordnung wäre. Durch reserved() wird der Bedingung wieder die
                                                                                # passende Liste von Einträgen zugewiesen.
        for each_entry in x_matrix[constraint]:                                 # Für jeden Eintrag der die Bedingung erfüllt hat,
            for other_constraint in y_matrix[each_entry]:                       # finde jede andere Bedingung, die der Eintrag erfüllt hat und
                if constraint != other_constraint:                              # [<-- Einträge würden sonst für "constraint" doppelt hinzugefügt werden]
                    x_matrix[other_constraint].add(each_entry)                  # füge ihn der Bedingung wieder hinzu.

def solve(x_matrix, y_matrix, solution):
    # Wenn alle Bedingungen entfernt sind (--> siehe select(): x_matrix.pop()), ist "x_matrix" leer und "solution" wird zurückgegeben
    if not x_matrix:
        yield list(solution)
    else:
        constraint = min(x_matrix, key=lambda k: len(x_matrix[k]))              # "constraint" ist jetzt die Bedingung mit der geringsten Anzahl an Einträgen
        for entry in list(x_matrix[constraint]):                                # Für jeden Eintrag, der die Bedingung erfüllt:
            solution.append(entry)                                              # Wähle den Eintrag als Teil der Lösung aus und
            removed_entries = select(x_matrix, y_matrix, entry)                 # entferne ihn mit allen Antagonisten aus der Matrix, sodass die Bedingung exakt einmal
                                                                                # erfüllt ist (select() reduziert hierbei die Matrix)
            for s in solve(x_matrix, y_matrix, solution):                       # Rekursion: Rufe solve() erneut mit der neuen (kleineren) Matrix und aktuellen Lösung auf
                yield s                                                         # solve() liefert erst eine Lösung zurück, wenn die Matrix leer ist.
                                                                                # Bis dahin tritt immer wieder Rekursion auf. Die fertige Lösung wird dann bis zum Anfang
                                                                                # "durchgereicht".
            deselect(x_matrix, y_matrix, entry, removed_entries)                # Die Matrix wird wieder reaktiviert/aufgebaut und
            solution.pop()                                                      # der letzte Eintrag aus der Lösung entfernt.

def sudoku(puzzle):
    grid = []
    for solution in solve_sudoku(puzzle):                                     
        grid = solution  
    return grid



def valid(puzzle, guess, i, j):
    line_valid = guess not in puzzle[i]
    column_valid = guess not in (puzzle[k][j] for k in range(9))
    subgrid_valid = guess not in (puzzle[i - i % 3 + m][j - j % 3 + n] 
                                  for n in range(3) 
                                  for m in range(3))
    return line_valid and column_valid and subgrid_valid

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for guess in range(1, 10):
                    if valid(puzzle, guess, i, j):
                        puzzle[i][j] = guess
                        if sudoku(puzzle):
                            return puzzle
                        puzzle[i][j] = 0
                return False


    return puzzle