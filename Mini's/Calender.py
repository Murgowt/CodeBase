mon=int(input("Enter the Month Number."))
year=int(input("Enter the Year."))
if year%4==0:
    mon_nod=[31,29,31,30,31,30,31,31,30,31,30,31]
else:
    mon_nod=[31,28,31,30,31,30,31,31,30,31,30,31]
temp1=(year-1)%400
temp2=temp1//100
if temp2==0:
    temp3=0
elif temp2==1:
    temp3=5
elif temp2==2:
    temp3=3
elif temp2==3:
    temp3=1    
temp4=temp1%100
temp4_ly=temp4//4
temp_oy=temp4-temp4_ly
temp5=((temp4_ly*2)+temp_oy)%7
sum=0
for i in range(0,mon-1):
    sum=sum+mon_nod[i]
temp6=(sum+1)%7
odddays=(temp3+temp5+temp6)%7

if mon==1:
    mon_name="January"
elif mon==2:
    mon_name="February"    
elif mon==3:
    mon_name="March"
elif mon==4:
    mon_name="April"      
elif mon==5:
    mon_name="May"      
elif mon==6:
    mon_name="June"      
elif mon==7:
    mon_name="July"      
elif mon==8:
    mon_name="August"      
elif mon==9:
    mon_name="September"      
elif mon==10:
    mon_name="October"      
elif mon==11:
    mon_name="November"      
elif mon==12:
    mon_name="December" 
counter=1
j=0 
print("\n\n",mon_name,year)
print("SUN MON  TUE  WED  THU  FRI  SAT")    
while(counter<=mon_nod[mon-1]):
        if (j!=odddays):
            print("     ",end='')
        else:
            while(counter<=mon_nod[mon-1]):
                if (j==6 or j==13 or j==20 or j==27 or j==34):
                    print(counter,"\n")
                    counter=counter+1
                    j=j+1
                else:
                    if counter>=10:
                        print(counter,"  ",end='')
                        counter=counter+1
                        j=j+1 
                    else:    
                        print(counter,"   ",end='')
                        counter=counter+1
                        j=j+1    
        j=j+1        
        
        
