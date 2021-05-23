#-------------------1------------------#
#def chang(arr):
#    for i in range(len(arr)):
#        if arr[i]>0:
#            arr[i]="big"
#
#    print(arr)

#arr=[]
#length= int(input("PLZ enter the length of the array :"))
#for i in range (0,length):
#    arr1=int(input("inter the value"))
#    arr.append(arr1)
#chang(arr)
#--------------------------------------#

#--------------2-----------------------#

#def sumTotal(arr):
#    count=0
#    for i in range(len(arr)):
#        if arr[i]>0:
#            count=count+1
#    arr[len(arr)-1]=count
#    print(arr)
#arr=[]
#length= int(input("PLZ enter the length of the array :"))
#for i in range (0,length):
#    arr1=int(input("inter the value"))
#    arr.append(arr1)
#
#sumTotal(arr)
#---------------------------------------------#

#-------------------3---------------------------#

#-------------------3---------------------------#
#def sum(arr):
#    sum=0
#    for i in range (len(arr)):
#        sum=sum+arr[i]
#    print(sum)    
#arr=[]
#length= int(input("PLZ enter the length of the array :"))
#for i in range (0,length):
#    arr1=int(input("inter the value"))
#    arr.append(arr1)
#
#sum(arr)
#-----------------------------------------------#
#-------------------4---------------------------#

#def sumarr(arr):
#    sum=0
#    for i in range (len(arr)):
#        sum=sum+arr[i]
#    avg=sum/len(arr)
#
#    print(avg)    
#arr=[]
#length= int(input("PLZ enter the length of the array :"))
#for i in range (0,length):
#    arr1=int(input("inter the value"))
#    arr.append(arr1)

#sumarr(arr)
#-----------------------------------------------#
#---------------------5------------------------#
#def sumarr(arr):
#    count=0
#    for i in range (len(arr)):
#      count=count+1
#
#    print(count)    
#arr=[]
#
#for i in range (1000):
#    arr1=input("inter the value")
#    if arr1=="stop":
#        break 
#    arr.append(arr1)
#      
#sumarr(arr)
#-----------------------------------------------#
#------------------6-----------------------------#

#def min(arr):
#    min=arr[0]
#    if len(arr)==0:
#        return "emty"
#    for i in range (len(arr)):
#        if min > arr[i]:
#            min=arr[i]
#    print(min)
#arr=[]
#length= int(input("PLZ enter the length of the array :"))
#for i in range (0,length):
#    arr1=int(input("inter the value"))
#    arr.append(arr1)
#min(arr)
#-----------------------------------------------#
#-----------------6----------------------------#
#def minarr(arr):
#    
#    if len(arr)==0:
#        return 'empty'
#    min=arr[0]
#    for i in range (len(arr)):
#        if min > arr[i]:
#            min=arr[i]
#    print(min)
#arr=[]
#minarr(arr)
#print(minarr)

#-------------------------------------------------#
#-------------------7------------------------------#

#def maxarr(arr):
#    
#    if len(arr)==0:
#        return 'empty'
#    max=arr[0]
#    for i in range (len(arr)):
#        if max < arr[i]:
#            max=arr[i]
#    print(min)
#arr=[]
#maxarr(arr)
#-------------------------------------------------#
#--------------------8-----------------------------#
#def full(arr):
#    length=0
#    min=arr[0]
#    max=arr[0]
#    sum=0
#    for i in range (len(arr)):
#        length=length+1
#        sum=sum+arr[i]
#        if max>arr[i]:
#          max=arr[i]
#        elif min<arr[i]:
#            min=arr[i]
#        
#    avg=sum/length
#    print(avg)
#    print(max)
#    print(min)
#    print(length)    
#arr=[]
#length= int(input("PLZ enter the length of the array :"))
#for i in range (length):
#    arr1=int(input("inter the value"))
#    
#    arr.append(arr1)
#      
#full(arr)
#------------------------------------------------------------#
#--------------------9----------------------------------------#
#def Reverse(arr):
#    j=1
#    a=int(len(arr)/2)
#    for i in range (a):
#        temp=arr[i]
#        arr[i]=arr[len(arr)-j]
#        arr[len(arr)-j]=temp
#        j=j+1
#    print(arr)
#arr=[1,2,3,4,5,6]
#Reverse(arr)
#--------------------------------------------------------------#