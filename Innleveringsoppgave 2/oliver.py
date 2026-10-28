poeng = 0
print("Silje og Elias")

print("hva velger du å gjøre")
print("Du velger å ta inddividuelle samtaller først, derret et strukturert fellesmøte om saken")
print("eller")
print("Du tar avgjørelsen selv")
valg1 = input("skriv inn 1 eller 2: ")

if valg1 == "1":
    print("Du snakker med begge hver for seg, leder et fellesmøte og finner en kompromissløsning som begge aksepterer")
elif valg1 == "2":
    print("Tar en besluttning selv, noe som fører til misnøye og eksalering av konflikten")
    poeng = poeng + 1
else:
    print("du klarte ikke velge mellom 1 og 2, så du blir offentlig henrettet")


print("Hamdi og hallgeir")
print("hva velger du å gjøre?")
print("Du tar inativ til et fellesmøte")
print("eller")
print("Avventer situasjonen og håper det løser seg selv")
valg2 = input("Skriv inn 1 eller 2: ")

if valg2 == "1":
    print("Du Sammler Hamdi og Hallgeir til et felles møte og finner en løsning som balanserer kontroll og åpenhet")
elif valg2 == "2":
    print("Du avventer situasjonen, noe som fører til eskalering av konflikten og splittelse i teamet")
    poeng = poeng + 1
else:
    print("du klarte ikke velge mellom 1 og 2, så du blir offentlig henrettet")

print("Motivasjon i teamet")
print("hva velger du å gjøre?")
print("Sette av tid til relasjonsbygging og sosiale aktiviteter")
print("eller")
print("prioritere fremdrift og leveranse.")
valg3 = input("skriv inn 1 eller 2: ")

if valg3 == "1":
    print("Du velger å sette av tid til relasjonsbugging og sosiale aktiviteter, noe som styrker samholdt og motivasjon")
elif valg3 == "2":
    print("Du prioriterer fremdrift og leveranse, noe som øker stresset og senker motivasjonen")
    poeng = poeng + 1


if poeng == 0:
    print("Teamet gjenoppretter tillit og går videre til norming-fasen")
elif poeng >= 1 and poeng <= 2:
    print("konflikten løses delvis, men relasjonene er fortsatt sårbare")
elif poeng == 3:
    print("prosjektet mister samhold og forsinkes")