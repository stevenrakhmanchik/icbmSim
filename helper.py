from math import*
object=object; zu=NameError; zn=range; gz=True; gV=False; gQ=float; gC=None; gJ=int
gE=raw_input; gO=open; gj=str; gl=zip; go=len
global i; global s; global BA01; global Y; global P
class zS(object):
	def __setattr__(z,name,value):
		object.__setattr__(z,name,value)
	def __init__(z,parent):
	  z.parent=parent
	  z.burntime=['']; z.thrust0=['']; z.Isp0=['']; z.m0=['']; z.fuelfraction=['']; z.fuelmass=['']; z.dMdt=['']; z.FinHeight=['']; z.SweepAngle=['']; z.FinTipChordLength=['']; z.FinRootChord=['']; z.FinThickness=['']; z.data={'Time':[0],'Height':[0],'Mass':[0],'Velocity':[0],'Thrust':[0],'Drag':[0],'CD':[0],'Gamma':[pi/2],'Range':[0]}; z.Nosecone=['']
	def zB(z,trajectory):
	  	t=0.0; v=0; h=0.001; g=0; V=0.0; Q=0.0; C=z.zk(90)
		try:
		  J=wx.GetTopLevelParent(z.parent)
		except zu:
		  pass
		z.trajectory=trajectory
		E=20000; O=1; j=20000; l=.1; o=.01; h=0.0; r=0.0; W=r+1; p=0.0; f=0.0; H=0.0
		cd=0.0; I=6370000; g0=9.8066
		for i in zn(1,z.numstages+1):
		  h+=z.m0[i]
		  z.burntime.append(z.Isp0[i]*9.81*z.fuelmass[i]/z.thrust0[i])
		  r+=z.burntime[i]
		h+=z.payload; fh=z.FinHeight; sa=z.SweepAngle; d=z.FinTipChordLength; G=z.FinRootChord; R=z.FinThickness; A=z.FinsNumber
		global fh,sa,d,G,R,A
		t=(z.missilediam/2)**2*pi; K=z.rvdiam/2**2*pi
		if z.numstages==1:
		  i=z.Isp0[1]*9.81*log(h/(h-z.fuelmass[1]))
		if z.numstages==2:
		  i=z.Isp0[1]*9.81*log(h/(h-z.fuelmass[1])); i=i+z.Isp0[2]*9.81*log((h-z.m0[1])/(h-z.m0[1]-z.fuelmass[2]))
		if z.numstages==3:
		  i=0.; i=z.Isp0[1]*9.81*log(h/(h-z.fuelmass[1]))
		  i=i+z.Isp0[2]*9.81*log((h-z.m0[1])/(h-z.m0[1]-z.fuelmass[2])); i=i+z.Isp0[3]*9.81*log((h-z.m0[1]-z.m0[2])/(h-z.m0[1]-z.m0[2]-z.fuelmass[3]))
		if z.numstages==4:
		  i=0.; i=z.Isp0[1]*9.81*log(h/(h-z.fuelmass[1])); i=i+z.Isp0[2]*9.81*log((h-z.m0[1])/(h-z.m0[1]-z.fuelmass[2]))
		  i=i+z.Isp0[3]*9.81*log((h-z.m0[1]-z.m0[2])/(h-z.m0[1]-z.m0[2]-z.fuelmass[3]));i=i+z.Isp0[4]*9.81*log((h-z.m0[1]-z.m0[2]-z.m0[3])/(h-z.m0[1]-z.m0[2]-z.m0[3]-z.fuelmass[4]))
		if z.numstages==5:
		  i=0.; i=z.Isp0[1]*9.81*log(h/(h-z.fuelmass[1])); i=i+z.Isp0[2]*9.81*log((h-z.m0[1])/(h-z.m0[1]-z.fuelmass[2]))
		  i=i+z.Isp0[3]*9.81*log((h-z.m0[1]-z.m0[2])/(h-z.m0[1]-z.m0[2]-z.fuelmass[3])); i=i+z.Isp0[4]*9.81*log((h-z.m0[1]-z.m0[2]-z.m0[3])/(h-z.m0[1]-z.m0[2]-z.m0[3]-z.fuelmass[4]))
		  i=i+z.Isp0[5]*9.81*log((h-z.m0[1]-z.m0[2]-z.m0[3]-z.m0[4])/(h-z.m0[1]-z.m0[2]-z.m0[3]-z.m0[4]-z.fuelmass[5]))
		y=o; e=gz; m=h; w=z.dMdt[1]; a=O; D=gz; X=z.burntime[1]; N=1; v=C
		if z.trajectory=='Minimum Energy':
			s=exp((2500.*(i/1000.)+23629.)/4477.)
		Y=pi/2-.25*(1000*s/I+pi)
		if z.trajectory=='Burnout Angle':
			Y=z.BA01*3.14592/180.
		while t<E and h>0:
			z.data['Time'].append(t)
		z.data['Height'].append(h); z.data['Mass'].append(m); z.data['Velocity'].append(v); z.data['Thrust'].append(f); z.data['Drag'].append(H); z.data['CD'].append(cd); z.data['Gamma'].append(C); z.data['Range'].append(I*g)
		if(t+y/5)>=W and e==gz:
				y=l
		e=gV; M=g; T=h; L=C; b=v; P=m; B=t
		if(t+y/5)<=r:
			U=P-(w*y/2); F=t
		else:
			F=K
		V=z.zF(h); cd=z.zq(b,h); H=cd*F*V*(b**2)/2; p0=z.zm(0); Q=z.zm(h); x=z.nozzlearea
		if(t+y/5)>r:
			f=0.0
		elif N==1:
			f=z.Isp0[1]*z.dMdt[1]*9.81+x*pi*(p0-Q)
		elif N>1:
			f=z.Isp0[N]*z.dMdt[N]*9.81
		m=f-H; g=g0*I**2/(h+I)**2; q=z.zU(T,B); k=B+y/2; S=(b*cos(L)/(I+T))*y/2; c=M+S; u=T+b*sin(L)*y/2; n=5
		if t<n:
			zg=0.0
		elif(t>=n)and(t<=r):
			zg=((Y-pi/2)/(r-n))
		else:
			zg=S/(y/2)+m*sin(q)/(b*P)-(g*cos(L)/b)
		v=L+zg*y/2; dv=(m/P)*cos(q)-g*sin(L); zV=b+dv*y/2; zQ=z.zU(u,k); t+=y; object=(zV*cos(v))/(I+u)*y; g=M+object; h=T+zV*sin(v)*y
		if h>T:
			p=h
		zJ=v; n=5
		if t<=n:
			zE=0.0
		elif(t>n)and(t<=r):
			global Y; zE=((Y-pi/2)/(r-n))
		else:
			zE=object/(y)+(m/(zV*U))*sin(zQ)-(g*cos(v)/zV)
		C=L+zE*y
		if(t+y/5)<=r:
			m=P-w*y
		zO=(m/U)*cos(zQ)-g*sin(v); v=b+zO*y
		if(t+y/5)>X and D==gz:
			if __name__=="__main__":
				pass
	    	else:
				J.Results.StageVelocityResult[N].SetValue("%4.2f"%gQ(v/1000)); J.Results.StageAngleResult[N].SetValue("%4.2f"%gQ(C*180/pi))
				J.Results.StageHeightResult[N].SetValue("%4.2f"%gQ(h/1000)); J.Results.StageRangeResult[N].SetValue("%4.2f"%gQ(I*g/1000))
				J.Results.StageTimeResult[N].SetValue("%4.2f"%t)
	    	if N==1:
				m=h-z.m0[1]
	    	if N==2:
				m=h-z.m0[1]-z.m0[2]
	    	if N==3:
				m=h-z.m0[1]-z.m0[2]-z.m0[3]
	    	P=m
	    	if N<z.numstages:
				N+=1; X+=z.burntime[N]; w=z.dMdt[N]
	    	else:
				D=gV
		if t>=E:
				if __name__=="__main__":
					pass
				else:
					zj=wx.MessageDialog(z.parent,"Error",wx.OK|wx.ICON_INFORMATION); zj.ShowModal(); zj.Destroy()
		if __name__=="__main__":
			pass
		else:
			J.Results.ApogeeResult.SetValue("%4.2f"%gQ(p/1000)); J.Results.ApogeeVelocityResult.SetValue("%4.3f"%gQ(v/1000))
			J.Results.RangeResult.SetValue("%4.3f"%gQ(I*g/1000)); J.Results.FlightTimeResult.SetValue("%4.1f"%t)
		return(z.data)
		def zU(z,h,t):
			if z.trajectory=='Thrust Vector':
				if t>z.TStartTurn and t<z.TEndTurn:
					zU=-z.zk(z.TurnAngle)
				else:
					zU=0.0
	  		else:
				zU=0.0
			return zU
		def zF(z,h):
			zl=1.225
			if h<19200:
				V=zl*exp(-h/8420)
	  		elif h>19200 and h<47000:
				V=zl*(.857003+h/57947)**-13.201
	  		else:
				V=1.e-6
			return V
		def zx(z,h):
			if h<=11000:
				t=15.04-.00649*h
			elif h<=25000:
				t=-56.46
			elif h>25000:
				t=-131.21+.00299*h
			return t
		def zm(z,h):
			t=z.zx(h)
			if h<=11000:
				p=101.29*((t+273.1)/288.08)**5.256
			elif h<=25000:
				p=22.65*exp(1.73-.000157*h)
			elif h>25000:
				p=2.488*((t+273.1)/288.08)**-11.388
			return p
		def zq(z,v,h):
			if v==0.:
				v=0.0001
	  		t=z.zx(h)+273.15; a=sqrt(1.4*287*t); zo=v/a; ld=z.LdivD; zh=z.missilediam; zr=z.zF(h); zW=0.; CF=0.
			if A>=1:
				zp=0.5*(d+G); zf=0.5*(G+d)*fh; zH=zf+0.5*G*zh; Mu=0.00001789; zI=zr*v*zp/Mu; zd=500000; zG=zI**(1./5.)
				zR=zd*((0.074/(zI**(1./5.)))-(1.328/sqrt(zI))); zA=1.328/sqrt(zI); zt=(0.074/(zG))-zR/zI
				if zI<zd:
					CF=zA
				else:
					CF=zt
				zW=2.*CF*(1.+2.*(R/zp))*(4.*A*(zH))/(3.141592*zh**2.)
			else:
				zW=0.
			if z.Nosecone=='V2':
				if zo>5:
					cd=0.15-zW
				elif zo>1.8 and zo<=5:
					cd=-0.03125*zo+0.30625-zW
	   			elif zo>1.2 and zo<=1.8:
					cd=-0.25*zo+0.7-zW
	   			elif zo>0.8 and zo<=1.2:
					cd=0.625*zo-0.35-zW
	   			elif zo<=0.8:
					cd=0.15-zW
	  		if z.Nosecone=='elliptical':
				if zo>=1.2:
					zK=0.824584774*ld**-0.532619017; zi=1.0156845; zy=-0.226354-0.238389*log(ld); cd=(zK*zi**zo)*zo**(zy)
	   			elif zo>=1.05 and zo<=1.2:
					ze=1/(-0.2383263138-0.266070229318*ld); zw=1/(0.15266+0.160535*ld); cd=ze*zo+zw
	   			elif zo<1.05:
					cd=-0.05*ld+0.25
	  		if z.Nosecone=='Conical':
				if zo>1.5:
					za=1.619038033*exp(-1.31926217*ld); zw=ld/(-0.45318-0.89392*ld); zD=0.886118*exp(-ld/1.121185); cd=za/(1+zw*exp(-zD*zo))
				elif zo>=1.05 and zo<=1.5:
					ze=1/(-0.10823-0.81349*ld); zw=1/(0.054882+0.363845*ld); cd=ze*zo+zw
	   			elif zo<1.05:
					cd=0.075*ld+0.275
	  		if(z.Nosecone=='tangent ogive'):
				if zo>=1.2:
					zX=0.278184983*exp(ld**-0.8894687916); zN=1.0129458; zv=-0.604615023/(1+9.5779826*exp(-1*2.2080809*ld)); cd=zX*(zN**zo)*(zo**(zv))
	   			elif zo>=1.05 and zo<=1.2:
					zs=1/(-0.156531249-0.35165656*ld); zN=1/(0.10668068+0.2160142549*ld); cd=zs*zo+zN
	   			elif zo<1.05:
					cd=-0.075*ld+0.275
	  		if(z.Nosecone=='parabolic'):
				if zo>=1.2:
					zX=0.2433566382*exp(ld**-7.1807129); zN=1.009709; zv=-0.567521484056/(1+5.59560038938568*exp(-1*2.23635526782648*ld)); cd=zX*(zN**zo)*(zo**(zv))
	   			elif zo>=1.05 and zo<=1.2:
					zs=1/(-0.1595385088-0.41826608398336*ld); zN=1/(0.123489761128+0.244747303231711*ld); cd=zs*zo+zN
	   			elif zo<1.05:
					cd=-0.025*ld+0.125
	  		if(z.Nosecone=='sears-haack'):
				if zo>=1.2:
					zX=0.243884345*exp(ld**-0.80690309); zN=1.0047095; zv=-0.60330669/(1+14.6196741884*exp(-1*3.27801239521*ld)); cd=zX*(zN**zo)*(zo**(zv))
	   			elif zo>=1.05 and zo<=1.2:
					zs=1/(-0.111417758-0.436291862*ld); zN=1/(0.090907066+0.26210278132*ld); cd=zs*zo+zN
	   			elif zo<1.05:
					cd=-0.05*ld+0.25; cd=cd+zW
	  		return cd
	def zk(z,degree):
		return degree*pi/180
if __name__=="__main__":
	 zY=zS(gC); zY.numstages=gJ(gE("Number of stages: ")); zY.numfins=gJ(gE("Number of fins: "))
	 for i in zn(1,zY.numstages+1):
		zY.fuelmass.append(gQ(gE("Fuel mass: "))); zM=(gQ(gE("Dry mass: "))); zY.m0.append(zM+zY.fuelmass[i]); zY.fuelfraction.append(zY.fuelmass[i]/zY.m0[i])
		zY.Isp0.append(gQ(gE("Isp: "))); zY.thrust0.append(gQ(gE("Thrust (kg f): "))*9.81); zY.dMdt.append(gQ(zY.thrust0[i]/(zY.Isp0[i]*9.81)))
		zY.burntime.append(gQ(gE("Burntime (sec): "))); zY.payload=gQ(gE("Payload (kg): ")); zY.missilediam=gQ(gE("Missile Diameter (m): "))
		zY.nozzlearea=gQ(gE("Nozzle Area (m^2): ")); zY.LdivD=gQ(gE("Nosecone: Length/Diam (dimensionless): ")); zY.rvdiam=gQ(gE("Re-entry Diameter (m): "))
		zY.est_range=gQ(gE("Est range (km): "))*1000; zY.BA01=gQ(gE("Burnout Angle (deg): "))*1; zY.mach=gQ(gE("Mach: "))*1.;zY.FinHeight=gQ(gE("Fin Height [m]: "))*1
		zY.SweepAngle=gQ(gE("Sweep Angle [deg]: "))*1; zY.FinTipChordLength=gQ(gE("Fin Tip Chord Length [m]: "))*1; zY.FinRootChord=gQ(gE("Fin Root Chord [m]: "))*1
		zY.FinThickness=gQ(gE("Fin Thickness [m]: "))*1
	 zY.trajectory="Minimum Energy"
	 zT=zY.zB(zY.trajectory)
	 zL='data.txt'
	 zb=gO(zL,'w')
	 for i in zn(1,zY.numstages+1):
		zb.write("STAGE %i Parameters:\n"%i); zb.write("Fuel mass (kg): "+gj(zY.fuelmass[i])+'\n'); zb.write("Dry mass (kg): "+gj(zY.m0[i]-zY.fuelmass[i])+'\n')
		zb.write("Fuel fract: "+gj(zY.fuelfraction[i])+'\n'); zb.write("Isp @ SL: "+gj(zY.Isp0[i])+'\n'); zb.write("Burn time (sec): "+gj(zY.burntime[i])+'\n')
		zb.write("Thrust (N): "+gj(zY.thrust0[i])+'\n'); zb.write("dM/dt: "+gj(zY.dMdt[i])+'\n')
	 zb.write("\nTIME,HEIGHT,VELOCITY,MASS,THRUST,DRAG,CD,GAMMA,RANGE\n"); zP=gl(zT['Time'],zT['Height'],zT['Velocity'],zT['Mass'],zT['Thrust'],zT['Drag'],zT['Cd'],zT['Gamma'],zT['mach'],zT['Range'])
	 for i in zn(1,go(zP)):
		for n in zn(0,go(zP[i])):
			zb.write('%.3f'%zP[i][n])
		zb.write(','); zb.write('\n')
	 z.outfile.close()
else:
	 import wx
