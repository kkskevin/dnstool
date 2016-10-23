# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder 
## http://www.wxformbuilder.org/


import sys,os,wmi,wx,thread,subprocess
getValue=100
getIpName=0
getHosts=0

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self ):
		wx.Frame.__init__ ( self, None, id = wx.ID_ANY, title = u"网络检测工具集1.2", pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		self.icon = wx.Icon('ghosts.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(self.icon)  
		
		#TEXT GUI
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_textCtrl6, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		#PING TOOLS GUI
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"PING 工具" ), wx.VERTICAL )
		
		self.m_textCtrl10 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString,wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_textCtrl10, 0, wx.ALL, 5 )
		self.Bind(wx.EVT_TEXT,self.getpingaddr,self.m_textCtrl10)
		
		self.m_button90 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"执行PING 命名", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_button90, 0, wx.ALL, 5 )
		self.Bind(wx.EVT_BUTTON,self.checkping,self.m_button90)
		
		self.m_button92 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Nslookup 工具", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_button92, 0, wx.ALL, 5 )
		self.Bind(wx.EVT_BUTTON,self.getNslookup,self.m_button92)

		self.m_button94 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"清空显示日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_button94, 0, wx.ALL, 5 )
		self.Bind(wx.EVT_BUTTON,self.clearNote,self.m_button94)
		
		gbSizer5.Add( sbSizer5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        #DNS TOOLS GUI
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"DNS 修改" ), wx.VERTICAL )
		
		m_choice6Choices = [u"阿里DNS:223.5.5.5",u"DNSPOD:119.29.29.29",u"百度DNS:180.76.76.76",u"114DNS:114.114.114.114"]
		self.m_choice6 = wx.Choice( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 0 )
		sbSizer8.Add( self.m_choice6, 0, wx.ALL, 5 )
		
		self.m_button91 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"修改DNS设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_button91, 0, wx.ALL, 5 )
		self.Bind(wx.EVT_BUTTON,self.getChoice,self.m_button91)
		
		self.m_button93 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"恢复DNS设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_button93, 0, wx.ALL, 5 )
		self.Bind(wx.EVT_BUTTON,self.setNetworkDhcp,self.m_button93)
		
		
		gbSizer5.Add( sbSizer8, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		#HOSTS TOOLS GUI
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"hosts工具" ), wx.VERTICAL )

		self.m_textCtrl11 = wx.TextCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString,wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		self.Bind(wx.EVT_TEXT,self.getHostsname,self.m_textCtrl11)

		self.m_button96 = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"绑定HOSTS", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_button96, 0, wx.ALL, 5 )
		self.Bind(wx.EVT_BUTTON,self.setHosts,self.m_button96)
		
		self.m_button95 = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"检测本地HOSTS", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_button95, 0, wx.ALL, 5 )
		self.Bind(wx.EVT_BUTTON,self.checkhosts,self.m_button95)
		
		self.m_button98 = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"重置本地HOSTS", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_button98, 0, wx.ALL, 5 )
		self.Bind(wx.EVT_BUTTON,self.clearhosts,self.m_button98)
		
		
		gbSizer5.Add( sbSizer10, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		#OTHER GUI
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"其他" ), wx.VERTICAL )
		
		self.m_button97 = wx.Button( sbSizer11.GetStaticBox(), wx.ID_ANY, u"未知", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11.Add( self.m_button97, 0, wx.ALL, 5 )
		
		self.m_button99 = wx.Button( sbSizer11.GetStaticBox(), wx.ID_ANY, u"未知", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11.Add( self.m_button99, 0, wx.ALL, 5 )
		
		
		gbSizer5.Add( sbSizer11, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		bSizer10.Add( gbSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
    
    #DNS TOOLS
	def getChoice(self,event):
		global getValue
		ChoiceID = self.m_choice6.GetCurrentSelection()
		if (ChoiceID == 0):
			setNicDnsAddr('223.5.5.5')

			if (getValue[0] == 0):
				self.dialogBox=wx.MessageBox(u"修改DNS成功",u"成功^_^")
			elif (getValue[0] == 1):
				self.dialogBox=wx.MessageBox(u"修改DNS成功",u"成功^_^")
			else:
				self.dialogBox=wx.MessageBox(u"修改DNS失败,请使用管理员运行!",u"失败咯@_@") 

		elif (ChoiceID == 1):
			setNicDnsAddr('119.29.29.29')

			if (getValue[0] == 0):
				self.dialogBox=wx.MessageBox(u"修改DNS成功",u"成功^_^")
			elif (getValue[0] == 1):
				self.dialogBox=wx.MessageBox(u"修改DNS成功",u"成功^_^")
			else:
				self.dialogBox=wx.MessageBox(u"修改DNS失败,请使用管理员运行!",u"失败咯@_@")

		elif (ChoiceID == 2):
			setNicDnsAddr('180.76.76.76')

			if (getValue[0] == 0):
				self.dialogBox=wx.MessageBox(u"修改DNS成功",u"成功^_^")
			elif (getValue[0] == 1):
				self.dialogBox=wx.MessageBox(u"修改DNS成功",u"成功^_^")
			else:
				self.dialogBox=wx.MessageBox(u"修改DNS失败,请使用管理员运行!",u"失败咯@_@")

		elif (ChoiceID == 3):
			setNicDnsAddr('114.114.114.114')

			if (getValue[0] == 0):
				self.dialogBox=wx.MessageBox(u"修改DNS成功",u"成功^_^")
			elif (getValue[0] == 1):
				self.dialogBox=wx.MessageBox(u"修改DNS成功",u"成功^_^")
			else:
				self.dialogBox=wx.MessageBox(u"修改DNS失败,请使用管理员运行!",u"失败咯@_@")
		else:
			exit()
		getValue = 100

    #Get input textCtr value
	def getpingaddr(self,event):
		global getIpName
		getIpName=event.GetString()
		
    #PING TOOLS
	def checkping(self,event):
		global getIpName
		pingVal=(os.popen('ping '+getIpName)).read()
		#pingVal= subprocess.check_output('ping '+getIpName)
		self.m_textCtrl6.SetValue(pingVal)
    
    #NSLOOKUP TOOLS
	def getNslookup(self,event):
		nslookupVal=(os.popen('nslookup '+getIpName)).read()
		self.m_textCtrl6.SetValue(nslookupVal)

    #CLEAR TEXTCtr
	def clearNote(self,event):
		self.m_textCtrl6.Clear()
    
    #HOSTS CHECK TOOLS
	def checkhosts(self,event):
		fh=open("C:\Windows\System32\drivers\etc\hosts","rb")
		for i in fh.readlines():
			self.m_textCtrl6.AppendText(str(i)+'\r\n')	
    
    #HOSTS RESET TOOLS
	def clearhosts(self,event):
		rwhosts='######clear hosts######\r\n127.0.0.1 localhost'
		try:
			fo = open("C:\Windows\System32\drivers\etc\hosts","wb")
			fo.writelines(rwhosts)
		except IOError:
			self.dialogBox=wx.MessageBox(u"重置hosts失败,请使用管理员运行!",u"失败咯@_@")
		else:
			self.dialogBox=wx.MessageBox(u"重置hosts成功",u"成功^_^")
			fo.close()
 

    #Get input HOSTS textCtr value
	def getHostsname(self,event):
		global getHosts
		getHosts=event.GetString()


    #SET HOSTS 
	def setHosts(self,event):
		setHost='\r\n'+getHosts
		try:
			fo = open("C:\Windows\System32\drivers\etc\hosts","a")
			fo.write(setHost)
		except IOError:
			self.dialogBox=wx.MessageBox(u"绑定hosts失败,请使用管理员运行!",u"失败咯@_@")
		else:
			self.dialogBox=wx.MessageBox(u"绑定hosts成功",u"成功^_^")
			fo.close()

		
    #DNS SET DHCP
	def setNetworkDhcp(self,event):
		wmiService = wmi.WMI ()
		colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)
		objNicConfig=colNicConfigs[0]
		returnValue =objNicConfig.SetDNSServerSearchOrder()
		returnValue =objNicConfig.EnableDHCP()
		if returnValue[0] == 0 :
			self.dialogBox=wx.MessageBox(u"还原DNS成功",u"成功^_^")
		elif returnValue[0] == 1 :
			self.dialogBox=wx.MessageBox(u"还原DNS成功",u"成功^_^")
		else:
			self.dialogBox=wx.MessageBox(u"还原DNS失败,请使用管理员运行!",u"失败=_=||")

			
	def __del__( self ):
		pass

#DNS CHANGE
def setNicDnsAddr(ip):
    global getValue
    wmiService = wmi.WMI ()
    colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)
    objNicConfig=colNicConfigs[0]
    arrDNSServers = [ip]
    returnValue =objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder = arrDNSServers)
    getValue = returnValue

	

if __name__ == '__main__':
    app = wx.App()
    MyFrame().Show()
    app.MainLoop()