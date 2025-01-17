## Krok 1: Vytvoření připojení v MySQL

V MySQL si vytvoř nový **Connection** a údaje pak vyplň do souboru `config.json`:

```json
{
  "database": {
    "host": "IP ADRESA",
    "port": "PORT",
    "user": "USERNAME",
    "password": "TVŮJE HESLO",
    "database": "NAZEV DB"
  },
  "logging": {
    "level": "ERROR",
    "log_file": "app.log"
  }
}
```

## Krok 2: Vytvoření databáze a vykonání SQL souborů

Najdi složku v MySQL, otevři aplikaci MySQL a připoj se k vytvořenému připojení. Vytvoř databázi a poté vykonej následující SQL soubory:

1. **Hotel.sql** - tento soubor vytvoří tabulky.
2. **Insert.sql** - tento soubor vloží data do tabulek.

Zkontroluj, že byly úspěšně vytvořeny tabulky a že data byla vložena správně.

## Krok 3: Instalace závislostí

Otevři terminál a nainstaluj potřebné balíčky pomocí příkazu:

### Installation

1. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```sh
   pip install mysql-connector-python
   ```


## Krok 4: Spuštění aplikace

Spusť soubor `main.py`. Můžeš to udělat buď v editoru (doporučuji Visual Studio Code), nebo přímo přes příkazovou řádku (CMD).
### Running the Application

```sh
python main.py
```