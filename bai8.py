# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:05:39 2024

@author: Student
"""

a = float(input(" so km taxi di duoc:"))
if a==1:
    b=20
    print("tien taxi la: ",b ,"k")
elif a<=3:
    b=a*13
    print("tien taxi la: ",b ,"k")
elif a<=8:
    b=3*13(a-3)*12
    print("tien taxi la: ",b ,"k")
elif a>8:
    b=3*13+5*12+(a-8)*10
    print("tien taxi la:",b)
if b>100:
    b=b*0.92
    print("tien taxi sau giam la:",b )    

    
