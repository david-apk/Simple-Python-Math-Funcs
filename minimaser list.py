
#функция принимает список интов любого размера
#функция отдает список размером от 1 до 8 элементов с минимальными потреями пиковых значений, значений краев и общего среднего
#аргументы:
	#1.входной список int or float
	#2.количество элементов на выходе (от 8 до 1)
def MINIMASER(listX, segments):
    if len(listX)>segments:
        correcttime=int(round((len(listX)/2),0))
        correctright=listX[correcttime::]
        correctleft=listX[:correcttime]
        correcttime=int(round((correcttime/2),0))
        right2=correctright[correcttime::]
        right2=right2[:-1]
        right1=correctright[:correcttime]
        right1=right1[1::]
        left2=correctleft[correcttime::]
        left2=left2[:-1]
        left1=correctleft[:correcttime]
        left1=left1[1::]
        exportlist=[]
        exportlist.append(round((listX[0]),2))
        #Left
        #1
        if min(left1)==min(listX):
            if ((sum(left1))/len(left1))<((sum(left2))/len(left2)):
            	if ((sum(left1))/len(left1))<((sum(right1))/len(right1)):
            		if ((sum(left1))/len(left1))<((sum(right2))/len(right2)):
                		exportlist.append(round((min(left1)),2))
        if max(left1)==max(listX):
            if ((sum(left1))/len(left1))>((sum(left2))/len(left2)):
            	if ((sum(left1))/len(left1))>((sum(right1))/len(right1)):
            		if ((sum(left1))/len(left1))>((sum(right2))/len(right2)):
                		exportlist.append(round((max(left1)),2))
        if len(exportlist)<2:
        	exportlist.append(round((sum(left1)/len(left1)),2))
            #2
        if min(left2)==min(listX):
            if ((sum(left2))/len(left2))<((sum(left1))/len(left1)):
            	if ((sum(left2))/len(left2))<((sum(right1))/len(right1)):
            		if ((sum(left2))/len(left2))<((sum(right2))/len(right2)):
            		    exportlist.append(round((min(left2)),2))
        if max(left2)==max(listX):
            if ((sum(left2))/len(left2))>((sum(left1))/len(left1)):
            	 if ((sum(left2))/len(left2))>((sum(right1))/len(right1)):
            	 	if ((sum(left2))/len(left2))>((sum(right2))/len(right2)):
                		exportlist.append(round((max(left2)),2))
        if len(exportlist)<3:
        	exportlist.append(round((sum(left2)/len(left2)),2))
        #central
        exportlist.append(round((correctleft[-1]),2))
        exportlist.append(round((correctright[0]),2))
        #Right
        #1
        if min(right1)==min(listX):
            if ((sum(right1))/len(right1))<((sum(left1))/len(left1)):
            	if ((sum(right1))/len(right1))<((sum(left2))/len(left2)):
            		if ((sum(right1))/len(right1))<((sum(right2))/len(right2)):
           		     exportlist.append(round((min(right1)),2))
        if max(right1)==max(listX):
            if ((sum(right1))/len(right1))>((sum(left2))/len(left2)):
            	if ((sum(right1))/len(right1))>((sum(left1))/len(left1)):
            		if ((sum(right1))/len(right1))>((sum(right2))/len(right2)):
           		     exportlist.append(round((max(right1)),2))
        if len(exportlist)<6:
        	exportlist.append(round((sum(right1)/len(right1)),2))
            #2
        if min(right2)==min(listX):
            if ((sum(right2))/len(right2))<((sum(left1))/len(left1)):
            	if ((sum(right2))/len(right2))<((sum(left2))/len(left2)):
            		if ((sum(right2))/len(right2))<((sum(right1))/len(right1)):
           		     exportlist.append(round((min(right2)),2))
        if max(right2)==max(listX):
            if ((sum(right2))/len(right2))>((sum(left2))/len(left2)):
            	if ((sum(right2))/len(right2))>((sum(left1))/len(left1)):
            		if ((sum(right2))/len(right2))>((sum(right1))/len(right1)):	
              		  exportlist.append(round((max(right2)),2))
        if len(exportlist)<7:
        	exportlist.append(round((sum(right2)/len(right2)),2))
        exportlist.append(round((listX[-1]),2))
        
          
        
        if segments<8:
        	newexportlist=[] 
        	
        if segments==7:
        	newexportlist.append(exportlist[0])
        	newexportlist.append(exportlist[1])
        	newexportlist.append(exportlist[2])
        	newexportlist.append(round(((exportlist[3]+exportlist[4])/2),2))
        	newexportlist.append(exportlist[5])
        	newexportlist.append(exportlist[6])
        	newexportlist.append(exportlist[-1])
        	return newexportlist      	       
        	
        if segments==6:
        	newexportlist.append(exportlist[0])
        	newexportlist.append(round(((exportlist[1]+exportlist[2])/2),2))
        	newexportlist.append(exportlist[3])
        	newexportlist.append(exportlist[4])
        	newexportlist.append(round(((exportlist[5]+exportlist[6])/2),2))
        	newexportlist.append(exportlist[-1])
        	return newexportlist     	        	
        	
        if segments==5:
        	newexportlist.append(exportlist[0])
        	newexportlist.append(round(((exportlist[1]+exportlist[2])/2),2))
        	newexportlist.append(round(((exportlist[4]+exportlist[3])/2),2))
        	newexportlist.append(round(((exportlist[5]+exportlist[6])/2),2))
        	newexportlist.append(exportlist[-1])
        	return newexportlist              	
        		        	
        if segments==4:
        	newexportlist.append(exportlist[0])
        	newexportlist.append(round(((exportlist[1]+exportlist[2]+exportlist[3])/3),2))
        	newexportlist.append(round(((exportlist[5]+exportlist[6]+exportlist[4])/3),2))
        	newexportlist.append(exportlist[-1])
        	return newexportlist       	        	
        	
        if segments==3:
        	newexportlist.append(round(((exportlist[0]+exportlist[1]+exportlist[2])/3),2))
        	newexportlist.append(round(((exportlist[4]+exportlist[3])/2),2))
        	newexportlist.append(round(((exportlist[-1]+exportlist[5]+exportlist[6])/3),2))
        	return newexportlist 
        	        	
        if segments==2:
        	newexportlist.append(round(((exportlist[0]+exportlist[1]+exportlist[2]+exportlist[3])/4),2))
        	newexportlist.append(round(((exportlist[-1]+exportlist[5]+exportlist[6]+exportlist[4])/4),2))
        	return newexportlist        
        
        if segments==1:
        	newexportlist.append(round(((exportlist[0]+exportlist[1]+exportlist[2]+exportlist[3]+exportlist[-1]+exportlist[5]+exportlist[6]+exportlist[4])/8),2))
        	return newexportlist                 




myinput=[8,6,5,7,5,4,5,6,5,4,6,5,4,33,9,2,6]
seg=5
myoutput=[]
print('input',myinput,'\n')
myoutput=MINIMASER(myinput,seg)
print('output',myoutput)