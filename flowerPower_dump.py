#!/usr/bin/python3

import shelve

DBDATA = u'flowerPower'


db = shelve.open(DBDATA)
for k, v in db.items():
    if k == 'Devices':
        # print('Unit: ', k)
        for unit, datas in v.items():
            print('Device', unit, '\n\t', datas)
    else:
        print(k, '\n', v)
db.close()
