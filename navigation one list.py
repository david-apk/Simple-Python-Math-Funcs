
#ФУНКЦИЯ НАВИГАЦИИ ПО ОДНОМУ СПИСКУ
#первичная обработка данных
#принимает: 
#1.номер итерации
#2.список для обработки (вся история), где индекс 0 это самая старая запись
#3.словарь для информации об идентичных к посл.
#4.словарь число:итерация (событие:последний раз)
#5.список для истории нижней границы
#6.словарь для информации о ближайших низших
#7.список для истории средних от истории
#8.словарь для информации о ближайших верхних
#9.список для истории верхней границы
#10.список для истории разниц
#записываеет в каждый список значение последним
########################################
def NAVIGoneLIST(time,listIN, dicSIMMIDOUT, dicINTIMEOUT, listLOWOUT, dicSIMLOWOUT, listMIDOUT, dicSIMHIOUT, listHIOUT, listDIFOUT):
#3 идентичное число: самое позднее его упом.
	dicSIMMIDOUT.clear()
	if time> 0:
		if listIN[-1] in dicINTIMEOUT:
			dicSIMMIDOUT['last time']= dicINTIMEOUT[listIN[-1]]
			dicSIMMIDOUT['times between']= (len(listIN)-dicINTIMEOUT[listIN[-1]])- 2
			reason= int(dicSIMMIDOUT['last time'])
			dicSIMMIDOUT['cycle']= listIN[reason : ]
			nexttimeexpect= list(dicSIMMIDOUT['cycle'])
			dicSIMMIDOUT['shortforecast']= nexttimeexpect[1: 2]
			dicSIMMIDOUT['first meet']=listIN.index(listIN[-1])
#4 обновляет упоминание последнейго числа
	dicINTIMEOUT[listIN[-1]]= float(time)	
#5 нижнаяя граница всей истории
	low= round(float(min(listIN)),2)
	listLOWOUT.append(low)	
#6 похожее.ниж.число : самое позднее его упомин.
	if time> 0:
		def nearlow(x):
			if x<  listIN[-1]:
				return 1
			else:
				return 0
		b= filter(nearlow, listIN)
		b= list(b)
		dicSIMLOWOUT.clear()
		if len(b)> 0:
			dicSIMLOWOUT['low sim value']= max(b)
			dicSIMLOWOUT['last time']= dicINTIMEOUT[max(b)]
			dicSIMLOWOUT['times between']= (len(listIN)-dicINTIMEOUT[max(b)])- 2
			reason= int(dicSIMLOWOUT['last time'])
			dicSIMLOWOUT['cycle']= listIN[reason : ]
			nexttimeexpect= list(dicSIMLOWOUT['cycle'])
			dicSIMLOWOUT['shortforecast']= nexttimeexpect[1: 2]
			dicSIMLOWOUT['first meet']= float(listIN.index(max(b)))		
#7 среднее значение всей истории
	mid = (sum(list(map(float, listIN))))/len(listIN)
	mid = round(float(mid),2)
	listMIDOUT.append(mid)
#8 похожее.выш.число : самое позднее его упомин.
	if time> 0:
		def nearhi(x):
			if x>  listIN[-1]:
				return 1
			else:
				return 0
		b= filter(nearhi, listIN)
		b= list(b)
		dicSIMHIOUT.clear()
		if len(b)> 0:
			dicSIMHIOUT['hight sim value']= min(b)
			dicSIMHIOUT['last time']= dicINTIMEOUT[min(b)]
			dicSIMHIOUT['times between']= (len(listIN)- dicINTIMEOUT[min(b)])- 2
			reason = int(dicSIMHIOUT['last time'])
			dicSIMHIOUT['cycle']= listIN[reason : ]
			nexttimeexpect= list(dicSIMHIOUT['cycle'])
			dicSIMHIOUT['shortforecast']= nexttimeexpect[1: 2]
			dicSIMHIOUT['first meet']=listIN.index(min(b))			
#9 верхняя граница всей истории
	hight= round(float(max(listIN)),2)
	listHIOUT.append(hight)	
#10 разница между верхом и низом за всю историю
	difference= round((hight-low),2)
	listDIFOUT.append(difference)
	if 'shortforecast' in dicSIMMIDOUT:
			midoption=dicSIMMIDOUT['shortforecast']
	if 'shortforecast' in dicSIMLOWOUT:
			lowoption=dicSIMLOWOUT['shortforecast']
	if 'shortforecast' in dicSIMHIOUT:
			hioption=dicSIMHIOUT['shortforecast']






##################################
#ТЕСТ ДАНО
time=0#итерации
inp=[]#последнее значение
simmid={}#точто такое же(если было)
numtime={}#когда было такое же
low=[]
simlow={}
mid=[]
simhi={}	
hight=[]
dif=[]

#ЗАПУСК ТЕСТА
while True:
	inputNUMBER=input('\nвведите число ')
	inp.append(float(inputNUMBER))
	NAVIGoneLIST(time,inp,simmid,numtime,low,simlow,mid,simhi,hight,dif)	
	
	#ЛОГ
	print('\n\n\n\nНАВИГАЦИЯ ПО ОДНОМУ СПИСКУ')
	print('итерация',time)
	print('последнее число',inputNUMBER)
	print('предыдущее идентичное число',simmid,'\n')
	if 'cycle' in simlow:
		print('похоже на начало этого',simlow['cycle'],'\n')
	if 'shortforecast' in simlow:
		print('ожидается', simlow['shortforecast'],'\n')
	if 'cycle' in simhi:
		print('похоже на начало этого',simhi['cycle'],'\n')
	if 'shortforecast' in simhi:
		print('ожидается', simhi['shortforecast'],'\n')
	print('низ',low)
	print('середина',mid)
	print('верх',hight)
	print('разница между верхом и низом',dif)
	print('список\n',inp,'\n')
	print('известные факты и их последнее упоминание\n',numtime,'\n')
	
	
	
	
	time=time+1