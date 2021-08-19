
import serial
from ast import literal_eval
import time
import re
import struct

ser = serial.Serial('/dev/ttyS0', baudrate = 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
def data():
	return hex(ord(ser.read()))

def arr1(a1):
	print("..............found 1st",a1)
	a=0
	while(a!=7):
		print("appending in w1 ")
		w1.append(data())
		a=a+1

def arr2(a2):
	print("................found 2nd",a2)
	b=0
	while(b!=16):
		print("appending in w2 ")
		w2.append(data())
		b=b+1
def arr3(a3):
        print("..............found 3rd",a3)
        c=0
        while(c!=6):
                print("appending in cr ")
                cr.append(data())
                c=c+1
def arr4(a4):
        print("..............found 4th",a4)
        d=0
        while(d!=5):
                print("appending in arth ")
                arth.append(data())
                d=d+1

def arr5(a5):
        print("..............found 5th",a5)
        e=0
        while(e!=3):
                print("appending in vcp ")
                vcp.append(data())
                e=e+1
def arr6(a6):
        print("..............found 6th",a6)
        f=0
        while(f!=7):
                print("appending in std")
                std.append(data())
                f=f+1
def arr7(a7):
        print("..............found 7th",7)
        g=0
        while(g!=3):
                print("appending in  sts")
                sts.append(data())
                g=g+1
def arr8(a8):
        print("..............found 8th",a8)
        h=0
        while(h!=2):
                print("appending in ldc ")
                ldc.append(data())
                h=h+1
def arr9(a9):
        print("..............found 9th",a9)
        i=0
        while(i!=3):
                print("appending in ecgs ")
                ecgs.append(data())
                i=i+1
def arr10(a10):
        print("..............found 1oth",a10)
        j=0
        while(j!=3):
                print("appending in sa ")
                sa.append(data())
                j=j+1

def arr11(a11):
        print("..............found 11th",a11)
        k=0
        while(k!=4):
                print("appending in sst ")
                sst.append(data())
                k=k+1
def arr12(a12):
        print("..............found 12th",a12)
        l=0
        while(l!=2):
                print("appending in mid ")
                mid.append(data())
                l=l+1
def arr13(a13):
        print("..............found 13th",a13)
        m=0
        while(m!=1):
                print("appending in sri ")
                sri.append(data())
                m=m+1
def arr14(a14):
        print("..............found 14th",a14)
        n=0
        while(n!=2):
                print("appending in ecga")
                ecga.append(data())
                n=n+1
def arr15(a15):
        print("..............found 15th",a15)
        o=0
        while(o!=4):
                print("appending in ci")
                ci.append(data())
                o=o+1
def arr16(a16):
        print("..............found 16th",a16)
        p=0
        while(p!=7):
                print("appending in  td")
                td.append(data())
                p=p+1
def arr17(a17):
        print("..............found 17th",a17)
        q=0
        while(q!=6):
                print("appending in  w4")
                w4.append(data())
                q=q+1
def arr18(a18):
        print("..............found 18th",a18)
        t=0
        while(t!=2):
                print("appending in vldc")
                vldc.append(data())
                t=t+1
def arr19(a19):
        print("..............found 19th",a19)
        u=0
        while(u!=7):
                print("appending in sto1 ")
                sto1.append(data())
                u=u+1
def arr20(a20):
        print("..............found 2oth",a20)
        v=0
        while(v!=5):
                print("appending in sto2")
                sto2.append(data())
                v=v+1




w1=[]
w2=[]
cr=[]
arth=[]
vcp=[]
std=[]
sts=[]
ldc=[]
ecgs=[]
sa=[]
sst=[]
mid=[]
sri=[]
ecga=[]
ci=[]
td=[]
w4=[]
vldc=[]
sto1=[]
sto2=[]

while True:
	r=data()
	print(r)
	time.sleep(.7)
	if(r=="0x1"):
		arr1(r)
	elif(r=="0x2"):
		arr2(r)
        elif(r=="0x4"):
                arr3(r)
        elif(r=="0x5"):
                arr4(r)
        elif(r=="0x6"):
                arr5(r)
        elif(r=="0x7"):
                arr6(r)
        elif(r=="0x8"):
                arr7(r)
        elif(r=="0x9"):
                arr8(r)
        elif(r=="0xA"):
                arr9(r)
        elif(r=="0xB"):
                arr10(r)
        elif(r=="0xC"):
                arr11(r)
        elif(r=="0xD"):
                arr12(r)
        elif(r=="0xE"):
                arr13(r)
        elif(r=="0xF"):
                arr14(r)
        elif(r=="0x10"):
                arr15(r)
        elif(r=="0x11"):
                arr16(r)
        elif(r=="0x12"):
                arr17(r)
        elif(r=="0x13"):
                arr18(r)
        elif(r=="0x15"):
                arr19(r)
        elif(r=="0x16"):
                arr20(r)

	else:
		print("------------pass-----------")
	print("currently list are ",w1,w2,cr,arth,vcp,std,ldc,ecgs,sa,sst,mid,sri,ecga,ci,td,w4,vldc,sto1,sto2)

