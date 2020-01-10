# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 20:41:24 2020

@author: MSI
"""

import csv
def without_bracket(row):
    St1 = row
    St = St1[::-1]
    if (St[0]+St[1] != 'AN'):
        #print("hello")
        for i in range(len(St)):
            list.append(St[i])
            if(St[i].isupper()) ==True:
                if(St[i+1].islower())==True:
                    break
        F_St = "".join(list)
        Final = F_St[::-1]
    else:
        Final = St1
    return Final
    
def bracket(row):
    for i in range (len(row)):
        if(row[i] == '('):
            start =i
        elif(row[i]==')'):
            end = i
    
    return row[(start+1):end]
    



a =[]
F_List = []
F_List1 = []
F_List2 = []
F_List3 = []
F_List4 = []
List1 = []
List2 = []
with open('User1data.csv', 'r') as file:
    reader = csv.reader(file)
    a.append(next(reader))
    for row in reader:
        for i in range(4,6):
            list = []
            St1 = row[i]
            St = St1[::-1]
            if(St[0] == ')' or St[0] =='('):
               List1 =[]
               Value = (bracket(row[4]))
               List1.append(Value)
               F_List = List1
               F_List1.append(F_List)#To make in a MultiList for writing in row wise manner 
              
               
            else:
                List2 = []
                Value = without_bracket(row[5])
                List2.append(Value)
                F_List3 = List2
                F_List2.append(F_List3)#To make in a MultiList for writing in row wise manner
               
                    
a = F_List1
a.append(a)#To make in a MultiList for writing in row wise manner
#print(a)               
with open('User1.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerow(["Recommended"])
    for entries in a:
        writer.writerows([entries])
    
                


        
        
        
        
   


