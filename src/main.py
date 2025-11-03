# Tomasz Dobrowolski

file = open("/workspaces/matura-2025-r25-3a-LTCTornado/zalaczniki-2025/symbole.txt", "r")  # "r" = read mode
lines = [line.strip() for line in file.readlines()]

def czy_palindrom(lines):
    for line in lines:
        if line == line[::-1]:
            print(line)
czy_palindrom(lines)    


file.close()