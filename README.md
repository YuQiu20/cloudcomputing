Cloud Computing - MQTT Startpakket

Met dit startpakket zet je snel een complete IoT-omgeving op. Dit pakket start de volgende Docker-containers:

*   **Mosquitto (MQTT Broker)** - Poort `1883`
*   **Node-RED** - Poort `1880`
*   **InfluxDB** - Poort `8086`
*   **Portainer** - Poort `9000`

---

Voorbereiding & Opstarten

1. **Maak de omgevingsvariabelen aan (optioneel)**  
   Kopieer het voorbeeldbestand als je variabelen wilt gebruiken:
   ```bash
   copy .env.example .env
   ```

2. **Start de Docker-stack**  
   Bouw en start de containers op de achtergrond:
   ```bash
   docker compose up -d
   ```

3. **Controleer je containers**  
   Check of alle containers succesvol draaien:
   ```bash
   docker compose ps
   ```

---

Python Publishers Starten

Om testdata naar je database te sturen, gebruiken we twee Python-scripts.

4. **Installeer de MQTT-bibliotheek (éénmalig)**  
   ```bash
   python -m pip install --user paho-mqtt
   ```

5. **Start de datastromen**  
   Open **twee aparte PowerShell vensters** en voer in elk venster één van onderstaande commando's uit:
   * Venster 1: `python .\scripts\publish_joystick.py`
   * Venster 2: `python .\scripts\publish_buttons.py`

---

Webinterfaces

Zodra alles draait, zijn je diensten bereikbaar via de browser:

*   **Node-RED:** http://localhost:1880
*   **InfluxDB:** http://localhost:8086
*   **Portainer:** http://localhost:9000

---

Testen in Node-RED

Controleer of de data goed binnenkomt:

1. Open **Node-RED** in je browser.
2. Sleep twee **"mqtt in"** nodes naar je werkveld.
3. Configureer de nodes en luister naar de topics: `gateway/joystick` en `gateway/buttons`.
4. Sleep een **"debug"** node naar het veld en verbind deze met beide mqtt-nodes.
5. Klik rechtsboven op de rode knop **Deploy**.
6. Open het debug-paneel (rechter zijbalk). Als alles correct werkt, zie je hier nu continu de live MQTT-berichten binnenkomen!