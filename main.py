import time

# Import wx files
import wx
import gui

import slider

pol = slider.motors[0]
qwp = slider.motors[1]

class MainFrame(gui.MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MainFrame.__init__(self,parent)
    
    ## On close frame
    def OnClose_MainFrame(self, event):
        slider.home_motors(slider.motors)
        self.Destroy()
        
    ## Polariser controls
        
    def OnSpin_pol(self, event):
        selected_angle = self.m_spinCtrl_pol.GetValue()
        print("Polariser angle: {}".format(selected_angle))
        qwp_angle = qwp.get_angle()
        pol.backlashAngle(selected_angle)
        qwp.backlashAngle(qwp_angle)
        qwp.angle(qwp_angle)
        pol.angle(selected_angle)
        
    def OnButtonClick_polzero(self, event):
        selected_angle = self.m_spinCtrl_pol.GetValue()
        pol.set_offset_angle(selected_angle)
        self.m_spinCtrl_pol.SetValue(0)
        
    ## Waveplate controls
        
    def OnRadioBox_QWP(self, event):
        if self.m_radioBox_qwp.GetSelection() != 2:
            self.m_spinCtrl_qwp.Disable()
            self.m_button_qwpzero.Disable()
        else:
            # Enable custom angle control box
            self.m_spinCtrl_qwp.Enable()
            self.m_button_qwpzero.Enable()
            
            # Set QWP to custom angle
            selected_angle = self.m_spinCtrl_qwp.GetValue()
            pol_angle = pol.get_angle()
            qwp.backlashAngle(selected_angle)
            pol.backlashAngle(pol_angle)
            pol.angle(pol_angle)
            qwp.angle(selected_angle)
        
        # If RCP or LCP, set accordingly
        pol_angle = pol.get_angle()
        pol.backlashAngle(pol_angle)
        if self.m_radioBox_qwp.GetSelection() == 0:
            qwp.backlashAngle(pol_angle-45)
            qwp.angle(pol_angle-45)
            pol.angle(pol_angle)

        elif self.m_radioBox_qwp.GetSelection() == 1:
            qwp.backlashAngle(pol_angle+45)
            qwp.angle(pol_angle+45)
            pol.angle(pol_angle)

    def OnSpin_qwp(self, event):
        selected_angle = self.m_spinCtrl_qwp.GetValue()
        print("Waveplate angle: {}".format(selected_angle))
        pol_angle = pol.get_angle()
        qwp.backlashAngle(selected_angle)
        pol.backlashAngle(pol_angle)
        pol.angle(pol_angle)
        qwp.angle(selected_angle)
    
    def OnButtonClick_qwpzero(self, event):
        selected_angle = self.m_spinCtrl_qwp.GetValue()
        qwp.set_offset_angle(selected_angle)
        self.m_spinCtrl_qwp.SetValue(0)
        
    def OnButtonclick_saveconfig(self, event):
        slider.save_prefs()

app = wx.App(False)

# Create loader frame
frame = MainFrame(None)
frame.Show()

# Start the applications
app.MainLoop()



