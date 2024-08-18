# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:37:39 20245.

@author: Student
"""

distance=float(input("Nhap diem trung binh(GPA):"))
if distance <3.5:
    print("Hoc luc kem")
elif 3.5 <= distance <5.0:
    print("Hoc luc yeu")
elif  5.0 <= distance <7.0:
    print("Hoc luc trung binh")
elif  7.0 <= distance <8.0:
    print("Hoc luc kha")    
elif 8.0 <= distance <9.0:
    print("Hoc luc gioi")    
elif 9.0 <= distance <=10:
    print("Hoc xuat sac")    
else:
    print("Diem khong hop le")
    