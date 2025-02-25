# Cybersäkerhetsuppgift **Älgvaluate**

Detta projekt är en CTF-utmaning (Capture The Flag) som låter användare utforska och lära sig om `evals` sårbarheter från en hemsida. För mer detaljerad information om uppgifterna och målen, se [dokumenteringen](dokumentering.md).
## CTF-220S Setup Guide

### Nödvändiga komponenter
- Raspberry Pi
- Web-mappen
- Hacking-mappen
- Apache2

### Installation och konfiguration

1. Ladda ner projektfilerna
    ```bash
    git clone <repository-url>
    ```


2. kopiera web och hacking filerna till Raspberrypi
    ```bash
    scp -r web/ hacking/ pi@<raspberry-pi-ip>:~
    ```
3. Apache2 installation
    ```bash
    sudo apt update
    sudo apt install apache2
    ```

4. Kopiera webbfilerna
    ```bash
    sudo cp -r web/* /var/www/html/
    ```

5. Skapa gästkonto
    ```bash
    sudo adduser guest
    sudo usermod -d /home/guest/hacking guest
    sudo cp -r hacking /home/guest/
    sudo chown -R guest:guest /home/guest/hacking
    ```

6. Starta Apache2
    ```bash
    sudo systemctl start apache2
    sudo systemctl enable apache2
    ```

## Verifiering
- Kontrollera att webbservern är igång: `http://<raspberry-pi-ip>`
- Testa SSH-åtkomst: `ssh guest@<raspberry-pi-ip>`
### Map Stuktur
```
.
├── web/           # Web server files
├── hacking/       # Tools and resources for guest
└── docs/          # Additional documentation
```


## Säkerhetsinformation
- Gästkontot är begränsat till hacking-mappen
- Standardwebbporten (80) används för Apache2