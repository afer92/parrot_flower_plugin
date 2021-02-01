#
#   Buienradar.nl Weather Lookup Plugin
#
#   Frank Fesevur, 2017
#   https://github.com/ffes/domoticz-buienradar
#
#   About the weather service:
#   https://www.buienradar.nl/overbuienradar/gratis-weerdata
#
#   Very simple module to make local testing easier
#   It "emulates" Domoticz.Log() and Domoticz.Debug()
#

import shelve

Devices = {}
Images = {}
dbHistory = 'flowerPower'
DEBUG = False


def Log(s):
    print(s)


def Debug(s):
    if DEBUG:
        print(s)


def Error(s):
    print(s)


def Debugging(val):
    global DEBUG
    if val == 1:
        print('Debugging on')
        DEBUG = True


def Start():
    global Devices
    database = shelve.open(dbHistory)
    if 'Devices' in database.keys():
        Devices = database['Devices']
    '''
    if 1 in Devices:
        print(Devices.keys())
    '''
    database.close()


class Device:

    @property
    def nValue(self):
        return self._nValue

    @nValue.setter
    def nValue(self, value):
        self._nValue = value

    @property
    def sValue(self):
        return self._sValue

    @sValue.setter
    def sValue(self, value):
        self._sValue = value

    @property
    def ID(self):
        return self._sValue

    @ID.setter
    def ID(self, value):
        self._sValue = value

    @property
    def Typename(self):
        return self._typeName

    @Typename.setter
    def ID(self, value):
        self._typeName = value

    @property
    def Name(self):
        return self._name

    @Name.setter
    def ID(self, value):
        self._name = value

    @property
    def LastLevel(self):
        return 0

    @property
    def Image(self):
        return self._image

    @Image.setter
    def ID(self, value):
        self._image = value

    @property
    def Unit(self):
        return self._unit

    @Unit.setter
    def Unit(self, value):
        self._unit = value

    @property
    def TypeName(self):
        return self._typeName

    @TypeName.setter
    def TypeName(self, value):
        self._typeName = value

    @property
    def BatteryLevel(self):
        return self._batteryLevel

    @BatteryLevel.setter
    def BatteryLevel(self, value):
        self._batteryLevel = value

    @property
    def Type(self):
        return self._type

    @Type.setter
    def Type(self, value):
        self._type = value

    @property
    def Subtype(self):
        return self._subtype

    @Subtype.setter
    def Subtype(self, value):
        self._subtype = value

    @property
    def Options(self):
        return self._options

    @Options.setter
    def Options(self, value):
        self._options = value

    @property
    def Used(self):
        return self._used

    @Used.setter
    def Used(self, value):
        self._used = value

    def __init__(self, Name="", Unit=0, TypeName="", Used=0, Type=0,
                 Switchtype=0, Subtype=0, Image="", Options=""):
        self._nValue = 0
        self._sValue = ''
        self._batteryLevel = 0
        self._name = Name
        self._unit = Unit
        self._type = Type
        self._typeName = TypeName
        self._subtype = Subtype
        self._options = Options
        self._used = Used
        self._image = Image
        self._image = None

    def Update(self, nValue=None, sValue=None, Options=None, Image=None, BatteryLevel=None):
        global Devices
        if nValue is not None:
            self._nValue = nValue
        if (sValue is not None) and (sValue != ''):
            self._sValue = sValue
        elif self._sValue is None:
            self._sValue = ''
        if BatteryLevel is not None:
            self._batteryLevel = BatteryLevel
        if Image is not None:
            self._image = Image
        if Options is not None:
            self._options = Options
        txt2log = u'--- update unit {}\n   nValue: {}\n sValue: {}\n   image: {}'
        Debug(txt2log.format(self._unit, self._nValue, self._sValue, self._image))
        database = shelve.open(dbHistory)
        database['Devices'] = Devices
        database.close()

    def __str__(self):
        text2return = u'Name: {} Unit: {} Type: {} TypeName: {} Subtype: {} Options: {}\n'
        text2return += u'nValue: {} sValue: {} Image: {} BatteryLevel: {}'
        return text2return.format(self._name, self._unit, self._type, self._typeName,
                                  self._subtype, self._options,
                                  self._nValue, self._sValue, self._image, self._batteryLevel)

    def Create(self):
        global Devices
        Devices[self._unit] = self
        # Devices[self._name] = self
        database = shelve.open(dbHistory)
        dbDevices = {}
        if 'Devices' in database.keys():
            dbDevices = database['Devices']
        dbDevices[self._unit] = self
        database['Devices'] = dbDevices
        database.close()


class Image:

    @property
    def Name(self):
        return self._name

    @Name.setter
    def ID(self, value):
        self._name = value

    @property
    def Base(self):
        return self._base

    @Base.setter
    def ID(self, value):
        self._base = value

    @property
    def ID(self):
        return self._filename

    @ID.setter
    def ID(self, value):
        self._filename = value

    def __init__(self, Filename=""):
        self._filename = Filename
        self._name = Filename
        self._base = Filename

    def Create(self):
        Images[self._filename.split(u' ')[0]] = self
