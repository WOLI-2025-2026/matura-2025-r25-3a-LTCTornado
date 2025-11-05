# Tomasz Dobrowolski

file = open("/workspaces/matura-2025-r25-3a-LTCTornado/zalaczniki-2025/symbole.txt", "r")  # "r" = read mode
lines = [line.strip() for line in file.readlines()]

def czy_palindrom(lines):
    for line in lines:
        if line == line[::-1]:
            print(line)
czy_palindrom(lines)    

def kwadraty(lines):
    ans = []
    i = 0
    while i < len(lines)-2:
        j = 0
        while j < len(lines[i][j])-2:
            values = [lines[i][j], lines[i][j+1], lines[i][j+2], lines[i+1][j], lines[i+1][j+1], lines[i+1][j+2], lines[i+2][j], lines[i+2][j+1], lines[i+2][j+2]]
            if len(set(values)) == 1:
                ans.append()

file.close()