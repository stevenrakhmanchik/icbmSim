#!/usr/bin/env pythonw2.7
import wx, wx.adv
from wx.lib import plot
import sys,os,string
from math import *
from simssj2 import *

class ParamsPanel(wx.Panel):
    def __init__(self, parent, id,presets):
        wx.Panel.__init__(self, parent, id)
        self.presets = presets #ext ref for loading presets
        self.SetBackgroundColour('WHITE')

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.MainSizer = wx.FlexGridSizer(4,1,vgap=15,hgap=10)
        self.MainSizer.SetMinSize((600, 500))
        self.MiddleSizer = wx.FlexGridSizer(15,6,vgap=5,hgap=0)
        preset_list = ['']
        preset_list.extend(presets.keys())
        preset_list.sort()
        PresetChoice = wx.Choice(self,-1,choices=preset_list)
        PresetChoice.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.OnPresetChoice, PresetChoice)
        text = wx.StaticText(self,-1,'Preset Missiles',(20,100))
        font = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.BOLD)
        text.SetFont(font)
        self.MiddleSizer.Add(text,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(PresetChoice,0,wx.ALIGN_CENTER|wx.BOTTOM,border=5)
        self.MiddleSizer.Add(wx.StaticText(self,-1,'')) #blank



        #Number of Fins
        FinsNumberText = wx.StaticText(self,-1,"Number of Fins")
        self.FinsNumberControl = NumCtrl(self,-1,"Number of Fins")
        self.MiddleSizer.Add(FinsNumberText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.FinsNumberControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1,"    "),0,wx.ALIGN_LEFT)

        #Payload Weight
        PayloadWeightText = wx.StaticText(self,-1,"Payload Weight")
        self.PayloadWeightControl = NumCtrl(self,-1,"Payload Weight (kg)")
        UnitKilograms = wx.StaticText(self,-1,"kg        ")
        self.MiddleSizer.Add(PayloadWeightText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.PayloadWeightControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(UnitKilograms,0,wx.ALIGN_LEFT)

        #Fin Height
        FinHeightText = wx.StaticText(self,-1,"S: Fin Span")
        self.FinHeightControl = NumCtrl(self,-1,"S: Fin Span (m)")
        self.MiddleSizer.Add(FinHeightText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.FinHeightControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1,"    m  "),0,wx.ALIGN_LEFT)
        #self.StageResultSizer.Add(wx.StaticText(self,-1,"km/s"),(1,6),flag=wx.ALIGN_LEFT)

        #Reentry Vehicle
        RVText = wx.StaticText(self,-1,"RV Diameter")
        self.RVControl = NumCtrl(self,-1,"Diameter of re-entry vehicle (m). Set to zero to ignore drag on re-entry.")
        self.MiddleSizer.Add(RVText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.RVControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1,"m          "),0,wx.ALIGN_LEFT)

        #Fin Sweep Angle
        SweepAngleText = wx.StaticText(self,-1,"Sweep Angle")
        self.SweepAngleControl = NumCtrl(self,-1,"Sweep Angle")
        self.MiddleSizer.Add(SweepAngleText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.SweepAngleControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1,"    deg   "),0,wx.ALIGN_LEFT)

        #Nozzle Area
        NozzleText = wx.StaticText(self,-1,"Total Nozzle Area")
        self.NozzleControl = NumCtrl(self,-1,"Total Area of all nozzles")
        self.MiddleSizer.Add(NozzleText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.NozzleControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1,"m^2           "),0,wx.ALIGN_LEFT)
        print("line 94")

        #Fin Chord Length
        FinTipChordLengthText = wx.StaticText(self,-1,"CT: Fin Tip Chord")
        self.FinTipChordLengthControl = NumCtrl(self,-1,"CT: Fin Tip Chord")
        self.MiddleSizer.Add(FinTipChordLengthText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.FinTipChordLengthControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1,"    m    "),0,wx.ALIGN_LEFT)

		#Nosecone (L/D)
        LdivDText = wx.StaticText(self,-1,"Nosecone: (Length/Diameter)")
        self.LdivDControl = NumCtrl(self,-1,"(L/D) [dimensionless]")
        self.MiddleSizer.Add(LdivDText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.LdivDControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1,"           "),0,wx.ALIGN_LEFT)
        # print("line 94")

        #Fin Root Chord
        FinRootChordText = wx.StaticText(self,-1,"CR: Fin Root Chord")
        self.FinRootChordControl = NumCtrl(self,-1,"CR: Fin Root Chord")
        self.MiddleSizer.Add(FinRootChordText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.FinRootChordControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1,"    m  "),0,wx.ALIGN_LEFT)

		#Max Diameter
        DiameterText = wx.StaticText(self,-1,"Missile Diameter")
        self.DiameterControl = NumCtrl(self,-1,"Diameter of missile")
        self.MiddleSizer.Add(DiameterText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.DiameterControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1,"m           "),0,wx.ALIGN_LEFT)

        hBox = wx.BoxSizer(wx.HORIZONTAL)

        #Fin Thickness
        FinThicknessText = wx.StaticText(self,-1,"Fin Thickness")
        self.FinThicknessControl = NumCtrl(self,-1,"Fin Thickness")
        self.MiddleSizer.Add(FinThicknessText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.FinThicknessControl,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1,"    m "),0,wx.ALIGN_LEFT)


        #Number of Stages
        StageChoiceText = wx.StaticText(self,-1,"Number of Stages")
        self.StageChoiceBox = wx.Choice(self,-1,choices = ['1','2','3','4','5'])
        self.StageChoiceBox.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.OnStageChoice, self.StageChoiceBox)
        self.MiddleSizer.Add(StageChoiceText,0,wx.ALIGN_LEFT)
        self.MiddleSizer.Add(self.StageChoiceBox,0,wx.ALIGN_CENTER)
        self.MiddleSizer.Add(wx.StaticText(self,-1," "),0) #add blank
        self.TopSizer = wx.FlexGridSizer(10,3,vgap=5, hgap=5)
        self.TrajectoryChoiceSizer = wx.FlexGridSizer(1,2, vgap=0, hgap=5)
        self.TrajectoryChoiceSizer.Add(wx.StaticText(self,-1,"Trajectory"),0)
        self.TrajectoryChoiceBox = wx.Choice(self,-1,choices = ['Minimum Energy','Burnout Angle'])
        self.TrajectoryChoiceSizer.Add(self.TrajectoryChoiceBox,0)
        self.Bind(wx.EVT_CHOICE, self.OnTrajectoryChoice, self.TrajectoryChoiceBox)
        self.TopSizer.Add(self.TrajectoryChoiceSizer,0)
        self.NoseconeChoiceSizer = wx.FlexGridSizer(1,2, vgap=0, hgap=5)
        self.NoseconeChoiceSizer.Add(wx.StaticText(self,-1,"Nosecone"),0)
        self.NoseconeChoiceBox = wx.Choice(self,-1,choices = ['Conical','V2','elliptical','parabolic','sears-haack','tangent ogive'])
        self.NoseconeChoiceSizer.Add(self.NoseconeChoiceBox,0)
        self.Bind(wx.EVT_CHOICE, self.OnNoseconeChoice, self.NoseconeChoiceBox)
        self.TopSizer.Add(self.NoseconeChoiceSizer,0)

        self.EstRangeSizer = wx.FlexGridSizer(1,3, vgap=0, hgap=5)
        self.EstRangeSizer.Add(wx.StaticText(self,-1,"Est. Range"),0)
        self.EstRangeControl = NumCtrl(self,-1,"Estimated range (km). Forces missile to MET after stage 1 burnout.")
        self.EstRangeSizer.Add(self.EstRangeControl,0)
        self.EstRangeSizer.Add(wx.StaticText(self,-1,"km"),0)
        self.TopSizer.Add(self.EstRangeSizer,0)

        #ETA SIZER
        self.EtaSizer = wx.FlexGridSizer(2,4,hgap=5,vgap=10)
        self.EtaSizer.Add(wx.StaticText(self,-1,"For t>"),0)
        self.EtaTStartTurn = NumCtrl(self,-1,"Time to start missile turnover (sec)")
        self.EtaSizer.Add(self.EtaTStartTurn,0)
        self.EtaSizer.Add(wx.StaticText(self,-1,"to t<"),0)
        self.EtaTEndTurn = NumCtrl(self,-1,"Time to stop missile turnover (sec)")
        self.EtaSizer.Add(self.EtaTEndTurn,0)
        #next row
        self.EtaSizer.Add(wx.StaticText(self,-1,"Eta"),0)
        self.EtaTurnAngle = NumCtrl(self,-1,"Angle between thrust and velocity vectors for above timespan (deg)")
        self.EtaSizer.Add(self.EtaTurnAngle,0)
        self.TopSizer.Add(self.EtaSizer,0)

        self.BurnoutAngleSizer = wx.FlexGridSizer(0,0,vgap=0, hgap=5)
        self.BurnoutAngleSizer.Add(wx.StaticText(self,-1,"Burnout Angle"),0)
        self.BurnoutAngleCtrl = NumCtrl(self,-1,"Angle of missile on stage 1 burnout")
        self.BurnoutAngleSizer.Add(self.BurnoutAngleCtrl,0)
        self.BurnoutAngleSizer.Add(wx.StaticText(self,-1,"deg h"),0)
        self.TopSizer.Add(self.BurnoutAngleSizer,0)

        #TURN ANGLE SIZER
        self.TurnAngleSizer = wx.FlexGridSizer(2,4,hgap=5,vgap=10)
        self.TurnAngleSizer.Add(wx.StaticText(self,-1,"For t>"),0)
        self.TurnTimeStart = NumCtrl(self,-1,"Time to start missile turnover (sec)")
        self.TurnAngleSizer.Add(self.TurnTimeStart,0)
        self.TurnAngleSizer.Add(wx.StaticText(self,-1,"to t<"),0)
        self.TurnTimeEnd = NumCtrl(self,-1,"Time to stop missile turnover (sec)")
        self.TurnAngleSizer.Add(self.TurnTimeEnd)
        #next row
        self.TurnAngleSizer.Add(wx.StaticText(self,-1,"Gamma"),0)
        self.TurnAngleStart = NumCtrl(self,-1,"Turnover angle at start (deg from vertical)")
        self.TurnAngleSizer.Add(self.TurnAngleStart)
        self.TurnAngleSizer.Add(wx.StaticText(self,-1,"Gamma"),0)
        self.TurnAngleEnd = NumCtrl(self,-1,"Turnover angle at end (deg from vertical)")
        self.TurnAngleSizer.Add(self.TurnAngleEnd)
        self.TopSizer.Add(self.TurnAngleSizer,0)

        #start with MET
        self.TrajectoryChoiceBox.SetSelection(0)
        self.TopSizer.Hide(self.BurnoutAngleSizer)
        self.TopSizer.Hide(self.EtaSizer)
        self.TopSizer.Hide(self.TurnAngleSizer)
        self.TopSizer.Show(self.EstRangeSizer)
        self.Layout()

        #start with Nosecone
        self.NoseconeChoiceBox.SetSelection(0)
        #self.TopSizer.Show(self.NoseconeSizer)
		# This is where I would enter other cones as well.
        self.Layout()


        #END MIDDLE SIZER

        #STAGE SIZER
        self.StageSizer = wx.GridBagSizer(5,6)
        self.StageSizer.Add(wx.StaticText(self,-1,"Fuel Mass"),(1,0))
        self.StageSizer.Add(wx.StaticText(self,-1,"Dry Mass"),(2,0))
        self.StageSizer.Add(wx.StaticText(self,-1,"Isp"),(3,0))
        self.StageSizer.Add(wx.StaticText(self,-1,"Thrust"),(4,0))
        #create empty list to hold objects
        self.StageNumberText=['']
        self.StageFuelMassCtrl=['']
        self.StageDryMassCtrl=['']
        self.StageIspCtrl=['']
        self.StageThrustCtrl=['']
        #create all stage data fields
        for i in range(1,6):
            self.StageNumberText.append(wx.StaticText(self,-1,"Stage %d" % i))
            self.StageSizer.Add(self.StageNumberText[i],(0,i),flag=wx.ALIGN_CENTER|wx.ALL,border=10)
            self.StageFuelMassCtrl.append(NumCtrl(self,-1,"Stage %i fuel mass (kg)" % i))
            self.StageSizer.Add(self.StageFuelMassCtrl[i],(1,i))
            self.StageDryMassCtrl.append(NumCtrl(self,-1,"Stage %i dry mass (kg)" % i))
            self.StageSizer.Add(self.StageDryMassCtrl[i],(2,i))
            if i == 1:
                isptype = "sea level"
            else:
                isptype = "vacuum"
            self.StageIspCtrl.append(NumCtrl(self,-1,"Stage %i specific impulse at %s (sec)" % (i,isptype)))
            self.StageSizer.Add(self.StageIspCtrl[i],(3,i))
            self.StageThrustCtrl.append(NumCtrl(self,-1,"Stage %i thrust (kg force)" % i))
            self.StageSizer.Add(self.StageThrustCtrl[i],(4,i))
        #hide all except first column
        for i in range(2,6):
            self.StageSizer.Hide(self.StageNumberText[i])
            self.StageSizer.Hide(self.StageFuelMassCtrl[i])
            self.StageSizer.Hide(self.StageDryMassCtrl[i])
            self.StageSizer.Hide(self.StageIspCtrl[i])
            self.StageSizer.Hide(self.StageThrustCtrl[i])

        #place units labels
        self.StageSizer.Add(wx.StaticText(self,-1,"kg"),(1,6),flag=wx.ALIGN_LEFT)
        self.StageSizer.Add(wx.StaticText(self,-1,"kg"),(2,6),flag=wx.ALIGN_LEFT)
        self.StageSizer.Add(wx.StaticText(self,-1,"sec"),(3,6),flag=wx.ALIGN_LEFT)
        self.StageSizer.Add(wx.StaticText(self,-1,"kg f"),(4,6),flag=wx.ALIGN_LEFT)


        #Bottom Button
        RunButton = wx.Button(self,-1,"Run Simulation")
        self.Bind(wx.EVT_BUTTON,self.OnRun, RunButton)
        RunButton.SetDefault()
        RunButton.SetSize(RunButton.GetBestSize())

        self.MainSizer.Add(self.MiddleSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT|wx.TOP,10)
        self.MainSizer.Add(self.TopSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,10)
        self.MainSizer.Add(self.StageSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,10)
        self.MainSizer.Add(RunButton,0,wx.ALIGN_LEFT|wx.EXPAND | wx.ALL, 50)
        self.MainSizer.SetSizeHints(self)

        #final setup
        self.SetSizer(self.MainSizer)
        self.SetAutoLayout(1)
        self.Layout()

    def OnFinsChoice(self, event, numfins_override=None):
        #event handler for number of stages
        if numfins_override:
            numfins = numfins_override
            #used when loading numfins from preset, SetValue doesn't call event handler
        else:
            numfins = int(event.GetString())
            print "NUMFINS=",numfins
            if numfins !=0:
                #self.StageSizer.Show(self.FinsNumberText)

                ''' #Fin Height
                FinHeightText = wx.StaticText(self,-1,"Fin Height")
                self.FinHeightControl = NumCtrl(self,-1,"Fin Height (m)")
                self.MiddleSizer.Add(FinHeightText,0,wx.ALIGN_LEFT)
                self.MiddleSizer.Add(self.FinHeightControl,0,wx.ALIGN_CENTER)
                self.MiddleSizer.Add(wx.StaticText(self,-1,"m"),0,wx.ALIGN_LEFT)

                #Fin Sweep Angle
                SweepAngleText = wx.StaticText(self,-1,"Sweep Angle (degC)")
                self.SweepAngleControl = NumCtrl(self,-1,"Sweep Angle (deg C)")
                self.MiddleSizer.Add(SweepAngleText,0,wx.ALIGN_LEFT)
                self.MiddleSizer.Add(self.SweepAngleControl,0,wx.ALIGN_CENTER)
                self.MiddleSizer.Add(wx.StaticText(self,-1,"m"),0,wx.ALIGN_LEFT)

                #Fin Chord Length
                FinTipChordLengthText = wx.StaticText(self,-1,"Fin Tip Chord Length")
                self.FinTipChordLengthControl = NumCtrl(self,-1,"Fin Tip Chord Length (m)")
                self.MiddleSizer.Add(FinTipChordLengthText,0,wx.ALIGN_LEFT)
                self.MiddleSizer.Add(self.FinTipChordLengthControl,0,wx.ALIGN_CENTER)
                self.MiddleSizer.Add(wx.StaticText(self,-1,"m"),0,wx.ALIGN_LEFT)

                #Fin Root Chord
                FinRootChordText = wx.StaticText(self,-1,"Fin Root Chord")
                self.FinRootChordControl = NumCtrl(self,-1,"Fin Root Chord (m)")
                self.MiddleSizer.Add(FinRootChordText,0,wx.ALIGN_LEFT)
                self.MiddleSizer.Add(self.FinRootChordControl,0,wx.ALIGN_CENTER)
                self.MiddleSizer.Add(wx.StaticText(self,-1,"m"),0,wx.ALIGN_LEFT)

                #Fin Thickness
                FinThicknessText = wx.StaticText(self,-1,"Fin Thickness")
                self.FinThicknessControl = NumCtrl(self,-1,"Fin Thickness (m)")
                self.MiddleSizer.Add(FinThicknessText,0,wx.ALIGN_LEFT)
                self.MiddleSizer.Add(self.FinThicknessControl,0,wx.ALIGN_CENTER)
                self.MiddleSizer.Add(wx.StaticText(self,-1,"m"),0,wx.ALIGN_LEFT)





                self.FinsSizer.Show(self.FinHeight)   # S
                self.FinsSizer.Show(self.SweepAngle)  # Angle
                self.FinsSizer.Show(self.FinTipChordLength) # CT[m]
                self.FinsSizer.Show(self.FinRootChord) # CR[m]
                self.FinsSizer.Show(self.FinThickness) # TF[m]
                '''
        self.Layout()


    def OnStageChoice(self, event, numstage_override=None):
        #event handler for number of stages
        if numstage_override:
            numstages = numstage_override
            #used when loading numstages from preset, SetValue doesn't call event handler
        else:
            numstages = int(event.GetString())
            print "NUMSTAGES=",numstages
        #show requested stages
        for i in range(1,numstages+1):
            self.StageSizer.Show(self.StageNumberText[i])
            self.StageSizer.Show(self.StageFuelMassCtrl[i])
            self.StageSizer.Show(self.StageDryMassCtrl[i])
            self.StageSizer.Show(self.StageIspCtrl[i])
            self.StageSizer.Show(self.StageThrustCtrl[i])
        #hide others
        for i in range(numstages+1,6):
            self.StageSizer.Hide(self.StageNumberText[i])
            self.StageFuelMassCtrl[i].SetValue("")
            self.StageSizer.Hide(self.StageFuelMassCtrl[i])
            self.StageDryMassCtrl[i].SetValue("")
            self.StageSizer.Hide(self.StageDryMassCtrl[i])
            self.StageIspCtrl[i].SetValue("")
            self.StageSizer.Hide(self.StageIspCtrl[i])
            self.StageThrustCtrl[i].SetValue("")
            self.StageSizer.Hide(self.StageThrustCtrl[i])
        self.Layout()



    def OnNoseconeChoice(self,event):
        choice = event.GetString()
        print('Your choice is:'+ choice)

    def OnTrajectoryChoice(self,event):
        choice = event.GetString()
        if choice == 'Minimum Energy':
            self.TopSizer.Show(self.EstRangeSizer)
            self.TopSizer.Hide(self.EtaSizer)
            self.TopSizer.Hide(self.BurnoutAngleSizer)
            self.TopSizer.Hide(self.TurnAngleSizer)
        if choice == 'Thrust Vector':
            self.TopSizer.Show(self.EtaSizer)
            self.TopSizer.Hide(self.EstRangeSizer)
            self.TopSizer.Hide(self.BurnoutAngleSizer)
            self.TopSizer.Hide(self.TurnAngleSizer)
        if choice == 'Burnout Angle':
            self.TopSizer.Show(self.BurnoutAngleSizer)
            self.TopSizer.Hide(self.EtaSizer)
            self.TopSizer.Hide(self.EstRangeSizer)
            self.TopSizer.Hide(self.TurnAngleSizer)
        if choice == 'Turn Angle':
            self.TopSizer.Show(self.TurnAngleSizer)
            self.TopSizer.Hide(self.EtaSizer)
            self.TopSizer.Hide(self.EstRangeSizer)
            self.TopSizer.Hide(self.BurnoutAngleSizer)
        self.Layout()

    def OnPresetChoice(self, event):
        try:
            preset_data = self.presets[event.GetString()]
            numstages = preset_data['numstages']
            self.PayloadWeightControl.SetValue(str(preset_data['payload']))
            self.RVControl.SetValue(str(preset_data['rvdiam']))
            self.NozzleControl.SetValue(str(preset_data['nozzlearea']))
            self.LdivDControl.SetValue(str(preset_data['LdivD']))
            self.EstRangeControl.SetValue(str(preset_data['estrange']))
            self.StageChoiceBox.SetSelection(numstages-1)
            self.DiameterControl.SetValue(str(preset_data['missilediam']))

            for i in range(1,numstages+1):
                self.StageFuelMassCtrl[i].SetValue(str(preset_data['fuelmass'][i]))
                self.StageDryMassCtrl[i].SetValue(str(preset_data['drymass'][i]))
                self.StageIspCtrl[i].SetValue(str(preset_data['Isp0'][i]))
                self.StageThrustCtrl[i].SetValue(str(preset_data['thrust0'][i]))
        except KeyError:
            print("missing param in presets.py")

        try:
            self.OnStageChoice(None,numstage_override=numstages)
        except UnboundLocalError:
            #when choosing null twice, catch error
            pass

    def OnRun(self,event):
        sim = Simulation(self)

        try:

            sim.FinHeight = float(self.FinHeightControl.GetValue())
            sim.SweepAngle = float(self.SweepAngleControl.GetValue())
            sim.FinTipChordLength = float(self.FinTipChordLengthControl.GetValue())
            sim.FinRootChord = float(self.FinRootChordControl.GetValue())
            sim.FinThickness = float(self.FinThicknessControl.GetValue())
            sim.FinsNumber = float(self.FinsNumberControl.GetValue())


            sim.payload = float(self.PayloadWeightControl.GetValue())
            sim.rvdiam = float(self.RVControl.GetValue())
            sim.nozzlearea = float(self.NozzleControl.GetValue())
            sim.LdivD = float(self.LdivDControl.GetValue())
            sim.missilediam = float(self.DiameterControl.GetValue())
            sim.Nosecone = self.NoseconeChoiceBox.GetStringSelection()
            sim.trajectory = self.TrajectoryChoiceBox.GetStringSelection()
            if sim.trajectory == 'Minimum Energy':
                sim.est_range = float(self.EstRangeControl.GetValue())*1000 #convert to m

            if sim.trajectory == 'Thrust Vector':
                sim.TStartTurn = float(self.EtaTStartTurn.GetValue())
                sim.TEndTurn = float(self.EtaTEndTurn.GetValue())
                sim.TurnAngle = float(self.EtaTurnAngle.GetValue())

            if sim.trajectory == 'Burnout Angle':
                sim.burnout_angle = float(self.BurnoutAngleCtrl.GetValue())

            if sim.trajectory == 'Turn Angle':
                sim.TurnTimeStart = float(self.TurnTimeStart.GetValue())
                sim.TurnTimeEnd = float(self.TurnTimeEnd.GetValue())
                sim.TurnAngleStart = float(self.TurnAngleStart.GetValue())
                sim.TurnAngleEnd = float(self.TurnAngleEnd.GetValue())


            sim.numstages = int(self.StageChoiceBox.GetSelection()+1)
            print 'sim.numstages =',sim.numstages

            for i in range(1,sim.numstages+1):
                sim.fuelmass.append(float(self.StageFuelMassCtrl[i].GetValue()))
                sim.m0.append(float(self.StageDryMassCtrl[i].GetValue())+sim.fuelmass[i])
                sim.fuelfraction.append(float(sim.fuelmass[i]/sim.m0[i]))
                sim.Isp0.append(float(self.StageIspCtrl[i].GetValue()))
                sim.thrust0.append(float(self.StageThrustCtrl[i].GetValue())*9.81)
                sim.dMdt.append(float(sim.thrust0[i]/(sim.Isp0[i]*9.81)))

            self.sim = sim #external reference for writing sim params to file

            app = wx.GetTopLevelParent(self)

            #run sim, saving results
            trajectory = self.TrajectoryChoiceBox.GetStringSelection()
            app.Results.data = sim.integrate(trajectory)

			#run sim, saving results
            Nosecone = self.NoseconeChoiceBox.GetStringSelection()
            app.Results.data = sim.integrate(Nosecone)

            app.nb.AdvanceSelection(forward=True) #turn to results page


            #show requested stages
            other = app.Results #short ref for below calls
            for i in range(1,sim.numstages+1):
                other.StageResultSizer.Show(other.StageNumberText[i])
                other.StageResultSizer.Show(other.StageVelocityResult[i])
                other.StageResultSizer.Show(other.StageAngleResult[i])
                other.StageResultSizer.Show(other.StageHeightResult[i])
                other.StageResultSizer.Show(other.StageRangeResult[i])
                other.StageResultSizer.Show(other.StageTimeResult[i])
                other.StageResultSizer.Show(other.StageMachResult[i])

            """ #hide unused stages in Results panel
            for i in range(sim.numstages+0,6):
                other.StageResultSizer.Hide(app.Results.StageNumberText[i])
                other.StageResultSizer.Hide(other.StageVelocityResult[i])
                other.StageResultSizer.Hide(other.StageAngleResult[i])
                other.StageResultSizer.Hide(other.StageHeightResult[i])
                other.StageResultSizer.Hide(other.StageRangeResult[i])
                other.StageResultSizer.Hide(other.StageTimeResult[i])
                other.StageResultSizer.Hide(other.StageMachResult[i]) """
            app.Results.Layout()

        except ValueError:
            #Validator should take care of this, but just in case.
            dlg = wx.MessageDialog(self,"Please make sure all fields are filled in.","Entry error",wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

class PlotFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, (550,30), (600, 400))
        self.canvas = plot.PlotCanvas(self)
        #because PlotCanvas needs a frame, and won't play nice inside the main window

class ResultsPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        # COLOUR SET
        self.SetBackgroundColour('white')


        #RESULTS DATA DICTIONARY
        self.data = {'Time':[0],'Height':[0],'Velocity':[0],'Thrust':[0],'Drag':[0],'CD':[0],'cdfins':[0],'Gamma':[0],'Range':[0]}
        #create empty data dictionary

        app = wx.GetTopLevelParent(self)
        self.frame = PlotFrame(None,-1,"Results Plot")
        #create new plot window

        #MAIN SIZER
        MainResultsSizer = wx.FlexGridSizer(5,0,vgap=12,hgap=0)

        #RESULT SIZER
        FinalResultSizer = wx.FlexGridSizer(5,3,vgap=10,hgap=10)
        #Apogee
        FinalResultSizer.Add(wx.StaticText(self,-1,"Apogee"),0,wx.ALIGN_LEFT)
        self.ApogeeResult = NumCtrl(self,-1,"Largest height attained in flight (km)",style=wx.TE_READONLY)
        FinalResultSizer.Add(self.ApogeeResult,0,wx.ALIGN_CENTER)
        FinalResultSizer.Add(wx.StaticText(self,-1,"km"),0,wx.ALIGN_RIGHT)
        #V @ Apogee
        FinalResultSizer.Add(wx.StaticText(self,-1,"Apogee Velocity"),0,wx.ALIGN_LEFT)
        self.ApogeeVelocityResult = NumCtrl(self,-1,"Velocity at apogee (km/sec)",style=wx.TE_READONLY)
        FinalResultSizer.Add(self.ApogeeVelocityResult,0,wx.ALIGN_CENTER)
        FinalResultSizer.Add(wx.StaticText(self,-1,"km/s"),0,wx.ALIGN_RIGHT)
        #Range
        FinalResultSizer.Add(wx.StaticText(self,-1,"Range"),0,wx.ALIGN_LEFT)
        self.RangeResult = NumCtrl(self,-1,"Distance along earth surface to impact point (km)",style=wx.TE_READONLY)
        FinalResultSizer.Add(self.RangeResult,0,wx.ALIGN_CENTER)
        FinalResultSizer.Add(wx.StaticText(self,-1,"km"),0,wx.ALIGN_RIGHT)
        #Time
        FinalResultSizer.Add(wx.StaticText(self,-1,"Flight Time"),0,wx.ALIGN_LEFT)
        self.FlightTimeResult = NumCtrl(self,-1,"Time from liftoff to impact (sec)",style=wx.TE_READONLY)
        FinalResultSizer.Add(self.FlightTimeResult,0,wx.ALIGN_CENTER)
        FinalResultSizer.Add(wx.StaticText(self,-1,"sec"),0,wx.ALIGN_RIGHT)

        #STAGE RESULT SIZER
        self.StageResultSizer = wx.GridBagSizer(5,7)
        self.StageResultSizer.Add(wx.StaticText(self,-1,"Velocity"),(1,0))
        self.StageResultSizer.Add(wx.StaticText(self,-1,"Angle"),(2,0))
        self.StageResultSizer.Add(wx.StaticText(self,-1,"Height"),(3,0))
        self.StageResultSizer.Add(wx.StaticText(self,-1,"Range"),(4,0))
        self.StageResultSizer.Add(wx.StaticText(self,-1,"Time"),(5,0))
        #self.StageResultSizer.Add(wx.StaticText(self,-1,"Mach"),(6,0))
        #create empty list to hold objects
        self.StageNumberText=['']
        self.StageVelocityResult=['']
        self.StageAngleResult=['']
        self.StageHeightResult=['']
        self.StageRangeResult=['']
        self.StageTimeResult=['']
        self.StageMachResult=['']

        #create all stage data fields
        for i in range(1,6):
            self.StageNumberText.append(wx.StaticText(self,-1,"Stage %d" % i))
            self.StageResultSizer.Add(self.StageNumberText[i],(0,i),flag=wx.ALIGN_CENTER|wx.ALL,border=10)
            self.StageVelocityResult.append(NumCtrl(self,-1,"Velocity at stage %i burnout (km/sec)" % i,style=wx.TE_READONLY))
            self.StageResultSizer.Add(self.StageVelocityResult[i],(1,i))
            #self.StageMachResult.append(NumCtrl(self,-1,"Mach at stage %i burnout (mach)" % i,style=wx.TE_READONLY))
            #self.StageResultSizer.Add(self.StageMachResult[i],(1,i))
            self.StageAngleResult.append(NumCtrl(self,-1,"Angle at stage %i burnout (degrees from horizontal)" % i,style=wx.TE_READONLY))
            self.StageResultSizer.Add(self.StageAngleResult[i],(2,i))
            self.StageHeightResult.append(NumCtrl(self,-1,"Height at stage %i burnout (km)" % i,style=wx.TE_READONLY))
            self.StageResultSizer.Add(self.StageHeightResult[i],(3,i))
            self.StageRangeResult.append(NumCtrl(self,-1,"Range at stage %i burnout (km)" % i,style=wx.TE_READONLY))
            self.StageResultSizer.Add(self.StageRangeResult[i],(4,i))
            self.StageTimeResult.append(NumCtrl(self,-1,"Time of stage %i burnout (sec)" % i,style=wx.TE_READONLY))
            self.StageResultSizer.Add(self.StageTimeResult[i],(5,i))

        #place units labels
        self.StageResultSizer.Add(wx.StaticText(self,-1,"km/s"),(1,6),flag=wx.ALIGN_LEFT)
        self.StageResultSizer.Add(wx.StaticText(self,-1,"deg h"),(2,6),flag=wx.ALIGN_LEFT)
        self.StageResultSizer.Add(wx.StaticText(self,-1,"km"),(3,6),flag=wx.ALIGN_LEFT)
        self.StageResultSizer.Add(wx.StaticText(self,-1,"km"),(4,6),flag=wx.ALIGN_LEFT)
        self.StageResultSizer.Add(wx.StaticText(self,-1,"sec"),(5,6),flag=wx.ALIGN_LEFT)

        MainResultsSizer.Add(FinalResultSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT|wx.TOP,10)
        MainResultsSizer.Add(self.StageResultSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,10)

        #final setup
        self.SetSizer(MainResultsSizer)
        self.SetAutoLayout(1)
        self.Layout()

    def OnPlot(self,event):
        plot = []
        x = self.XRadioBox.GetStringSelection()
        y = self.YRadioBox.GetStringSelection()
        #print "Show Plot: %s vs %s" %(y,x)
        try:
            self.frame.Show(False) #hide previous
        except wx._core.PyDeadObjectError:
            #window has been closed by user, recreate
            self.frame = PlotFrame(None,-1,"Results Plot")
        self.frame.canvas.Reset() #clear previous
        self.frame.Show(True) #show blank

        #set plot title here before adding units to description string
        title = "%s vs %s" % (y,x)

        #determine stage burnouts
        app = wx.GetTopLevelParent(self)
        sim = app.Params.sim
        for i in range(1,sim.numstages+1):
            if x == "Time":
                x_stage = float(self.StageTimeResult[i].GetValue())
            if x == "Range":
                x_stage = float(self.StageRangeResult[i].GetValue())
            if x == "Velocity":
                x_stage = float(self.StageVelocityResult[i].GetValue())
            if x == "Mach":
                x_stage = float(self.StageMachResult[i].GetValue())

			#can't figure out y value
            #list lookup fails because array is floats w/ arbitrary precision
            #plot stage burnout
            plot.append(PolyMarker([(x_stage,0)],

                legend="Stage %d Burnout" % i,marker='cross',colour='red',size=1))

        #unit conversion
        if x == "Range":
            x_data = [elem/1000.0 for elem in self.data[x]] #convert to km
            x = x + ' (km)'
        elif x == "Time":
            x_data = self.data[x] #in seconds
            x = x + ' (sec)'
        elif x == "Velocity":
		    x_data = self.data[x]
        if y == "Drag":
            y_data = self.data[y] #in N
            y = y + ' (N)'
        elif y == "Gamma":
            y_data = [elem*(180.0/pi) for elem in self.data[y]] #convert to degrees
            y = y + ' (deg h)'
        elif y == "Height":
            h = self.data[y]
            y_data = [elem/1000.0 for elem in self.data[y]] #convert to km
            y = y + ' (km)'
        elif y == "Velocity":
            y_data = self.data[y] #in m/s
            y = y + ' (m/s)'
        elif y == "Thrust":
            y_data = self.data[y] #in N
            y = y + ' (N)'
        elif x == "Mach":
            h = self.data["Height"]
            # print h
            if h <= 11000.:
            #troposphere
               t = 15.04 - .00649*h
            elif h > 11000. and h <= 25000.:
            #lower stratosphere
               t = -56.46
            elif h > 25000.:
               t = 131.21 + .00299*h
            t = t + 273.15 #convert to kelvin
            a = sqrt(1.4*287*t)
            global x_data # note added this to not have the UnboundLocalError: https://eli.thegreenplace.net/2011/05/15/understanding-unboundlocalerror-in-python/
            # and I removed the def temperature(h) function since this is the same code.
            x_data = self.data["Velocity"]/a
        else:
            y_data = self.data[y] #for others, don't add units

        #plot trajectory line
        line = numpy.array(zip(x_data,y_data))
        plot.append(PolyLine(line,legend=x,colour='red'))

        self.frame.canvas.Draw(PlotGraphics(plot,title,x,y))



    def OnWriteToFile(self,event):

        dlg = wx.FileDialog(self, message="Save file as ...", defaultDir=os.getcwd(),
            defaultFile="data", style=wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.outfile = open(path,'w')

            app = wx.GetTopLevelParent(self) #get ref to AppFrame instance for printing stage params
            sim = app.Params.sim
            for i in range(1,sim.numstages+1):
                self.outfile.write("STAGE %i Parameters:\n" % i)
                self.outfile.write("Fuel mass (kg): " + str(sim.fuelmass[i]) + '\n')
                self.outfile.write("Dry mass (kg): " + str(sim.m0[i] - sim.fuelmass[i]) + '\n')
                self.outfile.write("Fuel fract: " + str(sim.fuelfraction[i]) + '\n')
                self.outfile.write("Isp: " + str(sim.Isp0[i]) + '\n')
                self.outfile.write("Burn time (sec): " + str(sim.burntime[i]) + '\n')
                self.outfile.write("Thrust (N): " + str(sim.thrust0[i]) + '\n')
                self.outfile.write("dM/dt: " + str(sim.dMdt[i]) + '\n')
            self.outfile.write("\nTIME,HEIGHT,VELOCITY,THRUST,DRAG,CD,GAMMA,RANGE\n")

            flat = zip(self.data['Time'],
                    self.data['Height'],
                    self.data['Velocity'],
                    self.data['Thrust'],
                    self.data['Drag'],
                    self.data['CD'],
                    self.data['cdfins'],
                    self.data['Gamma'],
                    self.data['Range'])
            #create flat list

            for i in range(1,len(flat)/2):
                for n in range(0,len(flat[i])):
                    self.outfile.write('%.3f' % flat[i][n])
                    self.outfile.write(',')
                self.outfile.write('\n')

            print("Data written to '%s'" % path)
            self.outfile.close()
        #clean up
        dlg.Destroy()



'''
class FinsPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        #MainSizer = wx.FlexGridSizer(4,1,vgap=25)
        MainSizer = wx.FlexGridSizer(0,1,vgap=25,hgap=0)

        TopSizer = wx.FlexGridSizer(1,2,vgap=0,hgap=10)

        self.png = wx.StaticBitmap(self, -1, wx.Bitmap("fins.png", wx.BITMAP_TYPE_ANY),pos=(540,10))

'''









class AdvancedPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        #MainSizer = wx.FlexGridSizer(4,1,vgap=25)
        MainSizer = wx.FlexGridSizer(0,1,vgap=25,hgap=0)

        TopSizer = wx.FlexGridSizer(1,2,vgap=0,hgap=10)
        VariableSizer = wx.FlexGridSizer(1,2,vgap=0,hgap=10)
        VariableSizer.Add(wx.StaticText(self,-1,"Solve for"),0,wx.ALIGN_LEFT)
        self.VariableChoice = wx.Choice(self,-1,choices = ["Fuel Fraction"])
        #self.VariableChoice.SetSelection(0) #only one kind of problem to solve
        VariableSizer.Add(self.VariableChoice,0,wx.ALIGN_LEFT)
        self.Bind(wx.EVT_CHOICE,self.OnChooseVar,self.VariableChoice)

        StageNumSizer = wx.FlexGridSizer(1,2,vgap=0,hgap=10)
        StageNumSizer.Add(wx.StaticText(self,-1,"Stage"),0)
        self.StageChoiceBox = wx.Choice(self,-1,choices = ['1','2','3','4','5'])
        StageNumSizer.Add(self.StageChoiceBox,0,wx.ALIGN_LEFT)
        self.StageChoiceBox.SetSelection(0)

        TopSizer.Add(VariableSizer,0)
        TopSizer.Add(StageNumSizer,0)

        # ConstraintSizer = wx.FlexGridSizer(3,3,hgap=10,vgap=10)
        ConstraintSizer = wx.FlexGridSizer(0,3,hgap=10,vgap=10)
        ConstraintSizer.Add(wx.StaticText(self,-1,"Stage Mass"),0,wx.ALIGN_LEFT)
        self.StageMassCtrl = NumCtrl(self,-1,"Fuel Mass + Dry Mass (kg). Does not include payload.")
        ConstraintSizer.Add(self.StageMassCtrl)
        ConstraintSizer.Add(wx.StaticText(self,-1,"kg"),0,wx.ALIGN_LEFT)

        ConstraintSizer.Add(wx.StaticText(self,-1,"Fuel Fraction"),0,wx.ALIGN_LEFT)
        self.FuelFractionCtrl = NumCtrl(self,-1,"Fuel Mass / Stage Mass")
        ConstraintSizer.Add(self.FuelFractionCtrl)
        ConstraintSizer.Add(wx.StaticText(self,-1,"%"),0,wx.ALIGN_LEFT)

        ConstraintSizer.Add(wx.StaticText(self,-1,"Fuel Mass"),0,wx.ALIGN_LEFT)
        self.FuelMassCtrl = NumCtrl(self,-1,"Fuel Mass (kg)",style=wx.TE_READONLY)
        ConstraintSizer.Add(self.FuelMassCtrl)
        ConstraintSizer.Add(wx.StaticText(self,-1,"kg"),0,wx.ALIGN_LEFT)

        ConstraintSizer.Add(wx.StaticText(self,-1,"Dry Mass"),0,wx.ALIGN_LEFT)
        self.DryMassCtrl = NumCtrl(self,-1,"Dry Mass (kg)",style=wx.TE_READONLY)
        ConstraintSizer.Add(self.DryMassCtrl)
        ConstraintSizer.Add(wx.StaticText(self,-1,"kg"),0,wx.ALIGN_LEFT)

        MiddleSizer = wx.FlexGridSizer(2,2,hgap=25,vgap=10)
        MiddleSizer.Add(wx.StaticText(self,-1,"Estimated Range"),0)
        self.AnsGuessControl = NumCtrl(self,-1,"Your guess for the missile range")
        MiddleSizer.Add(self.AnsGuessControl,0)

        SolveButton = wx.Button(self,-1,"Solve")
        self.Bind(wx.EVT_BUTTON,self.OnSolve, SolveButton)
        #SolveButton.SetDefault()
        #can't have two default buttons...
        SolveButton.SetSize(SolveButton.GetBestSize())

        AnswerSizer = wx.FlexGridSizer(2,2,hgap=5,vgap=5)
        AnswerSizer.Add(wx.StaticText(self,-1,"Variable"),0)
        self.AnswerControl = NumCtrl(self,-1,"First found value of the variable that gives the desired range",style=wx.TE_READONLY)
        AnswerSizer.Add(self.AnswerControl,0)
        AnswerSizer.Add(wx.StaticText(self,-1,"Range"),0)
        self.RangeControl = NumCtrl(self,-1,"Range with above variable",style=wx.TE_READONLY)
        AnswerSizer.Add(self.RangeControl,0)

        #use wx.Gauge for visual feedback
        self.max_runs = 25
        self.Gauge = wx.Gauge(self,-1,self.max_runs,size = [250,25],style = wx.GA_HORIZONTAL)

        MainSizer.Add(TopSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT|wx.TOP,10)
        MainSizer.Add(ConstraintSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,10)
        MainSizer.Add(MiddleSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,10)
        MainSizer.Add(SolveButton,0,wx.ALIGN_CENTER_HORIZONTAL)
        MainSizer.Add(self.Gauge,0,wx.ALIGN_CENTER_HORIZONTAL)
        MainSizer.Add(AnswerSizer,0,wx.ALIGN_CENTER_HORIZONTAL|wx.TOP,-20)

        self.SetSizer(MainSizer)
        self.SetAutoLayout(1)
        self.Layout()

    def OnChooseVar(self,event):
        "Gets control on Params panel for variable"
        app = wx.GetTopLevelParent(self)
        #get control for variable
        nstage = int(self.StageChoiceBox.GetSelection()+1)
        self.var_string = self.VariableChoice.GetStringSelection()
        if self.var_string == "Fuel Fraction":
            self.var_control = self.FuelFractionCtrl
            m_prop = float(app.Params.StageFuelMassCtrl[nstage].GetValue())
            m_struct = float(app.Params.StageDryMassCtrl[nstage].GetValue())
            self.StageMassCtrl.SetValue("%.2f" % (m_prop + m_struct))
            self.FuelFractionCtrl.SetValue("%.2f" % (m_prop/(m_struct+m_prop)*100))
            self.CheckConstraints()
        #set guesses
        self.AnsGuessControl.SetValue(app.Params.EstRangeControl.GetValue())

    def CheckConstraints(self):
        app = wx.GetTopLevelParent(self)
        nstage = int(self.StageChoiceBox.GetSelection()+1)
        self.var_string = self.VariableChoice.GetStringSelection()
        if self.var_string == "Fuel Fraction":
            m0 = float(self.StageMassCtrl.GetValue()) #keep stage mass const
            fuelfraction = float(self.FuelFractionCtrl.GetValue())/100
            if fuelfraction > 1:
                print("invalid fuel fraction, setting to maximum")
                fuelfraction = .99*100
                self.FuelFractionCtrl.SetValue("%.2f" % fuelfraction)
            if fuelfraction < 0:
                print("invalid fuel fraction, setting to minimum")
                fuelfraction = .01*100
                self.FuelFractionCtrl.SetValue("%.2f" % fuelfraction)
            m_prop = fuelfraction*m0
            m_struct = m0 - fuelfraction*m0
            self.FuelMassCtrl.SetValue("%.2f" % m_prop)
            self.DryMassCtrl.SetValue("%.2f" % m_struct)
            app.Params.StageFuelMassCtrl[nstage].SetValue("%.2f" % m_prop)
            app.Params.StageDryMassCtrl[nstage].SetValue("%.2f" % m_struct)
        else:
            pass
            #other constraints go here

    def OnSolve(self,event):
        "Solves for unknown variable iteratively. May take a while."

        if self.var_string == "":
            dlg = wx.MessageDialog(self,"Please choose a variable to solve for.","Unable to solve",wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return False

        try:
            #get solver params
            ans_est = float(self.AnsGuessControl.GetValue())
            var_est = float(self.var_control.GetValue())
        except ValueError:
                dlg = wx.MessageDialog(self,"Please fill in all fields.","Unable to solve",wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
                return False

        #print "Solve for stage",int(self.StageChoiceBox.GetSelection()+1),self.var_string

        #init search variables, need two starting values
        #f is sim range - ans_est, because secant method solves for roots
        oldx = var_est*.99 #hopefully still a reasonable value
        self.var_control.SetValue("%.2f" % oldx)
        oldf = self.RunSim() - ans_est

        x = var_est
        self.var_control.SetValue("%.2f" % var_est)
        f =  self.RunSim() - ans_est

        run = 0
        tolerance = 1e-2

        if (abs(f) > abs(oldf)):
            # swap so that f(x) is closer to 0
            #print "swap"
            oldx, x = x, oldx
            oldf, f = f, oldf

        while True:
            #secant method
            try:
                dx = f*(x - oldx)/(f - oldf)
                if abs(dx)<tolerance:
                    print("solved, tolerance")
                    break
            except ZeroDivisionError:
                print("solved, ZDE")
                break
            (oldx, x) = (x, x - dx)
            self.var_control.SetValue("%.2f" % x)
            (oldf, f) = (f, self.RunSim()-ans_est)
            run += 1 #increment run number
            print("sec(%d): x=%s, f(x)=%s, oldx=%s, oldf=%s,\n" % (run,x,f,oldx,oldf))
            self.Gauge.SetValue(run)
            self.AnswerControl.SetValue("%.2f" % x)
            self.RangeControl.SetValue("%.2f" % (f+ans_est))
            wx.Yield() #allow GUI to update
            if run > self.max_runs:
                dlg = wx.MessageDialog(self,"Solver failed to converge.","Unable to solve",wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
                return
        #end of loop
        #print("solved=",oldx)
        self.var_control.SetValue("%.2f" % oldx)
        self.AnswerControl.SetValue("%.2f" % oldx)
        self.Gauge.SetValue(self.max_runs)

        if self.var_string == "Fuel Fraction":
            #sanity check
            answer = float(self.AnswerControl.GetValue())
            if answer > 100 or answer < 0:
                dlg = wx.MessageDialog(self,"Solver converged on an invalid value. Try inputting a more reasonable starting value for the variable.","Unable to solve",wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()

    def RunSim(self):
        self.CheckConstraints()

        sim = Simulation(self)
        app = wx.GetTopLevelParent(self)
        try:
            sim.payload = float(app.Params.PayloadWeightControl.GetValue())
            sim.rvdiam = float(app.Params.RVControl.GetValue())
            sim.LdivD = float(app.Params.LdivDControl.GetValue())
            sim.missilediam = float(app.Params.DiameterControl.GetValue())
            sim.numstages = int(app.Params.StageChoiceBox.GetSelection()+1)
            sim.numfins = int(app.Params.FinsChoiceBox.GetSelection()+1)
            for i in range(1,sim.numstages+1):
                sim.fuelmass.append(float(app.Params.StageFuelMassCtrl[i].GetValue()))
                sim.m0.append(float(app.Params.StageDryMassCtrl[i].GetValue())+sim.fuelmass[i])
                sim.fuelfraction.append(float(sim.fuelmass[i]/sim.m0[i]))
                sim.Isp0.append(float(app.Params.StageIspCtrl[i].GetValue()))
                sim.thrust0.append(float(app.Params.StageThrustCtrl[i].GetValue())*9.81) #convert from kgf to N
                sim.dMdt.append(float(sim.thrust0[i]/(sim.Isp0[i]*9.81)))
            trajectory = app.Params.TrajectoryChoiceBox.GetStringSelection()
            Nosecone = app.Params.NoseconeChoiceBox.GetStringSelection()
            if trajectory == "Minimum Energy":
                sim.est_range = float(app.Params.EstRangeControl.GetValue())*1000 #convert to m
            if trajectory == 'Thrust Vector':
                sim.TStartTurn = float(self.EtaTStartTurn.GetValue())
                sim.TEndTurn = float(self.EtaTEndTurn.GetValue())
                sim.TurnAngle = float(self.EtaTurnAngle.GetValue())
            if trajectory == 'Burnout Angle':
                sim.burnout_angle = float(self.BurnoutAngleCtrl.GetValue())

        except ValueError:
                dlg = wx.MessageDialog(self,"Please fill in all fields in Parameters panel.","Unable to solve",wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
                #advance to params panel
        #run sim
        data = sim.integrate(trajectory)
        answer = float(app.Results.RangeResult.GetValue())
        #subtract from ans_est because method works to find zero
        del(sim) #delete last run
        del(data)
        return answer


class AppFrame(wx.Frame):

    def __init__(self, parent, id, title):
        # RESIZE THE APP FRAME HERE!
        wx.Frame.__init__(self, parent, id, title, (-1,-1), wx.Size(800,650)) # (width,length )
        font = wx.Font(8, wx.FONTFAMILY_SWISS, wx.NORMAL, wx.BOLD)
        wx.Frame.SetFont(self, font)

        # Now Create the menu bar and items
        self.MenuBar = wx.MenuBar()
        FileMenu = wx.Menu()
        #hack
        about = FileMenu.Append(-1, 'About...')
        self.Bind(wx.EVT_MENU,self.OnAbout,about)

        FileMenu.Append(200, 'Page Setup', 'Setup the printer page')
        wx.EVT_MENU(self, 200, self.OnFilePageSetup)
        FileMenu.Append(201, 'Print Preview', 'Show the current plot on page')
        wx.EVT_MENU(self, 201, self.OnFilePrintPreview)
        FileMenu.Append(202, 'Print Plot', 'Print the current plot')
        wx.EVT_MENU(self, 202, self.OnFilePrint)
        FileMenu.Append(203, 'Save Plot', 'Save current plot')
        wx.EVT_MENU(self, 203, self.OnSaveFile)
        FileMenu.Append(205, 'Q&uit', 'Quit this Application')
        wx.EVT_MENU(self,205, self.OnFileExit)
        if 'phoenix' in wx.PlatformInfo:
            wx.PyApp.SetMacExitMenuItemId(wx.ID_EXIT)
        else:
            wx.App_SetMacExitMenuItemId(205) #mac-ify
        self.MenuBar.Append(FileMenu, '&File')

        #Plot Menu, shamelessly stolen from wx.lib.plot.TestFrame
        PlotMenu = wx.Menu()
        PlotMenu.Append(211, '&Redraw', 'Redraw plot')
        self.Bind(wx.EVT_MENU,self.OnPlotRedraw, id=211)
        PlotMenu.Append(212, '&Clear', 'Clear canvas')
        self.Bind(wx.EVT_MENU,self.OnPlotClear, id=212)
        PlotMenu.Append(213, '&Scale', 'Scale canvas')
        self.Bind(wx.EVT_MENU,self.OnPlotScale, id=213)
        PlotMenu.Append(214, 'Enable &Zoom', 'Enable Mouse Zoom', kind=wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU,self.OnEnableZoom, id=214)
        PlotMenu.Append(215, 'Enable &Grid', 'Turn on Grid', kind=wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU,self.OnEnableGrid, id=215)
        PlotMenu.Append(220, 'Enable &Legend', 'Turn on Legend', kind=wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU,self.OnEnableLegend, id=220)
        PlotMenu.Append(222, 'Enable &Point Label', 'Show Closest Point', kind=wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU,self.OnEnablePointLabel, id=222)
        PlotMenu.Append(235, '&Plot Reset', 'Reset to original plot')
        self.Bind(wx.EVT_MENU,self.OnReset, id=235)
        self.MenuBar.Append(PlotMenu, '&Plot')

        #Help Menu
        HelpMenu = wx.Menu()
        HelpMenu.Append(300, '&About', 'About...')
        wx.EVT_MENU(self, 300, self.OnAbout)

        if wx.Platform == "__WXMAC__":
            if "phoenix" in wx.PlatformInfo:
                wx.PyApp.SetMacAboutMenuItemId(wx.ID_ABOUT)
                wx.PyApp.SetMacHelpMenuTitleName('&Help')
            else:
                wx.App.SetMacAboutMenuItemId(300)
                wx.App_SetMacHelpMenuTitleName("&Help")
        else:
            self.MenuBar.Append(HelpMenu, "&Help")
        self.SetMenuBar(self.MenuBar)
        self.CreateStatusBar(1)
        self.SetStatusText("")

        #load presets
        try:
            preset_path = os.path.join(self.get_main_dir(),"presets.515.txt")
            presets_file = open(preset_path,'r')
            presets = eval(presets_file.read())
        except SyntaxError:
            dlg = wx.MessageDialog(self,"Syntax error in presets.txt. Make sure there are no empty lines or statements.","Parse error",wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            presets = {'Error reading presets.txt':{}}

        #create tabs
        self.nb = wx.Notebook(self,-1)
        self.Params = ParamsPanel(self.nb, -1, presets)
        #elf.Fins = FinsPanel(self.nb, -1)
        self.Results = ResultsPanel(self.nb, -1)
        #self.Advanced = AdvancedPanel(self.nb, -1) TURNED OFF MAY 18

        self.nb.AddPage(self.Params, "Settings")
        #self.nb.AddPage(self.Fins, "Fin Geom Explanation")
        self.nb.AddPage(self.Results, "Results")
        #self.nb.AddPage(self.Advanced, "Advanced")

    def OnFilePageSetup(self, event):
        self.Results.frame.canvas.PageSetup()

    def OnFilePrintPreview(self, event):
        self.Results.frame.canvas.PrintPreview()

    def OnFilePrint(self, event):
        self.Results.frame.canvas.Printout()

    def OnSaveFile(self, event):
        self.Results.frame.canvas.SaveFile()

    def OnFileExit(self, event):
        sys.exit()

    def OnAbout(self, event):
        info = wx.adv.AboutDialogInfo()
        info.SetName('ICBM Simulator')
        info.SetDescription("It's not rocket science but it is a drag")
        info.SetLicence(__doc__)
        wx.adv.AboutBox(info)


    #Plot Event Handlers, shamelessly stolen from wx.lib.plot.TestFrame
    def OnPlotRedraw(self,event):
        self.Results.frame.canvas.Redraw()
    def OnPlotClear(self,event):
        self.Results.frame.canvas.Clear()
    def OnPlotScale(self, event):
        if self.Results.frame.canvas.last_draw != None:
            graphics, xAxis, yAxis= self.Results.frame.canvas.last_draw
            self.Results.frame.canvas.Draw(graphics,(1,3.05),(0,1))
    def OnEnableZoom(self, event):
        self.Results.frame.canvas.SetEnableZoom(event.IsChecked())
    def OnEnableGrid(self, event):
        self.Results.frame.canvas.SetEnableGrid(event.IsChecked())
    def OnEnableLegend(self, event):
        self.Results.frame.canvas.SetEnableLegend(event.IsChecked())
    def OnEnablePointLabel(self, event):
        self.Results.frame.canvas.SetEnablePointLabel(event.IsChecked())
    def OnReset(self,event):
        self.Results.frame.canvas.Reset()

    #to get relative exe location in windows
    #from http://aspn.activestate.com/ASPN/Mail/Message/py2exe-users/2264366
    def main_is_frozen(self):
        return (hasattr(sys, "frozen") or # new py2exe
            hasattr(sys, "importers")) # old py2exe
    def get_main_dir(self):
        if self.main_is_frozen():
            return os.path.dirname(sys.executable)
        else:
            return os.path.dirname(sys.argv[0])

class NumCtrl(wx.TextCtrl):
    """A custom text entry field, with predefined size, validator, and tooltips."""
    def __init__(self,parent,id,helpString,**kwargs):
        wx.TextCtrl.__init__(self,parent,id,size=[70,20],validator=DigitsOnly(),**kwargs)
        self.helpString = helpString
        self.Bind(wx.EVT_ENTER_WINDOW,self.ShowHelpString)
        self.Bind(wx.EVT_LEAVE_WINDOW,self.ClearHelpString)
    def ShowHelpString(self,evt):
        app = wx.GetTopLevelParent(self)
        app.SetStatusText(self.helpString)
    def ClearHelpString(self,evt):
        app = wx.GetTopLevelParent(self)
        app.SetStatusText("")

class DigitsOnly(wx.Validator):
    """A validator to prevent entry of text in params panel"""
    def __init__(self):
        wx.Validator.__init__(self)
        self.Bind(wx.EVT_CHAR, self.OnChar)
    def Clone(self):
        return DigitsOnly()

    def Validate(self, win):
        tc = self.GetWindow()
        val = tc.GetValue()
        for x in val:
            if x not in string.digits:
                return False
        return True

    def OnChar(self, event):
        key = event.GetKeyCode()

        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return
        if chr(key) in string.digits:
            event.Skip()
            return
        if chr(key) in '.-e':
            #allow entry of decimals and exponentials
            event.Skip()
            return
        if not wx.Validator_IsSilent():
            wx.Bell()
        return
        # Returning without calling event.Skip eats the event before it
        # gets to the text control
    #end validator class

class IRBMApp(wx.App):
    def OnInit(self):
        #create main frame
        self.MainFrame = AppFrame(None,-1,"ICBM Simulator")
        self.MainFrame.Show(True)
        self.SetTopWindow(self.MainFrame)
        #self.BackgoundColour = 'grey'

        return True

#RUN
app = IRBMApp(0)
app.MainLoop()
