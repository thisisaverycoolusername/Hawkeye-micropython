🌐 Hawkeye Raspberry Pi Pico W Access Point with Temperature Sensor 🌡️

This project sets up a Raspberry Pi Pico W as a Wi-Fi Access Point (AP) 📶 and serves temperature readings 🌡️ from a DS18B20 temperature sensor over HTTP using the micropython-phew library.
✨ Features

    🚀 Creates a Wi-Fi access point (AP) with a custom SSID and password.
    📡 Serves a GET endpoint (/temp) to retrieve temperature readings from the DS18B20 sensor.
    🛠️ Handles any undefined routes with a 404 error response.

🛒 Requirements

    🖥️ Raspberry Pi Pico W
    🌡️ DS18B20 temperature sensor
    🐍 MicroPython
    📦 micropython-phew library

🔌 Hardware Setup

    Connect the DS18B20 sensor:
        🟢 Data pin to GPIO 17.
        🔴 Power and ground pins to 3.3V and GND on the Pico W.
        🔧 Add a 4.7kΩ pull-up resistor between the data pin and 3.3V.

📥 Installing micropython-phew

To install the micropython-phew library:

    Download the package from PyPI via Thonny. Tools -> Manage packages -> Search for "micropython-phew" 📦
    Upload the necessary files to your Raspberry Pi Pico W.
