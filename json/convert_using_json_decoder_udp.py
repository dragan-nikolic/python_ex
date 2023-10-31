"""
Demonstrates how to convert Python object to JSON and vice versa using JSONDecoder

Created: 2023-09-20
"""

import json

class SfTestdata(object):
    def __init__(self, sf):
        self.sf = sf

def udpTestdataDecoder(obj):
    if '__type__' in obj and obj['__type__'] == 'UdpTestdata':
        return UdpTestdata(obj['sf'])
    return obj

udpObj = json.loads(
            '{"__type__": "UdpTestdata", "sf": {"ids.t_ddo.perf_comp_sales": "ids_qa.t_ddo.perf_comp_sales", "idh.t_comp.weekly_sales": "idh_qa.t_comp.weekly_sales"}}',
            object_hook=udpTestdataDecoder)

print("Type of decoded object from JSON Data")
print(type(udpObj))
print("Udp Details")
print(type(udpObj.sf))
print(udpObj.sf)