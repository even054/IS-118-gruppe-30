gamestart = input("""\nHei og velkommen til ett kort interaktiv Python-spill. I dette spillet skal
du spille som prosjektleder Erling og må løse tre konflikter angående hans prosjekt og dens medlemmer.
Etter seks uker med god stemning og motivasjon har prosjektet gått inn i den klassiske storming fasen,
der ulike faglige perspektiver og personlige preferanser har begynt å kollidere.Du mottar poeng basert 
på om du gjør riktig valg eller ikke. Klar til å spille? (ja/nei): """)

gamestart = gamestart.lower()

if gamestart == "ja":
    print("\nFlott! La oss starte spillet.")
else:
    print("\nOk, kanskje en annen gang. Ha en fin dag!")
    quit()

answer_1 = input("""\nKonflikt 1: Uenighet om teknologivalg og design har utviklet seg fra en sakskonflikt 
til en personkonflikt. Silje (UX/UI-designer) mener løsningen Elias (IT-rådgiver) foreslår vil låse 
brukeropplevelsen og hindre innovasjon. Elias mener Siljes forslag er urealistisk, usikkert og for kostbart. 
Diskusjonene blir stadig mer emosjonelle, og begge trekker støtte fra sine nærmeste i teamet. 
\n\nDu har to alternativer:\n1) Individuelle samtaler først, deretter et strukturert fellesmøte om saken. 
\n2) Erling tar en avgjørelse selv.\nHva velger du? (Skriv 1 eller 2): """)

if answer_1 == "1":
    print("""\nDu snakker med begge hver for seg, leder et fellesmøte og finner en kompromissløsning som begge aksepterer.
    Du får 1 poeng for god konflikthåndtering""")
elif answer_1 == "2":
    print("""\nDu tar en avgjørelse selv, og den ene parten føler seg misfornøyd og misforstått. Konflikten eskalerer.
    Du får 0 poeng for dårlig konflikthåndtering.""")
else:
    print("\nUgyldig valg. Start spill på nytt og skriv enten 1 eller 2.")
    quit()

answer_2 = input("""\nKonflikt 2: Samtidig med konflikten mellom Silje og Elias oppstår det spenning mellom Hamdi 
(kulturavdelingen) og Hallgeir (brukerrepresentant). De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter. 
Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform mens Hallgeir ønsker et mer åpent, dialogbasert 
system med rom for spontane innspill. Foreløpig er uenigheten lavmælt, men Erling merker at frustrasjonen vokser. Prosjektet 
nærmer seg en viktig milepæl: første prototype skal være klar om tre uker. Stemningen er spent, kommunikasjonen hakkete, og 
Erling vet at hans neste valg kan avgjøre om teamet beveger seg videre mot “norming”, eller blir stående fast i stormen. 
\n\nDu har to alternativer:\n1) Erling tar initiativ til et felles møte nå. \n2) Erling avventer og håper de løser det selv.
\nHva velger du? (Skriv 1 eller 2): """)