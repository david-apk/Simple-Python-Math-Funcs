#принимает два числа, делит их разницу на третье
#выдает список с числами от первого ко второму
def FREERANGE (x,y,scale,listSCALEOUT):
	x=float(x)
	y=float(y)
	z=int(scale)
	if z==0:
		z=1
	if x>y:
		g=(x-y)/z
		g=float(g)
		listSCALEOUT.append(x)
		xx=x-g
		for i in range(0,z-1):
			listSCALEOUT.append(round(xx,2))
			xx=xx-g
			xx=float(xx)
		listSCALEOUT.append(round(y))
	if x<y:
		g=(y-x)/z
		g=float(g)
		listSCALEOUT.append(x)
		xx=x+g
		for i in range(0,z-1):
			listSCALEOUT.append(round(xx,2))
			xx=xx+g
			xx=float(xx)
		listSCALEOUT.append(y)
	print('\nFREERANGE\n',x,'\n',y,'\nделим на ',scale,'итог:\n',listSCALEOUT)

while True:
	ee=input('\nпервый край: ')
	tt=input('второй край: ')
	zz=input('на сколько частей делить: ')
	uu=[]
	
	FREERANGE(ee,tt,zz,uu)

	