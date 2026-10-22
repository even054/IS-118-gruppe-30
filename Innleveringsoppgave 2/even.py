poeng = 0

print("Hei, velkommen til spillet vårt. Du skal velge et alternativ per situasjon så får du poeng basert på hva du velger og en ny situasjon. Til slutt så får du et endepunkt basert på poengene dine. \n")

print("Situasjon 1: Silje og Elias")
print("A: Individuelle samtaler først, deretter et strukturert fellesmøte om saken")
print("B: Erling avgjør selv \n")
valg_en = input("Hvilket valg tar du (A/B): ").lower()

if valg_en == "a":
    poeng += 1
    print("Nytt scenario: Snakker med begge hver for seg, leder et fellesmøte og finner en kompromissløsning som begge aksepterer \n")
elif valg_en == "b":
    poeng += 0
    print("Nytt scenario: Tar en beslutning alene, noe som fører til misnøye og eskalering av konflikten \n")
else:
    print("Du valgte et ugyldig alternativ, prøv igjen!")
    quit()

print("Situasjon 2: Hamdi og Hallgeir")
print("A: Erling tar initiativ til et felles møte nå")
print("B: Erling avventer og håper de løser det selv \n")
valg_to = input("Hvilket valg tar du (A/B): ").lower()

if valg_to == "a":
    poeng += 1
    print("Nytt scenario: Samler Hamdi og Hallgeir til et felles møte og finner løsning som balanserer kontroll og åpenhet \n")
elif valg_to == "b":
    poeng += 0
    print("Nytt scenario: Avventer situasjonen, noe som fører til eskalering av konflikten og splittelse i teamet \n")
else:
    print("Du valgte et ugyldig alternativ, prøv igjen!")
    quit()

print("Situasjon 3: Motivasjon i teamet")
print("A: Sette av tid til relasjonsbygging og sosiale aktiviteter")
print("B: Prioritere fremdrift og leveranser \n")
valg_tre = input("Hvilket valg tar du (A/B): ").lower()

if valg_tre == "a":
    poeng += 1
    print("Nytt scenario: Prioriterer relasjonsbygging og sosiale aktiviteter, noe som styrker samholdet og motivasjonen i teamet \n")
elif valg_tre == "b":
    poeng += 0
    print("Nytt scenario: Prioriterer fremdrift og leveranser, noe som øker stresset og senker motivasjonen i teamet \n")
else:
    print("Du valgte et ugyldig alternativ, prøv igjen!")
    quit()

print(f"Endepunkt ({poeng} poeng):")
if poeng == 3:
    print("Teamet gjenoppretter tillit og går videre til norming-fasen.")
elif poeng >= 1 and poeng <= 2:
    print("Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
else:
    print("Prosjektet mister samhold og forsinkes.")