# https://github.com/GadgetReactor/pyHS100

from pyHS100 import SmartPlug, SmartBulb
from pprint import pformat as pf
import time

plug = SmartPlug("192.168.43.33")
print("Hardware: %s" % pf(plug.hw_info))
print("Full sysinfo: %s" % pf(plug.get_sysinfo())) # this prints lots of information about the device

rounds = 0
while True:
    print("Current consumption: %s" % plug.get_emeter_realtime())
    time.sleep(1)
    rounds += 1
    if rounds > 10:
        print("End")
        break