import base64
from time import time
def checkHash(data:bytes)->bool:
	try:
		d=base64.b64decode(data)
		print(d.decode('unicode_escape').encode())
		return True
	except:
		return False
def funcValid(tm:str,hash:str)->bool:
	try:
		tm=int(tm)
		ctime=int(time())
		timeRAnge=[ctime-length for length in range(1,second+1)]
		if tm in timeRAnge:
			if checkHash(hash.encode()):
				return True
			else:
				return False
		return False
	except:
		return False
def check(st:list)->bool:
	escape=int(st[0])
	count=1
	enc=list(st[1])
	time=''
	for n in enc:
		if count%escape==0:
			time+=enc.pop(count-1)
		count+=1
	if len(st)==3:
		time+=st[2]
		eq=st[2]
	if len(st)==4:
		time+=st[2]
		eq=st[3]
	wha=(''.join(enc)+'='*int(eq))
	return funcValid(time[0:10],wha)

if __name__ == '__main__':
	second=15   # time in second to increase hash valid time
	while True:
		try:
			st=input('Enter Hash -->')
			if check(st.split('-')):
				print('Success')
			else:
				print('Error')
		except:
			print('Error')