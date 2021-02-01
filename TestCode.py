# import fakeDomoticz as Domoticz
import fakeDomoticz
from fakeDomoticz import Device
from fakeDomoticz import Devices
from fakeDomoticz import Images

Parameters = {}
Parameters['Mode1'] = u"Manual selection (add below)"
Parameters['Mode2'] = u"A0:14:3D:A0:DE:9A,90:03:B7:E7:9A:00,A0:14:3D:07:C7:1B"
Parameters['Mode3'] = u"bluepy"
Parameters['Mode4'] = u"60"
Parameters['Mode5'] = u"Debug"


def runtest(plugin):

    fakeDomoticz.Start()
    fakeDomoticz.Debugging(0)

    plugin.onStart()
    # plugin.onCommand(1, '', '', '')
    plugin.onHeartbeat()
    plugin.onHeartbeat()
    plugin.onStop()
