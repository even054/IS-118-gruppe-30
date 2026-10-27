input("Hei! Velkommen til vårt lille spill om prosjektledelse. (Trykk Enter for å starte)")
Poeng = 0


valg1 = input("Du er Erling, en prosjektleder for et kommunalt team som jobber med en digital løsning for innbyggerne i en kommune. Det oppstår en situasjon mellom to teammedlemmer. Silje ønsker en innovativ løsning som gir innbyggerne flere muligheter, men Elias mener at Siljes løsning er for kostbar og urealistisk. Du kan enten velge alternativ a) å ha individuelle samtaler først, deretter et strukturert fellesmøte om saken, eller alternativ b) Erling avgjør selv. Hva velger du? (Skriv a eller b) ").strip().lower()

if valg1 == "a":
    print("Du velger å ha individuelle samtaler først. Du snakker med dem hver for seg og klarer å stoppe en sakskonflikt fra å utvikle seg til en personkonflikt. Deretter har du et samlet møte for å finne et kompromiss. Godt jobbet, du klarte denne gangen å dra prosjektet videre!")
    Poeng += 1
elif valg1 == "b":
    print("Du velger å prioritere fremdrift og tar avgjørelsen selv. Mange i teamet er enige i hvordan du håndterte konflikten, men Silje og Elias sin konflikt ble ikke løst og ligger og ulmer.")
    Poeng -= 1

valg2 = input("Tiden går fort og prosjektet nærmer seg en viktig milepæl. Det er bare 3 uker til prototypen skal være klar!!! Teamet oppfatter tidsfristen og stressnivået øker. En lavmælt konflikt har oppstått mellom Hamdi og Hallgeir. Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform, mens Hallgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill. Du har to alternativer: a) ta initiativ til et felles møte nå, eller b) avvente og forvente at de oppklarer det selv som de voksne menneskene de er. Hva velger du? (Skriv a eller b) ").strip().lower()

if valg2 == "a":
    print("Du velger å ta initiativ til et felles møte. Du samler Hamdi og Hallgeir for å diskutere deres synspunkter og forslag. Gjennom møtet klarer teamet å samle seg rundt en løsning. Begge føler seg hørt og konflikten løses.")
    Poeng += 1
elif valg2 == "b":
    print("Du velger å avvente og forventer at de oppklarer det selv som voksne mennesker. Dette fører til en høylytt krangel mellom Hamdi og Hallgeir, og de ønsker ikke å snakke med hverandre lenger.")
    Poeng -= 1

valg3 = input("Tidsfristen for prototypen nærmer seg, og teamet begynner å føle presset og stemningen blir mer anspent. Du kan enten velge a) å sette av tid til relasjonsbygging og sosiale aktiviteter for å opprette sterkere tillit og teamfølelse, dette går av tid som kan brukes til å jobbe med prototypen, eller b) fokusere på tidspresset og jobbe med prototypen. Dette vil øke sjansene for å levere en god prototype, men teamet er allerede anspent og du vet at å sette mer press kan være destruktivt. Hva velger du? (Skriv a eller b) ").strip().lower()

if valg3 == "a":
    print("Du velger å sette av tid til relasjonsbygging og sosiale aktiviteter. Dette styrker samholdet og tilliten i teamet, noe som forbedrer kommunikasjonen og evnen til å jobbe sammen.")
    Poeng += 1
elif valg3 == "b":
    print("Du velger å fokusere på tidspresset og jobbe med prototypen. Dette øker sjansene for å levere en solid prototype, men teamet er stresset og begynner å vise tegn på utbrenthet.")
    Poeng -= 1

print("Du har gjort en heroisk innsats som prosjektleder. Du har håndtert konflikter og stress og klart å samle opp " + str(Poeng) + " poeng.")

input("Trykk Enter for å se resultatet av din innsats som prosjektleder.")

if Poeng == 3:
    print("Gratulerer, du har vist fremragende konflikthåndtering og ledelse. Teamet gjenoppretter tillit og går videre til norming-fasen.")
elif Poeng >= 1:
    print("Du har vist delvis god konflikthåndtering og ledelse. Teamet er fremdeles sårbart og konflikter ligger og ulmer, men det kunne vært verre.")
else:
    print("Jo, dette kunne gått bedre, Erling. Teamet står fast i storming-fasen og prosjektet blir forsinket.")
