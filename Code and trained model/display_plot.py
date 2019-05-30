import matplotlib.pyplot as plt

def derivative(y):
	x=[]
	for i,j in zip(y[:-1],y[1:]):
		x.append(j-i)
	plt.title('derivative')
	plt.plot(range(len(x)),x)
	plt.show()
	return x

def square(deri):
	x=[]
	for i in deri:
		x.append(i*i)
	
	plt.title('square')
	plt.plot(range(len(x)),x)
	plt.show()
	
	return x

def threshold1(sq):
	x=[]
	for i in sq:
		if i<0.001:
			x.append(0)
		else:
			x.append(i)
	
	plt.title('threshold')
	plt.plot(range(len(x)),x)
	plt.show()
	
	return x

def moving_window(th):
	x=[]
	for i,j in enumerate(th[3:]):
		x.append((th[i-3]+th[i-2]+th[i-1]+th[i])/4)
	
	plt.title('moving window')
	plt.plot(range(len(x)),x)
	plt.show()
	
	return x

def threshold2(mv):
	x=[]
	for i in mv:
		if i>0.0025:
			x.append(1)
		else:
			x.append(0)
	
	plt.title('threshold 2')
	plt.plot(range(len(x)),x)
	plt.show()
	
	return x

def peak_detection(time,th2):
	x=[]
	for i,j in enumerate(zip(th2[1:],th2[:-1])):
		if j==(0,1):
			x.append(time[i])
	#print('times scales',x)
	return x

def string_conv(pd):
	x=[]
	for i in pd:
		minute,sec=i.split(':')
		x.append(60*eval(minute)+eval(sec))
	return x

def RR_interval(time_scale):
	x=[]
	for i,j in zip(time_scale[:-1],time_scale[1:]):
		x.append(j-i)
	return x

def main():
	f=open("100.csv")
	data=f.read().split('\n')
	print(len(data))
	time,x,y,vx=[],[],[],-1
	for i,j in enumerate(data[:2000]):
		t,_,_,mvii,v5=j.split(',')
		x.append(eval(v5)-eval(mvii))
		time.append(eval(t))
		if vx==-1:
			vx=eval(v5)
		vx=0.75*vx+0.25*eval(v5)
		y.append(vx)
	
	plt.plot(range(len(x)),x,c='r')
	#plt.plot(range(len(y)),y,c='b')
	plt.title('Comparison B/w Input and Filtered signal')
	plt.xlabel('samples')
	plt.ylabel('Mili Volts (mV)')
	plt.show()
	'''
	deri=derivative(y)
	sq=square(deri)
	th1=threshold1(sq)
	mv=moving_window(th1)
	th2=threshold2(mv)
	pd=peak_detection(time,th2)
	'''
	'''
	time_scale=string_conv(pd)
	time_scale=RR_interval(time_scale)
	print(len(time_scale))
	'''
	#print(len(pd))
	'''
	s=0
	for i in time_scale:
		s+=i
	s/=len(time_scale)
	print(s)
	if 60<60/s<100:
		print('normal heart beat with {} bpm'.format(60//s))
	elif 60/s<60:
		print('Bradycardia (Arrhythmia) with {} bpm'.format(60//s))
	else:
		print('Tachycardia (Arrhythmia) with {} bpm'.format(60//s))
	'''

if __name__=="__main__":
	main()
