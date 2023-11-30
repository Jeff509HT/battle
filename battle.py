#1
a="AWS"
b=a.lower()
print(b)


#2
c= "Ayibobo Ayiti"
d=list(c.split(" "))
print(d)

#3

e="wey"
f=c.upper()
print(f)

#4
def inisyal(chenn):
    inisyal = [mo[0] for mo in chenn.split()]
    nouvo_chenn = ''.join(inisyal)
    return nouvo_chenn

# Ekzanp itilizasyon
chenn_enterenman = "PC"
nouvo_chenn =inisyal(chenn_enterenman)

print("Nouvo a se: ", nouvo_chenn)

#5
i= "Django"
j= i.replace("a", "@")
print(j)

#6
l = "Hello World"[::-1]
m = l.capitalize()
print(m)

#7
n="objecta"
o= n.find("a")
print(o)

#8
def total_endeks_a(chenn):
    total = 0

    for endeks, karakter in enumerate(chenn):
        if karakter.lower() == "a":
            total += 1

    return total


chenn_enterenman = "Test"
total_endeks_a = total_endeks_a(chenn_enterenman)

print("Total endeks 'a': ", total_endeks_a)

#9
def a(chenn):
    chenn_miniskil = chenn.lower()
    endeks = chenn_miniskil.find("a")
    lis_endeks = []

    while endeks != -1:
        lis_endeks.append(endeks)
        endeks = chenn_miniskil.find("a", endeks + 1)

    return lis_endeks

chenn_enterenman = "Computeraaakla"
a = a(chenn_enterenman)

print("Lis endeks 'a': ",a)

#10
def retire_espas_ak_kole(chenn):
    chenn_san_espas = chenn.replace(" ", "")
    chenn_final = chenn_san_espas + str(len(chenn))
    return chenn_final

chenn_enterenman = "plopla"
chenn_final = retire_espas_ak_kole(chenn_enterenman)

print("Chenn final: ", chenn_final)