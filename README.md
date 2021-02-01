# Parrot Flower Power & Pot plugin

## Installation
Install the plugin in Domoticz: https://www.domoticz.com/wiki/Using_Python_plugins

Install dependencies:
  pip3 install bluepy
  pip3 install btlewrap

In automatic mode, the plugin will do bluetooth scans at startup, and integrate any Parrot Flower devices it finds. 

In manual mode you can select which devices to add by entering their mac addresses on the hardware page. To find your Parrot Flower' mac-addresses do a bluetooth scan:
```
sudo hcitool lescan
```
1. Install dependencies:
```
pip3 install bluepy
pip3 install btlewrap
```
2. Clone repository into your domoticz plugins folder
```
cd domoticz/plugins
git clone https://github.com/afer92/parrot_flower_plugin.git FlowerPower
```
3. Restart domoticz
4. Make sure that "Accept new Hardware Devices" is enabled in Domoticz settings
5. Go to "Hardware" page and add new item with type "MELCloud plugin"
## Plugin update

```
cd domoticz/plugins/FlowerPower
git pull
```
## Testing without Domoticz
1. Clone repository
```
cd scripts/tests
git clone https://github.com/afer92/parrot_flower_plugin.git FlowerPower
```
2. Edit TestCode.py
```
Parameters['Mode1'] = u"Manual selection (add below)" # or "Automatic scanning"
Parameters['Mode2'] = u"A0:14:3D:A0:DE:9A,90:03:B7:E7:9A:00,A0:14:3D:07:C7:1B"
Parameters['Mode3'] = u"bluepy" # or "gatttool" or "pygatt"
Parameters['Mode4'] = u"60"
Parameters['Mode5'] = u"Debug" # or "Normal"
```
3. Run test
```
python3 plugin.py
```

## Thanks to

https://github.com/flatsiedatsie/Mi_Flower_mate_plugin
https://github.com/open-homeautomation/miflora
https://github.com/ChristianKuehnel/btlewrap
https://github.com/afer92/node-flower-power
