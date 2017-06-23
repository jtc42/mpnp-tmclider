# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Apr 24 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"TMClider GUI", pos = wx.DefaultPosition, size = wx.Size( 296,262 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText_pol = wx.StaticText( self, wx.ID_ANY, u"Polariser angle (deg.)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_pol.Wrap( -1 )
		bSizer5.Add( self.m_staticText_pol, 0, wx.ALL, 5 )
		
		gSizer21 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_spinCtrl_pol = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, -360, 360, 0 )
		gSizer21.Add( self.m_spinCtrl_pol, 0, wx.ALL, 5 )
		
		self.m_button_polzero = wx.Button( self, wx.ID_ANY, u"Zero/Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer21.Add( self.m_button_polzero, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( gSizer21, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_radioBox_qwpChoices = [ u"RCP", u"LCP", u"Custom" ]
		self.m_radioBox_qwp = wx.RadioBox( self, wx.ID_ANY, u"QWP angle", wx.DefaultPosition, wx.DefaultSize, m_radioBox_qwpChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_qwp.SetSelection( 2 )
		gSizer2.Add( self.m_radioBox_qwp, 0, wx.ALL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText_qwpcustom = wx.StaticText( self, wx.ID_ANY, u"Custom angle (deg.)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_qwpcustom.Wrap( -1 )
		bSizer2.Add( self.m_staticText_qwpcustom, 0, wx.ALL, 5 )
		
		self.m_spinCtrl_qwp = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, -360, 360, 0 )
		bSizer2.Add( self.m_spinCtrl_qwp, 0, wx.ALL, 5 )
		
		self.m_button_qwpzero = wx.Button( self, wx.ID_ANY, u"Zero/Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button_qwpzero, 0, wx.ALL, 5 )
		
		
		gSizer2.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button_saveconfig = wx.Button( self, wx.ID_ANY, u"Save calibration", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button_saveconfig, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose_MainFrame )
		self.m_spinCtrl_pol.Bind( wx.EVT_SPINCTRL, self.OnSpin_pol )
		self.m_spinCtrl_pol.Bind( wx.EVT_TEXT_ENTER, self.OnSpin_pol )
		self.m_button_polzero.Bind( wx.EVT_BUTTON, self.OnButtonClick_polzero )
		self.m_radioBox_qwp.Bind( wx.EVT_RADIOBOX, self.OnRadioBox_QWP )
		self.m_spinCtrl_qwp.Bind( wx.EVT_SPINCTRL, self.OnSpin_qwp )
		self.m_spinCtrl_qwp.Bind( wx.EVT_TEXT_ENTER, self.OnSpin_qwp )
		self.m_button_qwpzero.Bind( wx.EVT_BUTTON, self.OnButtonClick_qwpzero )
		self.m_button_saveconfig.Bind( wx.EVT_BUTTON, self.OnButtonclick_saveconfig )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose_MainFrame( self, event ):
		event.Skip()
	
	def OnSpin_pol( self, event ):
		event.Skip()
	
	
	def OnButtonClick_polzero( self, event ):
		event.Skip()
	
	def OnRadioBox_QWP( self, event ):
		event.Skip()
	
	def OnSpin_qwp( self, event ):
		event.Skip()
	
	
	def OnButtonClick_qwpzero( self, event ):
		event.Skip()
	
	def OnButtonclick_saveconfig( self, event ):
		event.Skip()
	

###########################################################################
## Class LoaderFrame
###########################################################################

class LoaderFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 249,116 ), style = wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText_loading = wx.StaticText( self, wx.ID_ANY, u"Initialising slider...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_loading.Wrap( -1 )
		bSizer3.Add( self.m_staticText_loading, 0, wx.ALL, 5 )
		
		self.m_gauge_loading = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_loading.SetValue( 100 ) 
		bSizer3.Add( self.m_gauge_loading, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

