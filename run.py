
_a='ICBM Simulator'
_Z='Results Plot'
_Y='cdfins'
_X='Turn Angle'
_W='Stage %d'
_V='Dry Mass'
_U='Fuel Mass'
_T='deg h'
_S='Drag'
_R='Thrust Vector'
_Q='sec'
_P=False
_O='Thrust'
_N='Minimum Energy'
_M='Unable to solve'
_L='Fuel Fraction'
_K='Height'
_J='Time'
_I='kg'
_H='Gamma'
_G='km'
_F='Burnout Angle'
_E=True
_D='Range'
_C='Velocity'
_B=None
_A='%.2f'
import wx,wx.adv
from wx.lib import plot
import sys,os,string
from math import *
from helper import *
class PP01(wx.Panel):
	def __init__(self,parent,id,presets):
		J='Time to stop missile turnover (sec)';I='to t<';H='Time to start missile turnover (sec)';G='For t>';F='Fin Thickness';E='CR: Fin Root Chord';D='CT: Fin Tip Chord';C='Sweep Angle';B='    m  ';A='Number of Fins';wx.Panel.__init__(self,parent,id);self.presets=presets;self.SetBackgroundColour('WHITE');vbox=wx.BoxSizer(wx.VERTICAL);self.MainSizer=wx.FlexGridSizer(4,1,vgap=15,hgap=10);self.MainSizer.SetMinSize((600,500));self.MiddleSizer=wx.FlexGridSizer(15,6,vgap=5,hgap=0);PresL=[''];PresL.extend(presets.keys());PresL.sort();PresetChoice=wx.Choice(self,-1,choices=PresL);PresetChoice.SetSelection(0);self.Bind(wx.EVT_CHOICE,self.OPC,PresetChoice);text=wx.StaticText(self,-1,'Preset Missiles',(20,100));font=wx.Font(12,wx.ROMAN,wx.NORMAL,wx.BOLD);text.SetFont(font);self.MiddleSizer.Add(text,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(PresetChoice,0,wx.ALIGN_CENTER|wx.BOTTOM,border=5);self.MiddleSizer.Add(wx.StaticText(self,-1,''));FinsNumberText=wx.StaticText(self,-1,A);self.FinsNumberControl=NC01(self,-1,A);self.MiddleSizer.Add(FinsNumberText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.FinsNumberControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,'    '),0,wx.ALIGN_LEFT);PayloadWeightText=wx.StaticText(self,-1,'Payload Weight');self.PayloadWeightControl=NC01(self,-1,'Payload Weight (kg)');UnitKilograms=wx.StaticText(self,-1,'kg        ');self.MiddleSizer.Add(PayloadWeightText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.PayloadWeightControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(UnitKilograms,0,wx.ALIGN_LEFT);FinHeightText=wx.StaticText(self,-1,'S: Fin Span');self.FinHeightControl=NC01(self,-1,'S: Fin Span (m)');self.MiddleSizer.Add(FinHeightText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.FinHeightControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,B),0,wx.ALIGN_LEFT);RVText=wx.StaticText(self,-1,'RV Diameter');self.RVControl=NC01(self,-1,'Diameter of re-entry vehicle (m). Set to zero to ignore drag on re-entry.');self.MiddleSizer.Add(RVText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.RVControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,'m          '),0,wx.ALIGN_LEFT);SweepAngleText=wx.StaticText(self,-1,C);self.SweepAngleControl=NC01(self,-1,C);self.MiddleSizer.Add(SweepAngleText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.SweepAngleControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,'    deg   '),0,wx.ALIGN_LEFT);NozzleText=wx.StaticText(self,-1,'Total Nozzle Area');self.NozzleControl=NC01(self,-1,'Total Area of all nozzles');self.MiddleSizer.Add(NozzleText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.NozzleControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,'m^2           '),0,wx.ALIGN_LEFT);FinTipChordLengthText=wx.StaticText(self,-1,D);self.FinTipChordLengthControl=NC01(self,-1,D);self.MiddleSizer.Add(FinTipChordLengthText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.FinTipChordLengthControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,'    m    '),0,wx.ALIGN_LEFT);LdivDText=wx.StaticText(self,-1,'Nosecone: (Length/Diameter)');self.LdivDControl=NC01(self,-1,'(L/D) [dimensionless]');self.MiddleSizer.Add(LdivDText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.LdivDControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,'           '),0,wx.ALIGN_LEFT);FinRootChordText=wx.StaticText(self,-1,E);self.FinRootChordControl=NC01(self,-1,E);self.MiddleSizer.Add(FinRootChordText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.FinRootChordControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,B),0,wx.ALIGN_LEFT);DiameterText=wx.StaticText(self,-1,'Missile Diameter');self.DiameterControl=NC01(self,-1,'Diameter of missile');self.MiddleSizer.Add(DiameterText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.DiameterControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,'m           '),0,wx.ALIGN_LEFT);hBox=wx.BoxSizer(wx.HORIZONTAL);FinThicknessText=wx.StaticText(self,-1,F);self.FinThicknessControl=NC01(self,-1,F);self.MiddleSizer.Add(FinThicknessText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.FinThicknessControl,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,'    m '),0,wx.ALIGN_LEFT);StageChoiceText=wx.StaticText(self,-1,'Number of Stages');self.StageChoiceBox=wx.Choice(self,-1,choices=['1','2','3','4','5']);self.StageChoiceBox.SetSelection(0);self.Bind(wx.EVT_CHOICE,self.OSC,self.StageChoiceBox);self.MiddleSizer.Add(StageChoiceText,0,wx.ALIGN_LEFT);self.MiddleSizer.Add(self.StageChoiceBox,0,wx.ALIGN_CENTER);self.MiddleSizer.Add(wx.StaticText(self,-1,' '),0);self.TopSizer=wx.FlexGridSizer(10,3,vgap=5,hgap=5);self.TrajectoryChoiceSizer=wx.FlexGridSizer(1,2,vgap=0,hgap=5);self.TrajectoryChoiceSizer.Add(wx.StaticText(self,-1,'Trajectory'),0);self.TrajectoryChoiceBox=wx.Choice(self,-1,choices=[_N,_F]);self.TrajectoryChoiceSizer.Add(self.TrajectoryChoiceBox,0);self.Bind(wx.EVT_CHOICE,self.OTC,self.TrajectoryChoiceBox);self.TopSizer.Add(self.TrajectoryChoiceSizer,0);self.NoseconeChoiceSizer=wx.FlexGridSizer(1,2,vgap=0,hgap=5);self.NoseconeChoiceSizer.Add(wx.StaticText(self,-1,'Nosecone'),0);self.NoseconeChoiceBox=wx.Choice(self,-1,choices=['Conical','V2','elliptical','parabolic','sears-haack','tangent ogive']);self.NoseconeChoiceSizer.Add(self.NoseconeChoiceBox,0);self.Bind(wx.EVT_CHOICE,self.ONC,self.NoseconeChoiceBox);self.TopSizer.Add(self.NoseconeChoiceSizer,0);self.EstRangeSizer=wx.FlexGridSizer(1,3,vgap=0,hgap=5);self.EstRangeSizer.Add(wx.StaticText(self,-1,'Est. Range'),0);self.EstRangeControl=NC01(self,-1,'Estimated range (km). Forces missile to MET after stage 1 burnout.');self.EstRangeSizer.Add(self.EstRangeControl,0);self.EstRangeSizer.Add(wx.StaticText(self,-1,_G),0);self.TopSizer.Add(self.EstRangeSizer,0);self.EtaSizer=wx.FlexGridSizer(2,4,hgap=5,vgap=10);self.EtaSizer.Add(wx.StaticText(self,-1,G),0);self.EtaTStartTurn=NC01(self,-1,H);self.EtaSizer.Add(self.EtaTStartTurn,0);self.EtaSizer.Add(wx.StaticText(self,-1,I),0);self.EtaTEndTurn=NC01(self,-1,J);self.EtaSizer.Add(self.EtaTEndTurn,0);self.EtaSizer.Add(wx.StaticText(self,-1,'Eta'),0);self.EtaTurnAngle=NC01(self,-1,'Angle between thrust and velocity vectors for above timespan (deg)');self.EtaSizer.Add(self.EtaTurnAngle,0);self.TopSizer.Add(self.EtaSizer,0);self.BurnoutAngleSizer=wx.FlexGridSizer(0,0,vgap=0,hgap=5);self.BurnoutAngleSizer.Add(wx.StaticText(self,-1,_F),0);self.BurnoutAngleCtrl=NC01(self,-1,'Angle of missile on stage 1 burnout');self.BurnoutAngleSizer.Add(self.BurnoutAngleCtrl,0);self.BurnoutAngleSizer.Add(wx.StaticText(self,-1,_T),0);self.TopSizer.Add(self.BurnoutAngleSizer,0);self.TurnAngleSizer=wx.FlexGridSizer(2,4,hgap=5,vgap=10);self.TurnAngleSizer.Add(wx.StaticText(self,-1,G),0);self.TurnTimeStart=NC01(self,-1,H);self.TurnAngleSizer.Add(self.TurnTimeStart,0);self.TurnAngleSizer.Add(wx.StaticText(self,-1,I),0);self.TurnTimeEnd=NC01(self,-1,J);self.TurnAngleSizer.Add(self.TurnTimeEnd);self.TurnAngleSizer.Add(wx.StaticText(self,-1,_H),0);self.TurnAngleStart=NC01(self,-1,'Turnover angle at start (deg from vertical)');self.TurnAngleSizer.Add(self.TurnAngleStart);self.TurnAngleSizer.Add(wx.StaticText(self,-1,_H),0);self.TurnAngleEnd=NC01(self,-1,'Turnover angle at end (deg from vertical)');self.TurnAngleSizer.Add(self.TurnAngleEnd);self.TopSizer.Add(self.TurnAngleSizer,0);self.TrajectoryChoiceBox.SetSelection(0);self.TopSizer.Hide(self.BurnoutAngleSizer);self.TopSizer.Hide(self.EtaSizer);self.TopSizer.Hide(self.TurnAngleSizer);self.TopSizer.Show(self.EstRangeSizer);self.Layout();self.NoseconeChoiceBox.SetSelection(0);self.Layout();self.StageSizer=wx.GridBagSizer(5,6);self.StageSizer.Add(wx.StaticText(self,-1,_U),(1,0));self.StageSizer.Add(wx.StaticText(self,-1,_V),(2,0));self.StageSizer.Add(wx.StaticText(self,-1,'Isp'),(3,0));self.StageSizer.Add(wx.StaticText(self,-1,_O),(4,0));self.StageNumberText=[''];self.StageFuelMassCtrl=[''];self.StageDryMassCtrl=[''];self.StageIspCtrl=[''];self.StageThrustCtrl=['']
		for i in range(1,6):
			self.StageNumberText.append(wx.StaticText(self,-1,_W%i));self.StageSizer.Add(self.StageNumberText[i],(0,i),flag=wx.ALIGN_CENTER|wx.ALL,border=10);self.StageFuelMassCtrl.append(NC01(self,-1,'Stage %i fuel mass (kg)'%i));self.StageSizer.Add(self.StageFuelMassCtrl[i],(1,i));self.StageDryMassCtrl.append(NC01(self,-1,'Stage %i dry mass (kg)'%i));self.StageSizer.Add(self.StageDryMassCtrl[i],(2,i))
			if i==1:isptype='sea level'
			else:isptype='vacuum'
			self.StageIspCtrl.append(NC01(self,-1,'Stage %i specific impulse at %s (sec)'%(i,isptype)));self.StageSizer.Add(self.StageIspCtrl[i],(3,i));self.StageThrustCtrl.append(NC01(self,-1,'Stage %i thrust (kg force)'%i));self.StageSizer.Add(self.StageThrustCtrl[i],(4,i))
		for i in range(2,6):self.StageSizer.Hide(self.StageNumberText[i]);self.StageSizer.Hide(self.StageFuelMassCtrl[i]);self.StageSizer.Hide(self.StageDryMassCtrl[i]);self.StageSizer.Hide(self.StageIspCtrl[i]);self.StageSizer.Hide(self.StageThrustCtrl[i])
		self.StageSizer.Add(wx.StaticText(self,-1,_I),(1,6),flag=wx.ALIGN_LEFT);self.StageSizer.Add(wx.StaticText(self,-1,_I),(2,6),flag=wx.ALIGN_LEFT);self.StageSizer.Add(wx.StaticText(self,-1,_Q),(3,6),flag=wx.ALIGN_LEFT);self.StageSizer.Add(wx.StaticText(self,-1,'kg f'),(4,6),flag=wx.ALIGN_LEFT);RunButton=wx.Button(self,-1,'Run Simulation');self.Bind(wx.EVT_BUTTON,self.ORN,RunButton);RunButton.SetDefault();RunButton.SetSize(RunButton.GetBestSize());self.MainSizer.Add(self.MiddleSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT|wx.TOP,10);self.MainSizer.Add(self.TopSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,10);self.MainSizer.Add(self.StageSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,10);self.MainSizer.Add(RunButton,0,wx.ALIGN_LEFT|wx.EXPAND|wx.ALL,50);self.MainSizer.SetSizeHints(self);self.SetSizer(self.MainSizer);self.SetAutoLayout(1);self.Layout()
	def OFC(self,event,numfins_override=_B):
		if numfins_override:numfins=numfins_override
		else:
			numfins=int(event.GetString())
			if numfins!=0:0
		self.Layout()
	def OSC(self,event,numstage_override=_B):
		if numstage_override:numstages=numstage_override
		else:numstages=int(event.GetString())
		for i in range(1,numstages+1):self.StageSizer.Show(self.StageNumberText[i]);self.StageSizer.Show(self.StageFuelMassCtrl[i]);self.StageSizer.Show(self.StageDryMassCtrl[i]);self.StageSizer.Show(self.StageIspCtrl[i]);self.StageSizer.Show(self.StageThrustCtrl[i])
		for i in range(numstages+1,6):self.StageSizer.Hide(self.StageNumberText[i]);self.StageFuelMassCtrl[i].SetValue('');self.StageSizer.Hide(self.StageFuelMassCtrl[i]);self.StageDryMassCtrl[i].SetValue('');self.StageSizer.Hide(self.StageDryMassCtrl[i]);self.StageIspCtrl[i].SetValue('');self.StageSizer.Hide(self.StageIspCtrl[i]);self.StageThrustCtrl[i].SetValue('');self.StageSizer.Hide(self.StageThrustCtrl[i])
		self.Layout()
	def ONC(self,event):choice=event.GetString()
	def OTC(self,event):
		choice=event.GetString()
		if choice==_N:self.TopSizer.Show(self.EstRangeSizer);self.TopSizer.Hide(self.EtaSizer);self.TopSizer.Hide(self.BurnoutAngleSizer);self.TopSizer.Hide(self.TurnAngleSizer)
		if choice==_R:self.TopSizer.Show(self.EtaSizer);self.TopSizer.Hide(self.EstRangeSizer);self.TopSizer.Hide(self.BurnoutAngleSizer);self.TopSizer.Hide(self.TurnAngleSizer)
		if choice==_F:self.TopSizer.Show(self.BurnoutAngleSizer);self.TopSizer.Hide(self.EtaSizer);self.TopSizer.Hide(self.EstRangeSizer);self.TopSizer.Hide(self.TurnAngleSizer)
		if choice==_X:self.TopSizer.Show(self.TurnAngleSizer);self.TopSizer.Hide(self.EtaSizer);self.TopSizer.Hide(self.EstRangeSizer);self.TopSizer.Hide(self.BurnoutAngleSizer)
		self.Layout()
	def OPC(self,event):
		try:
			preset_data=self.presets[event.GetString()];numstages=preset_data['numstages'];self.PayloadWeightControl.SetValue(str(preset_data['payload']));self.RVControl.SetValue(str(preset_data['rvdiam']));self.NozzleControl.SetValue(str(preset_data['nozzlearea']));self.LdivDControl.SetValue(str(preset_data['LdivD']));self.EstRangeControl.SetValue(str(preset_data['estrange']));self.StageChoiceBox.SetSelection(numstages-1);self.DiameterControl.SetValue(str(preset_data['missilediam']))
			for i in range(1,numstages+1):self.StageFuelMassCtrl[i].SetValue(str(preset_data['fuelmass'][i]));self.StageDryMassCtrl[i].SetValue(str(preset_data['drymass'][i]));self.StageIspCtrl[i].SetValue(str(preset_data['Isp0'][i]));self.StageThrustCtrl[i].SetValue(str(preset_data['thrust0'][i]))
		except KeyError:pass
		try:self.OSC(_B,numstage_override=numstages)
		except UnboundLocalError:pass
	def ORN(self,event):
		sim=zS(self)
		try:
			sim.FinHeight=float(self.FinHeightControl.GetValue());sim.SweepAngle=float(self.SweepAngleControl.GetValue());sim.FinTipChordLength=float(self.FinTipChordLengthControl.GetValue());sim.FinRootChord=float(self.FinRootChordControl.GetValue());sim.FinThickness=float(self.FinThicknessControl.GetValue());sim.FinsNumber=float(self.FinsNumberControl.GetValue());sim.payload=float(self.PayloadWeightControl.GetValue());sim.rvdiam=float(self.RVControl.GetValue());sim.nozzlearea=float(self.NozzleControl.GetValue());sim.LdivD=float(self.LdivDControl.GetValue());sim.missilediam=float(self.DiameterControl.GetValue());sim.Nosecone=self.NoseconeChoiceBox.GetStringSelection();sim.trajectory=self.TrajectoryChoiceBox.GetStringSelection()
			if sim.trajectory==_N:sim.est_range=float(self.EstRangeControl.GetValue())*1000
			if sim.trajectory==_R:sim.TStartTurn=float(self.EtaTStartTurn.GetValue());sim.TEndTurn=float(self.EtaTEndTurn.GetValue());sim.TurnAngle=float(self.EtaTurnAngle.GetValue())
			if sim.trajectory==_F:sim.BA01=float(self.BurnoutAngleCtrl.GetValue())
			if sim.trajectory==_X:sim.TurnTimeStart=float(self.TurnTimeStart.GetValue());sim.TurnTimeEnd=float(self.TurnTimeEnd.GetValue());sim.TurnAngleStart=float(self.TurnAngleStart.GetValue());sim.TurnAngleEnd=float(self.TurnAngleEnd.GetValue())
			sim.numstages=int(self.StageChoiceBox.GetSelection()+1)
			for i in range(1,sim.numstages+1):sim.fuelmass.append(float(self.StageFuelMassCtrl[i].GetValue()));sim.m0.append(float(self.StageDryMassCtrl[i].GetValue())+sim.fuelmass[i]);sim.fuelfraction.append(float(sim.fuelmass[i]/sim.m0[i]));sim.Isp0.append(float(self.StageIspCtrl[i].GetValue()));sim.thrust0.append(float(self.StageThrustCtrl[i].GetValue())*9.81);sim.dMdt.append(float(sim.thrust0[i]/(sim.Isp0[i]*9.81)))
			self.sim=sim;app=wx.GetTopLevelParent(self);trajectory=self.TrajectoryChoiceBox.GetStringSelection();app.Results.data=sim.integrate(trajectory);Nosecone=self.NoseconeChoiceBox.GetStringSelection();app.Results.data=sim.integrate(Nosecone);app.nb.AdvanceSelection(forward=_E);other=app.Results
			for i in range(1,sim.numstages+1):other.StageResultSizer.Show(other.StageNumberText[i]);other.StageResultSizer.Show(other.StageVelocityResult[i]);other.StageResultSizer.Show(other.StageAngleResult[i]);other.StageResultSizer.Show(other.StageHeightResult[i]);other.StageResultSizer.Show(other.StageRangeResult[i]);other.StageResultSizer.Show(other.StageTimeResult[i]);other.StageResultSizer.Show(other.StageMachResult[i])
			app.Results.Layout()
		except ValueError:dlg=wx.MessageDialog(self,'Please make sure all fields are filled in.','Entry error',wx.OK|wx.ICON_INFORMATION);dlg.ShowModal();dlg.Destroy()
class PF01(wx.Frame):
	def __init__(self,parent,id,title):wx.Frame.__init__(self,parent,id,title,(550,30),(600,400));self.canvas=plot.PlotCanvas(self)
class RP01(wx.Panel):
	def __init__(self,parent,id):
		A='km/s';wx.Panel.__init__(self,parent,id);self.SetBackgroundColour('white');self.data={_J:[0],_K:[0],_C:[0],_O:[0],_S:[0],'CD':[0],_Y:[0],_H:[0],_D:[0]};app=wx.GetTopLevelParent(self);self.frame=PF01(_B,-1,_Z);MainResultsSizer=wx.FlexGridSizer(5,0,vgap=12,hgap=0);FinalResultSizer=wx.FlexGridSizer(5,3,vgap=10,hgap=10);FinalResultSizer.Add(wx.StaticText(self,-1,'Apogee'),0,wx.ALIGN_LEFT);self.ApogeeResult=NC01(self,-1,'Largest height attained in flight (km)',style=wx.TE_READONLY);FinalResultSizer.Add(self.ApogeeResult,0,wx.ALIGN_CENTER);FinalResultSizer.Add(wx.StaticText(self,-1,_G),0,wx.ALIGN_RIGHT);FinalResultSizer.Add(wx.StaticText(self,-1,'Apogee Velocity'),0,wx.ALIGN_LEFT);self.ApogeeVelocityResult=NC01(self,-1,'Velocity at apogee (km/sec)',style=wx.TE_READONLY);FinalResultSizer.Add(self.ApogeeVelocityResult,0,wx.ALIGN_CENTER);FinalResultSizer.Add(wx.StaticText(self,-1,A),0,wx.ALIGN_RIGHT);FinalResultSizer.Add(wx.StaticText(self,-1,_D),0,wx.ALIGN_LEFT);self.RangeResult=NC01(self,-1,'Distance along earth surface to impact point (km)',style=wx.TE_READONLY);FinalResultSizer.Add(self.RangeResult,0,wx.ALIGN_CENTER);FinalResultSizer.Add(wx.StaticText(self,-1,_G),0,wx.ALIGN_RIGHT);FinalResultSizer.Add(wx.StaticText(self,-1,'Flight Time'),0,wx.ALIGN_LEFT);self.FlightTimeResult=NC01(self,-1,'Time from liftoff to impact (sec)',style=wx.TE_READONLY);FinalResultSizer.Add(self.FlightTimeResult,0,wx.ALIGN_CENTER);FinalResultSizer.Add(wx.StaticText(self,-1,_Q),0,wx.ALIGN_RIGHT);self.StageResultSizer=wx.GridBagSizer(5,7);self.StageResultSizer.Add(wx.StaticText(self,-1,_C),(1,0));self.StageResultSizer.Add(wx.StaticText(self,-1,'Angle'),(2,0));self.StageResultSizer.Add(wx.StaticText(self,-1,_K),(3,0));self.StageResultSizer.Add(wx.StaticText(self,-1,_D),(4,0));self.StageResultSizer.Add(wx.StaticText(self,-1,_J),(5,0));self.StageNumberText=[''];self.StageVelocityResult=[''];self.StageAngleResult=[''];self.StageHeightResult=[''];self.StageRangeResult=[''];self.StageTimeResult=[''];self.StageMachResult=['']
		for i in range(1,6):self.StageNumberText.append(wx.StaticText(self,-1,_W%i));self.StageResultSizer.Add(self.StageNumberText[i],(0,i),flag=wx.ALIGN_CENTER|wx.ALL,border=10);self.StageVelocityResult.append(NC01(self,-1,'Velocity at stage %i burnout (km/sec)'%i,style=wx.TE_READONLY));self.StageResultSizer.Add(self.StageVelocityResult[i],(1,i));self.StageAngleResult.append(NC01(self,-1,'Angle at stage %i burnout (degrees from horizontal)'%i,style=wx.TE_READONLY));self.StageResultSizer.Add(self.StageAngleResult[i],(2,i));self.StageHeightResult.append(NC01(self,-1,'Height at stage %i burnout (km)'%i,style=wx.TE_READONLY));self.StageResultSizer.Add(self.StageHeightResult[i],(3,i));self.StageRangeResult.append(NC01(self,-1,'Range at stage %i burnout (km)'%i,style=wx.TE_READONLY));self.StageResultSizer.Add(self.StageRangeResult[i],(4,i));self.StageTimeResult.append(NC01(self,-1,'Time of stage %i burnout (sec)'%i,style=wx.TE_READONLY));self.StageResultSizer.Add(self.StageTimeResult[i],(5,i))
		self.StageResultSizer.Add(wx.StaticText(self,-1,A),(1,6),flag=wx.ALIGN_LEFT);self.StageResultSizer.Add(wx.StaticText(self,-1,_T),(2,6),flag=wx.ALIGN_LEFT);self.StageResultSizer.Add(wx.StaticText(self,-1,_G),(3,6),flag=wx.ALIGN_LEFT);self.StageResultSizer.Add(wx.StaticText(self,-1,_G),(4,6),flag=wx.ALIGN_LEFT);self.StageResultSizer.Add(wx.StaticText(self,-1,_Q),(5,6),flag=wx.ALIGN_LEFT);MainResultsSizer.Add(FinalResultSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT|wx.TOP,10);MainResultsSizer.Add(self.StageResultSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,10);self.SetSizer(MainResultsSizer);self.SetAutoLayout(1);self.Layout()
	def OPT(self,event):
		D=' (N)';C=' (km)';B='red';A='Mach';plot=[];x=self.XRadioBox.GetStringSelection();y=self.YRadioBox.GetStringSelection()
		try:self.frame.Show(_P)
		except wx._core.PyDeadObjectError:self.frame=PF01(_B,-1,_Z)
		self.frame.canvas.Reset();self.frame.Show(_E);title='%s vs %s'%(y,x);app=wx.GetTopLevelParent(self);sim=app.pms.sim
		for i in range(1,sim.numstages+1):
			if x==_J:x_stage=float(self.StageTimeResult[i].GetValue())
			if x==_D:x_stage=float(self.StageRangeResult[i].GetValue())
			if x==_C:x_stage=float(self.StageVelocityResult[i].GetValue())
			if x==A:x_stage=float(self.StageMachResult[i].GetValue())
			plot.append(PolyMarker([(x_stage,0)],legend='Stage %d Burnout'%i,marker='cross',colour=B,size=1))
		if x==_D:x_data=[elem/1000.0 for elem in self.data[x]];x=x+C
		elif x==_J:x_data=self.data[x];x=x+' (sec)'
		elif x==_C:x_data=self.data[x]
		if y==_S:y_data=self.data[y];y=y+D
		elif y==_H:y_data=[elem*(180.0/pi)for elem in self.data[y]];y=y+' (deg h)'
		elif y==_K:h=self.data[y];y_data=[elem/1000.0 for elem in self.data[y]];y=y+C
		elif y==_C:y_data=self.data[y];y=y+' (m/s)'
		elif y==_O:y_data=self.data[y];y=y+D
		elif x==A:
			h=self.data[_K]
			if h<=11000.0:t=15.04-0.00649*h
			elif h>11000.0 and h<=25000.0:t=-56.46
			elif h>25000.0:t=131.21+0.00299*h
			t=t+273.15;a=sqrt(1.4*287*t);global x_data;x_data=self.data[_C]/a
		else:y_data=self.data[y]
		line=numpy.array(zip(x_data,y_data));plot.append(PolyLine(line,legend=x,colour=B));self.frame.canvas.Draw(PlotGraphics(plot,title,x,y))
class AP01(wx.Panel):
	def __init__(self,parent,id):wx.Panel.__init__(self,parent,id);MainSizer=wx.FlexGridSizer(0,1,vgap=25,hgap=0);TopSizer=wx.FlexGridSizer(1,2,vgap=0,hgap=10);VariableSizer=wx.FlexGridSizer(1,2,vgap=0,hgap=10);VariableSizer.Add(wx.StaticText(self,-1,'Solve for'),0,wx.ALIGN_LEFT);self.VariableChoice=wx.Choice(self,-1,choices=[_L]);VariableSizer.Add(self.VariableChoice,0,wx.ALIGN_LEFT);self.Bind(wx.EVT_CHOICE,self.OCV,self.VariableChoice);StageNumSizer=wx.FlexGridSizer(1,2,vgap=0,hgap=10);StageNumSizer.Add(wx.StaticText(self,-1,'Stage'),0);self.StageChoiceBox=wx.Choice(self,-1,choices=['1','2','3','4','5']);StageNumSizer.Add(self.StageChoiceBox,0,wx.ALIGN_LEFT);self.StageChoiceBox.SetSelection(0);TopSizer.Add(VariableSizer,0);TopSizer.Add(StageNumSizer,0);ConstraintSizer=wx.FlexGridSizer(0,3,hgap=10,vgap=10);ConstraintSizer.Add(wx.StaticText(self,-1,'Stage Mass'),0,wx.ALIGN_LEFT);self.StageMassCtrl=NC01(self,-1,'Fuel Mass + Dry Mass (kg). Does not include payload.');ConstraintSizer.Add(self.StageMassCtrl);ConstraintSizer.Add(wx.StaticText(self,-1,_I),0,wx.ALIGN_LEFT);ConstraintSizer.Add(wx.StaticText(self,-1,_L),0,wx.ALIGN_LEFT);self.FuelFractionCtrl=NC01(self,-1,'Fuel Mass / Stage Mass');ConstraintSizer.Add(self.FuelFractionCtrl);ConstraintSizer.Add(wx.StaticText(self,-1,'%'),0,wx.ALIGN_LEFT);ConstraintSizer.Add(wx.StaticText(self,-1,_U),0,wx.ALIGN_LEFT);self.FuelMassCtrl=NC01(self,-1,'Fuel Mass (kg)',style=wx.TE_READONLY);ConstraintSizer.Add(self.FuelMassCtrl);ConstraintSizer.Add(wx.StaticText(self,-1,_I),0,wx.ALIGN_LEFT);ConstraintSizer.Add(wx.StaticText(self,-1,_V),0,wx.ALIGN_LEFT);self.DryMassCtrl=NC01(self,-1,'Dry Mass (kg)',style=wx.TE_READONLY);ConstraintSizer.Add(self.DryMassCtrl);ConstraintSizer.Add(wx.StaticText(self,-1,_I),0,wx.ALIGN_LEFT);MiddleSizer=wx.FlexGridSizer(2,2,hgap=25,vgap=10);MiddleSizer.Add(wx.StaticText(self,-1,'Estimated Range'),0);self.AnsGuessControl=NC01(self,-1,'Your guess for the missile range');MiddleSizer.Add(self.AnsGuessControl,0);SolveButton=wx.Button(self,-1,'Solve');self.Bind(wx.EVT_BUTTON,self.OS,SolveButton);SolveButton.SetSize(SolveButton.GetBestSize());AnswerSizer=wx.FlexGridSizer(2,2,hgap=5,vgap=5);AnswerSizer.Add(wx.StaticText(self,-1,'Variable'),0);self.AnswerControl=NC01(self,-1,'First found value of the variable that gives the desired range',style=wx.TE_READONLY);AnswerSizer.Add(self.AnswerControl,0);AnswerSizer.Add(wx.StaticText(self,-1,_D),0);self.RangeControl=NC01(self,-1,'Range with above variable',style=wx.TE_READONLY);AnswerSizer.Add(self.RangeControl,0);self.max_runs=25;self.Gauge=wx.Gauge(self,-1,self.max_runs,size=[250,25],style=wx.GA_HORIZONTAL);MainSizer.Add(TopSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT|wx.TOP,10);MainSizer.Add(ConstraintSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,10);MainSizer.Add(MiddleSizer,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT,10);MainSizer.Add(SolveButton,0,wx.ALIGN_CENTER_HORIZONTAL);MainSizer.Add(self.Gauge,0,wx.ALIGN_CENTER_HORIZONTAL);MainSizer.Add(AnswerSizer,0,wx.ALIGN_CENTER_HORIZONTAL|wx.TOP,-20);self.SetSizer(MainSizer);self.SetAutoLayout(1);self.Layout()
	def OCV(self,event):
		app=wx.GetTopLevelParent(self);nstage=int(self.StageChoiceBox.GetSelection()+1);self.var_string=self.VariableChoice.GetStringSelection()
		if self.var_string==_L:self.var_control=self.FuelFractionCtrl;m_prop=float(app.pms.StageFuelMassCtrl[nstage].GetValue());m_struct=float(app.pms.StageDryMassCtrl[nstage].GetValue());self.StageMassCtrl.SetValue(_A%(m_prop+m_struct));self.FuelFractionCtrl.SetValue(_A%(m_prop/(m_struct+m_prop)*100));self.CCS()
		self.AnsGuessControl.SetValue(app.pms.EstRangeControl.GetValue())
	def CCS(self):
		app=wx.GetTopLevelParent(self);nstage=int(self.StageChoiceBox.GetSelection()+1);self.var_string=self.VariableChoice.GetStringSelection()
		if self.var_string==_L:
			m0=float(self.StageMassCtrl.GetValue());fuelfraction=float(self.FuelFractionCtrl.GetValue())/100
			if fuelfraction>1:fuelfraction=0.99*100;self.FuelFractionCtrl.SetValue(_A%fuelfraction)
			if fuelfraction<0:fuelfraction=0.01*100;self.FuelFractionCtrl.SetValue(_A%fuelfraction)
			m_prop=fuelfraction*m0;m_struct=m0-fuelfraction*m0;self.FuelMassCtrl.SetValue(_A%m_prop);self.DryMassCtrl.SetValue(_A%m_struct);app.pms.StageFuelMassCtrl[nstage].SetValue(_A%m_prop);app.pms.StageDryMassCtrl[nstage].SetValue(_A%m_struct)
		else:0
	def OS(self,event):
		if self.var_string=='':dlg=wx.MessageDialog(self,'Solve for.',_M,wx.OK|wx.ICON_INFORMATION);dlg.ShowModal();dlg.Destroy();return _P
		try:ans_est=float(self.AnsGuessControl.GetValue());var_est=float(self.var_control.GetValue())
		except ValueError:dlg=wx.MessageDialog(self,'Please fill in all fields.',_M,wx.OK|wx.ICON_INFORMATION);dlg.ShowModal();dlg.Destroy();return _P
		oldx=var_est*0.99;self.var_control.SetValue(_A%oldx);oldf=self.RS()-ans_est;x=var_est;self.var_control.SetValue(_A%var_est);f=self.RS()-ans_est;run=0;tolerance=0.01
		if abs(f)>abs(oldf):oldx,x=x,oldx;oldf,f=f,oldf
		while _E:
			try:
				dx=f*(x-oldx)/(f-oldf)
				if abs(dx)<tolerance:break
			except ZeroDivisionError:break
			oldx,x=x,x-dx;self.var_control.SetValue(_A%x);oldf,f=f,self.RS()-ans_est;run+=1;self.Gauge.SetValue(run);self.AnswerControl.SetValue(_A%x);self.RangeControl.SetValue(_A%(f+ans_est));wx.Yield()
			if run>self.max_runs:dlg=wx.MessageDialog(self,_M,wx.OK|wx.ICON_INFORMATION);dlg.ShowModal();dlg.Destroy();return
		self.var_control.SetValue(_A%oldx);self.AnswerControl.SetValue(_A%oldx);self.Gauge.SetValue(self.max_runs)
		if self.var_string==_L:
			answer=float(self.AnswerControl.GetValue())
			if answer>100 or answer<0:dlg=wx.MessageDialog(self,_M,wx.OK|wx.ICON_INFORMATION);dlg.ShowModal();dlg.Destroy()
	def RS(self):
		self.CCS();sim=zS(self);app=wx.GetTopLevelParent(self)
		try:
			sim.payload=float(app.pms.PayloadWeightControl.GetValue());sim.rvdiam=float(app.pms.RVControl.GetValue());sim.LdivD=float(app.pms.LdivDControl.GetValue());sim.missilediam=float(app.pms.DiameterControl.GetValue());sim.numstages=int(app.pms.StageChoiceBox.GetSelection()+1);sim.numfins=int(app.pms.FinsChoiceBox.GetSelection()+1)
			for i in range(1,sim.numstages+1):sim.fuelmass.append(float(app.pms.StageFuelMassCtrl[i].GetValue()));sim.m0.append(float(app.pms.StageDryMassCtrl[i].GetValue())+sim.fuelmass[i]);sim.fuelfraction.append(float(sim.fuelmass[i]/sim.m0[i]));sim.Isp0.append(float(app.pms.StageIspCtrl[i].GetValue()));sim.thrust0.append(float(app.pms.StageThrustCtrl[i].GetValue())*9.81);sim.dMdt.append(float(sim.thrust0[i]/(sim.Isp0[i]*9.81)))
			trajectory=app.pms.TrajectoryChoiceBox.GetStringSelection();Nosecone=app.pms.NoseconeChoiceBox.GetStringSelection()
			if trajectory==_N:sim.est_range=float(app.pms.EstRangeControl.GetValue())*1000
			if trajectory==_R:sim.TStartTurn=float(self.EtaTStartTurn.GetValue());sim.TEndTurn=float(self.EtaTEndTurn.GetValue());sim.TurnAngle=float(self.EtaTurnAngle.GetValue())
			if trajectory==_F:sim.BA01=float(self.BurnoutAngleCtrl.GetValue())
		except ValueError:dlg=wx.MessageDialog(self,'Please fill in all fields in Parameters panel.',_M,wx.OK|wx.ICON_INFORMATION);dlg.ShowModal();dlg.Destroy()
		data=sim.integrate(trajectory);answer=float(app.Results.RangeResult.GetValue());del sim;del data;return answer
class AFr01(wx.Frame):
	def __init__(self,parent,id,title):
		B='phoenix';A='&Help';wx.Frame.__init__(self,parent,id,title,(-1,-1),wx.Size(800,650));font=wx.Font(8,wx.FONTFAMILY_SWISS,wx.NORMAL,wx.BOLD);wx.Frame.SetFont(self,font);self.MenuBar=wx.MenuBar();FileMenu=wx.Menu();FileMenu.Append(205,'Q&uit','Quit this Application');wx.EVT_MENU(self,205,self.OnFileExit)
		if B in wx.PlatformInfo:wx.PyApp.SetMacExitMenuItemId(wx.ID_EXIT)
		else:wx.App_SetMacExitMenuItemId(205)
		self.MenuBar.Append(FileMenu,'&File');HelpMenu=wx.Menu();HelpMenu.Append(300,'&About','About...');wx.EVT_MENU(self,300,self.OnAbout)
		if wx.Platform=='__WXMAC__':
			if B in wx.PlatformInfo:wx.PyApp.SetMacAboutMenuItemId(wx.ID_ABOUT);wx.PyApp.SetMacHelpMenuTitleName(A)
			else:wx.App.SetMacAboutMenuItemId(300);wx.App_SetMacHelpMenuTitleName(A)
		else:self.MenuBar.Append(HelpMenu,A)
		self.SetMenuBar(self.MenuBar);self.CreateStatusBar(1);self.SetStatusText('')
		try:preset_path=os.path.join(self.get_main_dir(),'presets.txt');presets_file=open(preset_path,'r');presets=eval(presets_file.read())
		except SyntaxError:dlg=wx.MessageDialog(self,'Eror',wx.OK|wx.ICON_INFORMATION);dlg.ShowModal();dlg.Destroy();presets={'Error reading presets.txt':{}}
		self.nb=wx.Notebook(self,-1);self.pms=PP01(self.nb,-1,presets);self.Results=RP01(self.nb,-1);self.nb.AddPage(self.pms,'Settings');self.nb.AddPage(self.Results,'Results')
	def OnFileExit(self,event):sys.exit()
	def OnAbout(self,event):info=wx.adv.AboutDialogInfo();info.SetName(_a);info.SetDescription('');info.SetLicence(__doc__);wx.adv.AboutBox(info)
	def main_is_frozen(self):return hasattr(sys,'frozen')or hasattr(sys,'importers')
	def get_main_dir(self):
		if self.main_is_frozen():return os.path.dirname(sys.executable)
		else:return os.path.dirname(sys.argv[0])
class NC01(wx.TextCtrl):
	def __init__(self,parent,id,helpString,**kwargs):wx.TextCtrl.__init__(self,parent,id,size=[70,20],validator=DO01(),**kwargs);self.helpString=helpString;self.Bind(wx.EVT_ENTER_WINDOW,self.shs01);self.Bind(wx.EVT_LEAVE_WINDOW,self.chs01)
	def shs01(self,evt):app=wx.GetTopLevelParent(self);app.SetStatusText(self.helpString)
	def chs01(self,evt):app=wx.GetTopLevelParent(self);app.SetStatusText('')
class DO01(wx.Validator):
	def __init__(self):wx.Validator.__init__(self);self.Bind(wx.EVT_CHAR,self.OnChar)
	def c01(self):return DO01()
	def v01(self,win):
		tc=self.GetWindow();val=tc.GetValue()
		for x in val:
			if x not in string.digits:return _P
		return _E
	def OnChar(self,event):
		key=event.GetKeyCode()
		if key<wx.WXK_SPACE or key==wx.WXK_DELETE or key>255:event.Skip();return
		if chr(key)in string.digits:event.Skip();return
		if chr(key)in'.-e':event.Skip();return
		if not wx.Validator_IsSilent():wx.Bell()
		return
class ICBMsim(wx.App):
	def OnInit(self):self.MainFrame=AFr01(_B,-1,_a);self.MainFrame.Show(_E);self.SetTopWindow(self.MainFrame);return _E
app=ICBMsim(0)
app.MainLoop()
