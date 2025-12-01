# Tomasz Dobrowolski
import numpy 

file = open("/workspaces/matura-2025-r25-3a-LTCTornado/zalaczniki-2025/symbole.txt", "r")
lines = [line.strip() for line in file.readlines()]

# zad 2.1
def zad2_1(lines):
    ans = ""
    for line in lines:
        if line == line[::-1]:
            ans += line + "\n"
    return ans
    

#print(czy_palindrom(lines))   

#zad 2.2

def zad2_2(lines):
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
        return f"{count} {cords}"
    else:
        return f"{cords}"

#print(kwadraty(lines))

#zad 2.3

def zad2_3(lines):    
    return (f"{(out := max(((int(line.replace('o','0').replace('+','1').replace('*','2'), 3), line) for line in lines), key=lambda x: x[0]))[0]} {out[1]}")
    #notatka dla mnie zebym pamietal o co chodzilo bo troche czasu nad tym spedzilem
    #((int(line.replace('o','0').replace('+','1').replace('*','2'), 3), line) for line in lines) zamienia kazda linie na liczbe w 
    # systemie dziesietnym po kolei, przechowujac poczatkowa wartosc line w typie touple
    #out := max  porownoje wartosci dzieki zdefiniowaniu ze ma porownywac 0 
    # dzieki temu ze naraz wykonujemy i przypisujemy program do zmiennej out znakiem :=, pod koniec dopisujemy poczatkowa linijke ktora trzymalismy w touple
#translate(lines)

 # zad 2.4
 
def zad2_4(lines):
    return (f"{(out := sum(int(line.replace('o','0').replace('+','1').replace('*','2'), 3) for line in lines))} {numpy.base_repr(out, 3).replace('0','o').replace('1','+').replace('2','*')}")
#suma(lines)
with open("/workspaces/matura-2025-r25-3a-LTCTornado/src/wynik2_1.txt", "w") as f:
    f.write(zad2_1(lines))
with open("/workspaces/matura-2025-r25-3a-LTCTornado/src/wynik2_2.txt", "w") as f:
    f.write(zad2_2(lines))
with open("/workspaces/matura-2025-r25-3a-LTCTornado/src/wynik2_3.txt", "w") as f:
    f.write(zad2_3(lines))
with open("/workspaces/matura-2025-r25-3a-LTCTornado/src/wynik2_4.txt", "w") as f:
    f.write(zad2_4(lines))

file.close()

# zad 3.1
file = open("/workspaces/matura-2025-r25-3a-LTCTornado/zalaczniki-2025/dron.txt", "r")
lines = [line.strip() for line in file.readlines()]
    
def zad3_1(lines):
    #NWD
    out = ""
    count = 0
    for j in range(-1,len(lines),1):
        a = abs(int(lines[j].split()[0]))
        b = abs(int(lines[j].split()[1]))
        for i in range(min(a,b),0,-1):
            if a % i == 0 and b % i == 0:
                nwd = i
                if nwd > 1:
                    count += 1
                out += f"{nwd}\n"
                break
            i -= 1
        j += 1
    out += f"{count}"
    return out

with open("/workspaces/matura-2025-r25-3a-LTCTornado/src/wynik3_1.txt", "w") as f:
        f.write(zad3_1(lines))   
        
        
# zad 3.2a 
def zad3_2a(lines):
    cord_a = 0
    cord_b = 0
    count = 0
    for j in range(0,len(lines),1):
        a = int(lines[j].split()[0])
        b = int(lines[j].split()[1])
        cord_a += a
        cord_b += b
        if 5000 > cord_a > 0 and 5000 > cord_b > 0:
            count += 1
    return f"{count}"

with open("/workspaces/matura-2025-r25-3a-LTCTornado/src/wynik3_2a.txt", "w") as f:
        f.write(zad3_2a(lines))  
    
# zad 3.2b
def zad3_2b(lines):
    cord_a = 0
    cord_b = 0
    cords_a = []
    cords_b = []
    cords_ab = ""
    for j in range(0,len(lines),1):
        cord_a += int(lines[j].split()[0])
        cord_b += int(lines[j].split()[1])
        cords_a.append(cord_a)
        cords_b.append(cord_b)
        cords_ab += f"{cord_a} {cord_b}\n"
    for i in range(len(cords_a)):
        for j in range(i+1,len(cords_a)):
            cords = f"{int(abs((cords_a[i] + cords_a[j])/2))} {int(abs((cords_b[i] + cords_b[j])/2))}"
            print(f"{cords_a[i]} {cords_b[i]}")
            if cords in cords_ab:
                return f"({cords_a[i]} {cords_b[i]}) ({cords}) ({cords_a[j]} {cords_b[j]})"
with open("/workspaces/matura-2025-r25-3a-LTCTornado/src/wynik3_2b.txt", "w") as f:
    f.write(zad3_2b(lines))  
    
    
file.close()

