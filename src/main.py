# Tomasz Dobrowolski

file = open("/workspaces/matura-2025-r25-3a-LTCTornado/zalaczniki-2025/symbole.txt", "r")  # "r" = read mode
lines = [line.strip() for line in file.readlines()]

# zad 2.1
def czy_palindrom(lines):
    ans = ""
    for line in lines:
        if line == line[::-1]:
            ans += line + "\n"
    return ans

#print(czy_palindrom(lines))   

#zad 2.2

def kwadraty(lines):
    count = 0
    cords = ""
    i = 0
    while i < len(lines)-2:
        j = 0
        while j < len(lines[i])-2:
            values = [lines[i][j], lines[i][j+1], lines[i][j+2], lines[i+1][j], lines[i+1][j+1], lines[i+1][j+2], lines[i+2][j], lines[i+2][j+1], lines[i+2][j+2]]
            if len(set(values)) == 1:
                count += 1
                cords += f"{str(i+2)} {str(j+2)} "
            j += 1
        i += 1
    if count > 1:
        return f"{str(count)} {cords}"
    else:
        return cords

#print(kwadraty(lines))

#zad 2.3

def translate(lines):    
    print(f"{(out := max(((int(line.replace('o','0').replace('+','1').replace('*','2'), 3), line) for line in lines), key=lambda x: x[0]))[0]} {out[1]}")
    #notatka dla mnie zebym pamietal o co chodzilo bo troche czasu nad tym spedzilem
    #((int(line.replace('o','0').replace('+','1').replace('*','2'), 3), line) for line in lines) zamienia kazda linie na liczbe w 
    # systemie dziesietnym po kolei, przechowujac poczatkowa wartosc line w typie touple
    #out := max  porownoje wartosci dzieki zdefiniowaniu ze ma porownywac 0 
    # dzieki temu ze naraz wykonujemy i przypisujemy program do zmiennej out znakiem :=, pod koniec dopisujemy poczatkowa linijke ktora trzymalismy w touple
translate(lines)
    







file.close()

