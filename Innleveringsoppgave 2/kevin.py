points = 0

print("Velkommen til leder-spillet vårt! Her vil du møte på en rekke konlfikter som du må håndtere!" \
"Ved hvert valg får du to alternativer. Da trykker du inn 1 eller 2")

print("Første scenario: Silje og Elias er uenige om et design og teknologi valg og dette har blusset opp til en personal" \
      "konflikt. Du må hjelpe til for å forhindre at prosjektet faller i grus")

print("""hva velger du å gjøre
1) Holder du individuelle møter og dertter tar det opp i plenum
2) Du tar avgjørelsen selv for å sikre fremdrift i prosjektet""")

valg_en = int(input())

if valg_en == 1:
    points +=1
    #print("Godt valg!")

elif valg_en ==2:
    points +=0
    #print("dårlig valg!")


print("""Du håndterte situajsonen mellom Silje og Elias
samtidig diskutere Hamdi og Hallgeir hvordan innbgyggerne skal delta i folkemøter. Det er enda rolig mellom dem
men sitasjonen bygger seg opp
Hvordan skal du håndtere dette?""")

print("""1) Du unngår å blande deg inn og håper de finner ut av det selv.
2) Inviterer til et felles møte for å avklare uenigheten""")

valg_en = int(input())

if valg_en ==2:
    points +=1
    #print("Godt valg!")

elif valg_en ==1:
    points +=0
    #print("dårlig valg!")

print(""" Du håndterte sitasjonen mellom Hamdi og Hallgeir. 
Du innser at teamet hanver i konflikter og det tærer på motivasjonen. 
hva velger du å gjøre?""")

print("""1) Prioriterer fremdrift i prosjektet
2) Setter av tid til sosiale aktiviteter""")

valg_en = int(input())

if valg_en ==2:
    points +=1
    #print("Godt valg!")

elif valg_en ==1:
    points +=0
    #print("dårlig valg!")

print(f"Du fikk {points} poeng!")

if points == 3:
    print("bra jobba, du håndterte situasjonene på en god måte!")

elif points == 0:
    print("Konfliktene ble håndtert på dårlige måter, gå på lederkurs!")

else:
    print("noen av situasjonene ble håndtert godt men kunne blitt gjort bedre!")

