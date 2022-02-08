#!/usr/bin/env python3
#Autor Salem Yousef Alfauri (salfauri)

#please read below comments :

import re 
import sys 
import os 

#put command to be run at specific time "here"  
command = "here"


#change the variable hour1 to match you specific hour 
hour1 = '14' 
#change the variable min1 to match you specific mins 
min1 = '21'

#hour2 = '11'
#min2 = '50'



def is_it_time():
    while True:


        os.system("date > /tmp/date.txt")
        date_file = open('/tmp/date.txt','r')
        date_file_C = date_file.read()
        date_file.close()
    
        pattern_1 = re.compile(r'\d\d')
        matches = pattern_1.finditer(date_file_C)
 
        h = ''
        for match in matches:
            h = h + str(match.group(0))
            
        h_splitted = re.findall('..?',h)
       
        hour = h_splitted[0]
        min = h_splitted[1]
        sec = h_splitted[2]


        print("alarm set for :***"+str(hour1.strip())+"***"+str(min1.strip()))
        print("==========================================================")
        print("hour :" + str(hour.strip()) + "mins :" + str(min.strip()) +"sec :"+str(sec.strip()) ) 
        print("==========================================================")
   

        if (min.strip() == min1.strip() and hour.strip() == hour1.strip() and sec =="00"):
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            #os.system('date >> errors-by-infinite-recursion.txt')
            os.system(command)
            is_it_time()


is_it_time()
   


        




    
    
   
    
