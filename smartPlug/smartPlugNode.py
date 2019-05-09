from becos import becosOneiroi
import time
from SmartPlug_Impl1 import SmartPlug_Impl
daemonURL='http://40.68.20.7:10200/'
clientName='PythonSmartPlugClient'
##conHandler=becosOneiroi.OneiroiHandler(daemonURL,clientName)
smartPlugNode=SmartPlug_Impl()
smartPlugNode.set_relayState('True')

input("waiting")