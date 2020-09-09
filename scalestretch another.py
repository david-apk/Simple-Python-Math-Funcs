#растягивает список в самых контрастных участках
#аргументы:
	#1.список на вход
	#2.число элементов в выходном списке
def SCALESTRETCH(listX,numOUT):
	if len(listX)<numOUT:
		addpoints=numOUT-int(len(listX))
		for i in range(0,addpoints):
			listY= listX[1:]
			listZ=[]
			iterX=iter(listX)
			iterY=iter(listY)
			for i in listY:
				d= (next(iterX)-next(iterY))
				listZ.append(abs(d))
			maxdif=max(listZ)
			t =listZ.index(maxdif)
			t=listX[t]
			insertindex=listX[listZ.index(maxdif)]
			nextindex=listX[listZ.index(maxdif)+1]
			if insertindex>nextindex:
				value= abs((round(float(maxdif/2),2))-t)
			if insertindex<nextindex:
				value= abs((round(float(maxdif/2),2))+t)
			if insertindex==nextindex:
				value= insertindex
			listX.insert(listZ.index(maxdif)+1, value)	

a=[0, 5, 2, 3, 0, 4, 10, 11]			
print('input',a)
SCALESTRETCH(a,15)
print('output',a)