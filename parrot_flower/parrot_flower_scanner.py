"""Scan for Parrot Flower Power & Pot devices"""

# use only lower case names here
VALID_DEVICE_NAMES = ['flower power',
                      'parrot pot']

DEVICE_PREFIXES = ['A0:14:3D:', '90:03:B7:']


def scan(backend, timeout=10):
    """Scan for Parrot Flower Power & Pot devices.

    Note: this must be run as root!
    """
    result = []
    for (mac, name) in backend.scan_for_devices(timeout):
        if (name is not None and name.lower() in VALID_DEVICE_NAMES):
            result.append(mac.upper())
        elif (mac is not None and mac.upper()[:9] in DEVICE_PREFIXES):
            result.append(mac.upper())
    return result
