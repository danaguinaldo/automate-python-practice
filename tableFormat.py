#! python3
# tableFormat.py - A formatter for tables.

tableData = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'], 
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    # Find max characters
    maxCharacters = 0
    colWidths = [0] * len(tableData) # [0, 0, 0] to hold max values in each row
    for x in range(0, len(tableData)):
        for y in tableData[x]:
            if len(y) > colWidths[x]:
                colWidths[x] = len(y)
    for x in colWidths:
        if x > maxCharacters:
            maxCharacters = x

    # Print formatted table
    for x in range(0, len(tableData[0])):
        for y in range(0, len(tableData)):
            if len(tableData[y][x]) < maxCharacters:
                print((' ' * (maxCharacters - len(tableData[y][x]))) + tableData[y][x], end=' ')
            else:
                print(tableData[y][x], end= ' ')    
        print('')

printTable()
