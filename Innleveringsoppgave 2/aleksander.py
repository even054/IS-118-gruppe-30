gamestart = input("\nVelkommen til ett kort interaktiv Python-spill, der du spiller som prosjektleder Erling \
og må løse tre konflikter angående hans prosjekt og dens medlemmer. Du mottar poeng basert på om du gjør riktig \
valg eller ikke. Klar til å spille? (ja/nei): ")

gamestart = gamestart.lower()
gamepoints = 0

if gamestart == "ja":
    print("\nFlott! La oss starte spillet.")
else:
    print("\nOk, kanskje en annen gang. Ha en fin dag!")
    quit()

answer_1 = input("\nKonflikt 1: Uenighet mellom Silje (UX/UI-designer) og Elias (IT-rådgiver) har utviklet seg \
fra en sakskonflikt til en personkonflikt. Silje mener løsningen Elias foreslår vil låse brukeropplevelsen og hindre \
innovasjon, mens Elias mener Siljes forslag er urealistisk, usikkert og for kostbart. Diskusjonene blir stadig mer  \
emosjonelle, og begge trekker støtte fra sine nærmeste i teamet. \n\nDu har to alternativer:\n1) Holde individuelle samtaler \
først, deretter ha et strukturert fellesmøte om saken. \n2) Ta en avgjørelse selv.\nHva velger du? (Skriv 1 eller 2): ")

if answer_1 == "1":
    print("\nDu snakker med begge hver for seg, leder et fellesmøte og finner en kompromissløsning som begge aksepterer. Du får 1 poeng for god konflikthåndtering.")
    gamepoints += 1
elif answer_1 == "2":
    print("\nDu tar en avgjørelse selv, og den ene parten føler seg misfornøyd og misforstått. Konflikten eskalerer. Du får 0 poeng for dårlig konflikthåndtering.")
    gamepoints += 0
else:
    print("\nUgyldig valg. Start spill på nytt og skriv enten 1 eller 2.")
    quit()

answer_2 = input("\nKonflikt 2: Hamdi (kulturavdelingen) og Hallgeir (brukerrepresentant) er uenige om hvordan innbyggerne \
skal kunne delta i digitale folkemøter. Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform mens \
Hallgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill. Foreløpig er uenigheten lavmælt, men du \
merker at frustrasjonen vokser. Prosjektet nærmer seg en viktig milepæl: første prototype skal være klar om tre uker. \
\n\nDu har to alternativer:\n1) Avventer og håper de løser det selv. \n2) Ta initiativ til et felles møte nå. \
\nHva velger du? (Skriv 1 eller 2): ")

if answer_2 == "1":
    print("\nDu avventer situasjonen, noe som fører til eskalering av konflikten og splittelse i teamet. Du får 0 poeng for dårlig konflikthåndtering.")
    gamepoints += 0
elif answer_2 == "2":
    print("\nDu Samler Hamdi og Hallgeir til et felles møte og finner en løsning som balanserer kontroll og åpenhet.")
    gamepoints += 1
else:
    print("\nUgyldig valg. Start spill på nytt og skriv enten 1 eller 2.")
    quit()

answer_3 = input("\nKonflikt 3: Det er blitt problemer med motivasjonen i teamet. \n\nDu har to alternativer:\n1) Sette av tid  \
til relasjonsbygging og sosiale aktiviteter. \n2) Prioritere fremdrift og leveranser.\nHva velger du? (Skriv 1 eller 2): ")

if answer_3 == "1":
    print("\nDu Prioriterer relasjonsbygging og sosiale aktiviteter, noe som styrker samholdet og motivasjonen i teamet. Du får 1 poeng for god ledelse.")
    gamepoints += 1
elif answer_3 == "2":
    print("\nDu Prioriterer fremdrift og leveranser, noe som øker stresset og senker motivasjonen i teamet. Du får 0 poeng for dårlig ledelse.")
    gamepoints += 0
else:
    print("\nUgyldig valg. Start spill på nytt og skriv enten 1 eller 2.")
    quit()

print(f"\nSpillet er over. Du fikk {gamepoints} poeng.")

if gamepoints == 3:
    print("Gratulerer! Teamet gjenoppretter tillit og går videre til norming-fasen.")
elif gamepoints == 2:
    print("Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
else:
    print("Prosjektet mister samhold og forsinkes.")