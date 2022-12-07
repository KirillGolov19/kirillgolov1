from math import * #kasutatud matemaatika moodul valesti

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #vale märk, lisatud "", lisatud float
S=a**2
print("Ruudu pindala", round(S,1)) #lisatud round funktsioon
P=4*a
print("Ruudu ümbermõõt", round(P,1)) #vale märk, lisatud ", lisatud round funktsioon
di=a*sqrt(2) #lisatud sqrt, math vale
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #palju sulgusid
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala", round(S,1)) #vale märk
P=2*(b+c)
print("Ristküliku ümbermõõt", round(P,1)) #lisatud funktsioon round
di=sqrt(b*2+c*2) #math vale
print("Ristküliku diagonaal", round(di,1)) #vähe sulgusid, funktsioon round parandada
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #vale märk ja palju sulgusid
d=2*r #lisatud märk *
print("Ringi läbimõõt", round(d,1)) #lisatud märk , , lisatud round funktsioon
S=pi*r**2
print("Ringi pindala", round(S, 2))
C=2*pi*r #vale märk 2, parandada valem
print("Ringjoone pikkus", round(C)) #vähe sulgusid
