print = input("Hei! Velkommen til vårt lille interaktive spill. Her får du velge mellom to forslag, og får poeng eller minus poeng ved svarene. Lykke til!")

poeng = 0



print = input("Du spiller som Erling, prosjektlederen. \n Det har gått seks uker siden prosjektet startet, og du har fått beskjed om at Silje og Elias har kommet til uenighet om teknologivalg og design har utviklet seg fra en sakskonflikt til en personkonflikt. \n Silje mener løsningen Elias foreslår vil låse brukeropplevelsen og hindre innovasjon. Elias mener Siljes forslag er urealistisk, usikkert og for kostbart. \nDiskusjonene blir stadig mer emosjonelle, og begge trekker støtte fra sine nærmeste i teamet. Du har to alternativer: 1) Individuelle samtaler først, deretter et strukturert fellesmøte om saken, eller 2) Erling avgjør selv. Hva velger du? (Skriv 1 eller 2) ")  

if print == "1": 
    print = input("Du velger å ha individuelle samtaler først. \n Du snakker med Silje og Elias hver for seg, og får en bedre forståelse av deres bekymringer og forslag. \n Etter samtalene arrangerer du et strukturert fellesmøte der begge parter får presentere sine synspunkter. Du leder møtet på en måte som fremmer respekt og samarbeid. \n Resultatet er at dere finner en kompromissløsning som begge parter kan akseptere. Du får 1 poeng for god konflikthåndtering!")
    poeng += 1
elif print == "2":
    print = input("Du velger å avgjøre selv. \nDu tar en beslutning basert på din egen vurdering av situasjonen, uten å involvere Silje og Elias i prosessen. Dette fører til at den ene parten føler seg misfornøyd og misforstått, og konflikten eskalerer. \n Du mister 1 poeng for dårlig konflikthåndtering.")
    poeng -= 1

print = input("Etter å ha håndtert konflikten mellom Silje og Elias, oppstår det en ny utfordring. \n Spenning mellom Hamdi og Hallgeir, De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter. Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform. \n Hallgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill. Du har to alternitiver: 1) Erling tar initiativ til et felles møte nå, eller 2) Erling avventer og håper de løser det selv. Hva velger du? (Skriv 1 eller 2) ")
if print == "1":
    print = input("Du velger å ta initiativ til et felles møte. \n Du samler Hamdi og Hallgeir for å diskutere deres bekymringer og forslag. Gjennom møtet klarer dere å identifisere felles mål og finne en løsning som kombinerer kontroll og åpenhet. \n Begge parter føler seg hørt, og du får 1 poeng for god konflikthåndtering!")
    poeng += 1
elif print == "2":
    print = input("Du velger å avvente og håper de løser det selv. \n Dette fører til at konflikten mellom Hamdi og Hallgeir eskalerer, og de begynner å trekke inn andre teammedlemmer i konflikten. \n Resultatet er en splittelse i teamet, og du mister 1 poeng for dårlig konflikthåndtering.")
    poeng -= 1


print = input(" Etter å ha håndtert konflikten mellom Hamdi og Hallgeir, må du sette opp et møte for motivasjon i teamet. Du har to alternativer: 1) Sette av tid til relasjonsbygging og sosiale aktiviteter, eller 2) Prioritere fremdrift og leveranser. Hva velger du? (Skriv 1 eller 2) ")
if print == "1":
    print = input("Du velger å sette av tid til relasjonbygging og sosiale aktiviteter. \n Dette styrker teamets samhold og skaper en positiv arbeidskultur. \n Teammedlemmene føler seg verdsatt og motivert, og du får 1 poeng for god ledelse!")
    poeng += 1
elif print == "2":
    print = input("Du velger å prioritere fremdrift og leveranser. \n Dette fører til at teamet føler seg presset og stresset, og motivasjonen synker. \n Du mister 1 poeng for dårlig ledelse.")
    poeng -= 1

print = input("Etter å ha håndtert alle disse utfordringene, har vi nå samlet poengene dine. Du har totalt " + str(poeng) + " poeng. Takk for å ha spilt vårt interaktive spill om konflikthåndtering og ledelse!")
if poeng >= 3:
    print = input("Gratulerer! Du har vist utmerket konflikthåndtering og ledelse. Du har oppnådd en høy poengsum og har demonstrert gode ferdigheter i å håndtere utfordringer i teamet.")
elif poeng >= 1:
    print = input("Dessverre, du har ikke oppnådd full score. Det kan være lurt å reflektere over dine valg og vurdere hvordan du kan forbedre dine ferdigheter i konflikthåndtering og ledelse.")
if poeng >= -1:
    print = input("Du har oppnådd en lav poengsum. Det kan være nyttig å søke veiledning og lære mer om konflikthåndtering og ledelse for å forbedre dine ferdigheter.")



              
