##becos Oneiroi Node Implementation
##Auto Generated:2018-11-15 14:10:10.553487 

from becos import becosOneiroi

import xml.etree.ElementTree as xmlParser
from lxml import objectify

from requestsetrelaystate import requestsetrelaystate
class SmartPlug_Impl(becosOneiroi.oneiroiReceiver):
	daemonURL='http://40.68.20.7:10200/'
	clientName='My Smart Plug'
	conHandler=becosOneiroi.OneiroiHandler(daemonURL,clientName)
	excAttributes=['original_tagname_','name','sendFrom','sendTo','soureClient','hide','ttargetClient','sourceClient','targetClient']
	alias=None
	voltage_mV=None
	current_mA=None
	power_mW=None
	relayState=None
	def OnResponse(self,message):
		print(message)
	def OnNodeResponse(self,NodeName,message):
		print(f'NodeName:{NodeName},message{message}')
	def OnMessageReceived(self,messageID,NodeName,XmlMessage):
		res=xmlParser.fromstring(XmlMessage)
		messageType=res.attrib['name']
		if messageType.lower()=='requestsetrelaystate':
			self.on_requestsetrelaystate_Received(XmlMessage)
	def OnAttributeValueReceived(self,Client,NodeName,AttributeName,AttributeValue):
		##print('Client Name='+ Client+', Attribute Name = '+ AttributeName + ', AttributeValue = '+AttributeValue)
		if(AttributeName=='alias'):
			self.alias=AttributeValue           
		elif(AttributeName=='voltage_mV'):
			self.voltage_mV=AttributeValue
		if(AttributeName=='current_mA'):
			self.current_mA=AttributeValue
		if(AttributeName=='power_mW'):
			self.power_mW=AttributeValue
		if(AttributeName=='relayState'):
			self.relayState=AttributeValue
	def __init__(self):
		self.conHandler.Connect_TO_Node('SmartPlug',self)
		self.conHandler.Subscribe_To_Node_Message('SmartPlug')
		self.conHandler.Setup_Attribute_Notification('SmartPlug','alias')
		self.conHandler.Setup_Attribute_Notification('SmartPlug','voltage_mV')
		self.conHandler.Setup_Attribute_Notification('SmartPlug','current_mA')
		self.conHandler.Setup_Attribute_Notification('SmartPlug','power_mW')
		self.conHandler.Setup_Attribute_Notification('SmartPlug','relayState')
	def set_alias(self,newValue):
		self.conHandler.Set_Node_Attribute_Value('SmartPlug','alias',newValue)
	def set_voltage_mV(self,newValue):
		self.conHandler.Set_Node_Attribute_Value('SmartPlug','voltage_mV',newValue)
	def set_current_mA(self,newValue):
		self.conHandler.Set_Node_Attribute_Value('SmartPlug','current_mA',newValue)
	def set_power_mW(self,newValue):
		self.conHandler.Set_Node_Attribute_Value('SmartPlug','power_mW',newValue)
	def set_relayState(self,newValue):
		self.conHandler.Set_Node_Attribute_Value('SmartPlug','relayState',newValue)
	def on_requestsetrelaystate_Received(self,xmlMessage):
		message_received=requestsetrelaystate()
		root = xmlParser.fromstring(xmlMessage)
		message_received.name=root.attrib['name']
		message_received.soureClient=root.attrib['soureClient']
		message_received.targetClient=root.attrib['targetClient']
		message_received.sendFrom=root.attrib['sendFrom']
		messageAttributes=message_received.__dict__.keys()
		for at in messageAttributes:
			if not at in self.excAttributes:
				setattr(message_received,at,root.find(at).text)
		print(xmlMessage)
	def getXMLString(self,inputMessage):

		xmlMessage="<?xml version='1.0' encoding='utf-8'?>"       
		xmlMessage= xmlMessage +f"<{inputMessage.name}  name='{inputMessage.name}' soureClient='{inputMessage.soureClient}' sendFrom='{inputMessage.sendFrom}' sendTo='{inputMessage.sendTo}' hide='' targetClient='{inputMessage.targetClient}'>"
		messageAttributes=inputMessage.__dict__.keys()     
		for at in messageAttributes:
			if not at in self.excAttributes:
				xmlMessage=xmlMessage+ '  ' + f"<{at}>{getattr(inputMessage,at)}</{at}>"
		xmlMessage=xmlMessage+f'</{inputMessage.name}>'
		return xmlMessage
