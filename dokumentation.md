*Sebastian Alin*  
# Rapport Cybersäkerhetsuppgift **Älgvaluate**

*Gå till lösningsförslaget för att se den korrekta flaggan*

## Innehållsförteckning
- [Rapport Cybersäkerhetsuppgift **Älgvaluate**](#rapport-cybersäkerhetsuppgift-älgvaluate)
  - [Innehållsförteckning](#innehållsförteckning)
  - [Beskrivning av uppgiften](#beskrivning-av-uppgiften)
    - [Komponenter](#komponenter)
    - [Säkerhetskoncept](#säkerhetskoncept)
  - [Syfte](#syfte)
  - [Lösningsskiss](#lösningsskiss)
  - [Uppskattad svårighetsgrad](#uppskattad-svårighetsgrad)
  - [Utvärdering](#utvärdering)
    - [Reflektion](#reflektion)
  - [Utvecklingspotential](#utvecklingspotential)
    - [Förbättringsområden](#förbättringsområden)
    - [Möjligheter att öka svårighetsgraden](#möjligheter-att-öka-svårighetsgraden)

## Beskrivning av uppgiften

Uppgiften består av en säkerhetsutmaning (CTF) där deltagaren ska:
1. Interagera med en miniräknar-app via webben (`10.22.4.116`).
2. Utnyttja en sårbarhet i `eval`-kommandot för att få åtkomst till serverns filsystem.
3. Hitta och ladda ner en lösenordsskyddad ZIP-fil.
4. Knäcka ZIP-filens lösenord.
5. Extrahera metadata från en bild i ZIP-filen för att hitta CTF-flaggan (se lösningsskissen för detaljer).

Användaren möts först av en webbapplikation med en miniräknare samt några övriga sidor. Hemsidan hostas lokalt på en Raspberry Pi med Apache2 och har adressen `10.22.4.116`. När användaren lyckas med injektionen i miniräknaren visas en instruktion om att ansluta till SSH-servern med inloggningen guest@10.22.4.116 och lösenordet guest.

![Miniräknare](Calculator.png)  
Miniräknargränssnitt

### Komponenter
- Apache2-webbserver från Raspberry Pi.
- Osäkert implementerat `eval`-kommando.
- SSH-server från Raspberry Pi.
- Lösenordsskyddad ZIP-fil, skapad med hjälp av onlineverktyget [ProtectedZip](https://protectedzip.com/).
- Bild på älg med dold metadata (skapad med "./Files_for_ctf_creation/GenerateMetadata.py").  
  ![Älg](./Files_for_ctf_creation/input.png)

### Säkerhetskoncept
- Kommandoinjektion via `eval`
- Brute-force av ZIP-lösenord
- Metadataanalys av bilder

## Syfte
Syftet med denna CTF-uppgift är att:
- Lära ut praktiska tekniker för kommandoinjektion och metadataanalys.
- Visa säkerhetsriskerna med användning av eval-funktionen.
- Ge praktisk erfarenhet av att arbeta med SSH och fjärråtkomst.
- Öka förståelsen för hur kryptering och lösenordsskydd fungerar.
- Introducera verktyg för metadataanalys och dess roll i cybersäkerhet.

## Lösningsskiss
1. **Initial Åtkomst**
   - Anslut till hemsidan [10.22.4.116](http://10.22.4.116) och utforska miniräknargränssnittet.  
   ![Miniräknare](Calculator.png)

2. **Kommandoinjektion**
   - Identifiera att kalkylatorn använder `eval`, vilket tydligt framgår av namnet Älgvaluate och de sidor där eval-sårbarheter beskrivs.  
     ![eval](eval.png)
   - Testa grundläggande kommandon såsom `1+1` och `alert("hello world")` för att se att funktionaliteten stämmer.
   - Prova att injicera systemkommandon:
     ```python
     __import__('os').system('ls')  # Listar filer
     ```
     ```javascript
     require('child_process').execSync('ls')
     ```
   - Inspektera HTML-koden för att hitta ledtrådar, exempelvis ett filnamn (`flag.txt`) och instruktioner på hur man får åtkomst till det.  
     ![ledtråd](new.png)
   - Ledtråden är kodad i Base64 och måste konverteras till text. Detta kan göras med ett enkelt Python-skript eller via webbverktyg som [Base64 Decode](https://www.base64decode.org/).
   - Genom att injicera följande kod i miniräknaren kan användaren asynkront hämta flaggan (flag.txt) och visa den i inmatningsrutan:
     ```javascript
     fetch('flag.txt')
       .then(response => response.text())
       .then(text => document.getElementById('result').value = text)
     ```

3. **Filsystemsexploration**
   - Efter injektionen visas instruktioner om att ansluta till `guest@10.22.4.116` via SSH.
   - Inne på servern finns flera kataloger där användaren ska hitta och ladda ner filen `Hemligheter.zip`.
   - Använd kommandot `scp` för att hämta filen:
     ```bash
     scp guest@10.22.4.116:/path/to/Hemligheter.zip ./
     ```
   - Alternativt kan man etablera en SSH-anslutning via VS Code för att överföra filen.

4. **ZIP-knäckning**
   - Den nedladdade ZIP-filen är krypterad med ett starkt lösenord.
   - Använd verktyget `fcrackzip` eller ett [onlineverktyg](https://www.lostmypass.com/file-types/zip/) för att brute-force lösenordet.
   - Vid extrahering används lösenordet `Admin`.

5. **Metadataextraktion**
   - Konvertera bilden från .heic till .png med hjälp av exempelvis [CloudConvert](https://cloudconvert.com/heic-to-png).
   - Analysera bildens metadata med verktyg som [Metadata2Go](https://www.metadata2go.com/).
   - Hitta CTF-flaggan i metadata (format: CTF220s{älgarna_har_fått_nog}).

## Uppskattad svårighetsgrad

Den uppskattade svårighetsgraden är **0.3** (30 % av deltagarna förväntas klara uppgiften), men detta kan justeras över tid.

**Motivering:**  
Stegen i uppgiften är inte väldigt komplexa, men de kräver kunskap om riskerna med eval (samt hur man unytjar riskerna med eval i javascript), tekniker för brute-force samt förståelse för metadataanalys.

Detta var från början 60% men eftersom, då det orgnialt ideen använde python, som krävde en enklare injektion `__import__('os').system('ls')` för att visa katalogens innehåll. Därför skulle inte en ssh anslutning häller krävas då filen `Hemligheter.zip` skulle finnas i samma katalog som python-programmet.

## Utvärdering

### Reflektion

En av de största utmaningarna under utvecklingen var att arbeta direkt på Raspberry Pi via SSH, vilket medförde följande problem:
- Avsaknad av GUI krävde att Apache-servern startades om manuellt vid varje uppdatering.
- SSH-anslutningen använde olika IP-adresser beroende på plats.
- 15–30 minuter gick förlorade varje gång en ny anslutning behövdes.
- Direktredigering via SSH ledde till en ineffektiv utvecklingsprocess.

Detta hade kunnat undvikas genom att utveckla och testa lokalt innan deployment till Raspberry Pi.

Ursprungligen planerades uppgiften som ett Python-program (eval.py) där användaren direkt skulle utnyttja eval-funktionen. På grund av problem med internethosting valdes istället en webbapplikation, vilket medförde begränsningar när det gäller att utforska systemfiler via eval-injektioner. Som en lösning implementerades en SSH-server där användaren kunde fortsätta sin utmaning efter den initiala injektionen.

Ändringen lade till ett extra lager av komplexitet, men gav samtidigt uppgiften ett mer realistiskt cybersäkerhetsperspektiv.

Hemsidan utvecklades med ren HTML, CSS och JavaScript – ett val som var tillräckligt för den enkla applikationen. I efterhand kunde utvecklingsprocessen effektiviserats med hjälp av ett ramverk som Vue + Nuxt i kombination med Tailwind CSS, vilket även hade bidragit till en enhetlig design.

## Utvecklingspotential
1. Använd ramverk och CSS-bibliotek för att snabba upp arbetsprocessen.
2. Testa och färdigställ koden lokalt innan den deployas, för att underlätta utvecklingen.

### Förbättringsområden
3. **Serversideskod**
   - Köra JavaScript-koden på serversidan istället för klienten kan öka effektiviteten samt belysa eval-sårbarheter.
4. **Global Hosting**
   - Hosta applikationen globalt istället för enbart lokalt för att göra utmaningen tillgänglig för fler.
5. **Användarrättigheter**
   - Begränsa användarrättigheter vid filåtkomst, vilket kräver goda kunskaper i bash och kommandoradsverktyg.
6. **Ledtrådar**
   - Implementera fler och mer intressanta ledtrådar som stöd för att lösa uppgiften.
   - Göra ledtrådarna mer kryptiska istället för att direkt beskriva åtgärderna.

### Möjligheter att öka svårighetsgraden
1. **Avancerad Kommandoinjektion**
   - Filtrera bort farliga kommandon.
   - Blockera vanliga shell-kommandon.
   - Implementera en vitlista med tillåtna tecken och operationer.
   - Begränsa inmatningens längd.
   - Sanera specialtecken från användarinput.
2. **Komplex ZIP-struktur**
   - Använda inbäddade ZIP-filer.
   - Implementera olika krypteringsmetoder.
   - Gömma filer i andra filformat.
3. **Utmaningar med Metadata**
   - Dela upp flaggan över flera bilder.
   - Kryptera metadata.
   - Använd steganografi.
4. **Serversäkerhet**
   - Implementera timeouts.
   - Införa IP-baserad begränsning (rate limiting).
5. **Extra Säkerhetslager**
   - Implementera honeypots.
   - Skapa fler decoy-filer.

