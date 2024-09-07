import network
import socket
from phew import server, connect_to_wifi
import machine, onewire, ds18x20, time

ds_pin = machine.Pin(17)
ap = network.WLAN(network.AP_IF)
ap.config(essid='Hawkeye', password='supersafe')
ap.active(True)

while not ap.active():
    pass

print("Access point active, IP:", ap.ifconfig()[0])

print('Access Point started')
print('SSID:', ap.config('essid'))
print('IP address:', ap.ifconfig()[0])

# Create a MicroPhew app
@server.route("/temp", methods=["GET"])
def random_number(request):
      
     
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
     
    roms = ds_sensor.scan()
     
    print('Found DS devices: ', roms)
     
    while True:
     
      ds_sensor.convert_temp()
     
      for rom in roms:
     
        return str(ds_sensor.read_temp(rom))

@server.catchall()
def catchall(request):
  return "Not found", 404

server.run()