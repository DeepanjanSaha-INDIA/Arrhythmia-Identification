import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('samples.csv')

df.rename(columns={"'MLII'":"ML"},inplace=True)
df.rename(columns={"'V5'":"V5"},inplace=True)
df.rename(columns={"'Elapsed time'":"time"},inplace=True)
print(df.head())

tot=21600
x=list(df['ML'])[:tot]

##--LOW PASS FILTER
low=[0,0]
x=12*[0]+x
for i,j in zip(range(12,len(x)),range(2,tot+2)):
    low.append(2*low[j-1]-low[j-2]+x[i]-2*x[i-6]+x[i-12])
low=low[2:]
print(len(low),len(x))
for i,j in enumerate(low):
    low[i]/=35
x=x[12:]
'''
plt.plot(range(len(x)),x,c='r',label='MLII')
plt.plot(range(len(low)),low,c='b',label='Low pass')
plt.legend()
plt.show()
'''
##--HIGH PASS FILTER
high=[0]
low=32*[0]+low
for i,j in zip(range(32,len(low)),range(1,tot+1)):
    high.append(32*low[i-16]-low[i]+low[i-32]-high[j-1])
low=low[32:]
high=high[1:]
print(len(low),len(high))
for i,j in enumerate(high):
    high[i]/=15
'''
plt.plot(range(len(high)),high,c='r',label='high pass')
plt.plot(range(len(low)),low,c='b',label='Low pass')
plt.legend()
plt.show()
'''
##--DERIVATIVE
deri=[]
high=[0]*2+high+[0]*2
for i in range(2,tot+2):
    deri.append((2*high[i+1]-2*high[i-1]+high[i+2]-high[i-2])/8)
high=high[2:-2]
print(len(deri),len(high))
'''
plt.plot(range(len(deri)),deri,c='r',label='derivative')
plt.plot(range(len(high)),high,c='b',label='high pass')
plt.legend()
plt.show()
'''
##--SQUARE
sq=[]
for i in range(len(deri)):
    sq.append(deri[i]*deri[i])
'''
plt.plot(range(len(sq)),sq,c='b',label='squared')
plt.show()
'''
##--MOVING AVERAGE
mv=[]
n=30
sq=[0]*n+sq+[0]*n
for i in range(n,len(deri)+n):
    mv.append(sum(sq[i:i+n])/n)
sq=sq[n:-n]
print(len(mv),len(mv))
'''
plt.plot(range(len(sq)),sq,c='r',label='squared')
plt.plot(range(len(mv)),mv,c='b',label='moving average')
plt.legend()
plt.show()
'''
##--THRESHOLD
sps=360
spk,npk,threshI,thresII,beat_count,prev,prev_val=0,0,0,0,0,0,False
thresh1,index=[],[]
for i,j in enumerate(mv):
    if j>threshI:
        spk=0.125*j+0.875*spk
    else:
        npk=0.125*j+0.875*npk
    threshI=0.75*npk+0.25*spk
    threshII=0.5*threshI
    thresh1.append(threshI)
    if i<50:
        print(j,threshI,j>threshI,spk,npk)
    if j>threshI and prev==False and j<prev_val:
        print('x')
        index.append(i)
        beat_count+=1
        prev=True
    if j<threshI and prev==True:
        prev=False
    prev_val=j
print(len(thresh1))
print(thresh1[:50])

##plt.plot(range(len(mv)),mv,c='b',label='moving average')
plt.plot(range(2000),thresh1[:2000],c='r',label='thresh')
plt.show()

print(beat_count)
no_beats=4
arr=[]
for i,j in zip(index[:-1],index[1:]):
    diff=(j-i)/100
    val=i
    for k in range(100):
        val+=diff
        arr.append(high[round(val)])
    break
print(len(arr))













