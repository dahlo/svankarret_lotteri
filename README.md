# Svankärrets lotteri

På senaste föreningsstämman hittades inga frivilliga som kunde ta sig an uppdraget som valberedning. Det beslutades istället att uppdraget ska lottas ut bland de medlemmar i föreningen som inte redan har ett pågågende återkommande uppdrag i föreningen. Enklast hade varit att ha en skål med lappar med alla husnummer och sen dra två stycken. Det kräver dock en del förberedelser som tar mer tid än man har under en pågående stämma så lotteriet sker nu i efterhand. För att se listan på hushåll som är med i dragningen, kolla i filen [lotteri.py](https://github.com/dahlo/svankarret_lotteri/blob/main/lotteri.py) och leta efter den långa listan med husnummer. Alla de husnummer som inte har en kommentar efter sig är med i dragningen.

Att lotta fram något utan vittnen på ett sätt som är upprepningsbart och verifierbart kräver lite mer än att bara be ett datorprogram slumpa fram två husnummer. Det måste ju vara samma sannolikhet att alla hus väljs, och ingen ska kunna påverka utfallet av lotteriet i förväg.

För att lösa detta kan man utnyttja det faktum att datorer egentligen inte kan generera slumptal på egen hand. Datorn tar en massa olika faktorer som tid, temperaturen inne i datorn och en rad andra saker som är svåra att styra över och summerar ihop dessa värden till en siffra. Denna siffra används sen som startpunk i matematiska funktioner som skapar tillsynes slumpmässiga tal ([pseudorandomness](https://en.wikipedia.org/wiki/Pseudorandomness)). Om man använder samma siffra nästa gång man kör programmet så kommer man få exakt samma "slumpmässiga" tal. Denna siffra som ligger till grund för den slumpmässiga tal man får kallas [seed](https://en.wikipedia.org/wiki/Random_seed) på engelska och översätts väl bäst till frövärde, det värde som resten av talserien växer fram ifrån.

Så återupprepbarheten går alltså att lösa genom att man sätter ett frövärde manuellt innan man kör lotteriet. Varje gång programmet körs så kommer det bli samma två hushåll som väljs. Vi måste dock se till att frövärdet väljs på ett bra och slumpmässigt sätt, samt att ingen kan påverka vilket frövärde som väljs.

Ett sätt att få slumpmässiga frövärden som inte kan förutsägas är att titta på Bitcoins blockkedja, och specifikt på det som kallas för [hashen](https://sv.wikipedia.org/wiki/Hashfunktion) för [block-headern](https://learnmeabitcoin.com/technical/block-header). Detta är ett hexadecimalt tal som inte går att förutsäga, dvs precis vad vi behöver för att välja ett bra frövärde för vårt lotteri. Tanken är då att man i förväg bestämmer en tidpunkt en par dagar framåt i tiden och att man tar det första blocket som produceras efter den tidpunkten och använder dess block-header-hash som frövärde.

Som exempel kan man titta på de [senaste producerade blocken](https://blockexplorer.one/bitcoin/mainnet) och ta hashsumman för det senaste blocket, `00000000000000000001ebe00575c3f63f90172fa89f121b2996e561b0d0bb46` just nu, och köra lotteri-programmet med den och be programmet generera 2 husnummer. För att hitta tidigare block baserat på en tid så kan man använda verktyg som [Block time calculator](https://www.blocktrainer.de/en/tools-services/block-time-calculator).

```bash
# ladda ner skriptet
git clone https://github.com/dahlo/svankarret_lotteri.git
cd svankarret_lotteri

# kör skriptet
python3 lotteri.py -s 00000000000000000002297f1395a67078f17e78d8eb4a13800b1d4aa3f50088 -n 2

# vilket ger detta svar:
Valda husnummer: 8K, 8M
```

Om tidpunkten för lotteriet bestäms i förväg så är det utom allas kontroll vilket frövärde som väljs, och alla som vill kan köra programmet och validera resultatet. Python 3.8.10 kommer användas vid körningen. Se nedan för ett exemple på hur man kör det via [Docker](https://www.docker.com/) så att man enkelt kan välja vilken version man kör.

```bash
docker run --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3.8.10 python lotteri.py -s "00000000000000000002297f1395a67078f17e78d8eb4a13800b1d4aa3f50088" -n 2
```





