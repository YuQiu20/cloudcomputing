<<<<<<< HEAD
﻿# Simpel MQTT startpakket - snelstart

Wat dit start:
- Mosquitto (MQTT broker) op poort 1883
- Node-RED op poort 1880
- InfluxDB op poort 8086
- Portainer op poort 9000

Snelstart:
1. Kopieer .env.example naar .env als je variabelen wilt gebruiken:
   copy .env.example .env

2. Start de stack:
   docker compose up -d

3. Controleer containers:
   docker compose ps

4. Installeer Python MQTT client (éénmalig):
   python -m pip install --user paho-mqtt

5. Start de publishers (in aparte PowerShell vensters):
   python .\scripts\publish_joystick.py
   python .\scripts\publish_buttons.py

6. Open in browser:
   - Node-RED: http://localhost:1880
   - InfluxDB: http://localhost:8086
   - Grafana: http://localhost:3000
   - Portainer: http://localhost:9000

7. In Node-RED: voeg twee "mqtt in" nodes toe met topics gateway/joystick en gateway/buttons, verbind beide met "debug" nodes en klik "Deploy".

8. Als alles werkt: je ziet in Node-RED Debug en in de mqtt-sub terminal de binnenkomende berichten.
=======
# cloudcomputing
>>>>>>> 6096465872133e78e1277b69b3315aca3cf28f32
