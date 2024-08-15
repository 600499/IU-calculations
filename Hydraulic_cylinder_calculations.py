import tkinter as tk
from tkinter import ttk

import math 
def Cylinder_cap_area (num1):
    Cylinder_cap_side_area = (math.pi/4*num1**2)
    return Cylinder_cap_side_area
def Cylinder_rod_area (num1, num2):
    Cylinder_rod_side_area = (math.pi/4*(num1-num2)**2)
    return Cylinder_rod_side_area
Power_pack = float(input("enter the powerpack:"))
if Power_pack == 22:
    Pump_Flow_rate = 100
    print(f"Flow rate : {Pump_Flow_rate} LPM")
elif Power_pack == 30:
   Pump_Flow_rate = 140
   print(f"Flow rate : {Pump_Flow_rate} LPM")
elif Power_pack == 45:
   Pump_Flow_rate = 200
   print(f"Flow rate : {Pump_Flow_rate} LPM")
else: 
 print("enter the valid power pack") 
print(f"powerpack : {Power_pack}")  
'to convert the pump flow rate into mm^3/s'
Pump_Flow_rate_in_mm_cube_per_second = (Pump_Flow_rate*10**6)/60
print(f"Pump flow rate in mm^3/s : {Pump_Flow_rate_in_mm_cube_per_second}")
#IU_size = int(input("enter the IU size:"))

if IU_size == 600 :
    Cylinder_Cap_Diameter = 115
    Cylinder_Rod_Diameter = 55
    Cylinder_Stroke_length = 1250
elif IU_size == 900:
    Cylinder_Cap_Diameter = 130  
    Cylinder_Rod_Diameter = 60
    Cylinder_Stroke_length = 225
elif IU_size == 1400:
    Cylinder_Cap_Diameter = 150
    Cylinder_Rod_Diameter = 75
    Cylinder_Stroke_length = 290
elif IU_size == 2350:
    Cylinder_Cap_Diameter =  180 
    Cylinder_Rod_Diameter = 80
    Cylinder_Stroke_length = 325
elif IU_size == 430 :
    Cylinder_Cap_Diameter = 107.5  
    Cylinder_Rod_Diameter = 55
    Cylinder_Stroke_length = 203
else:
    print("Invalid IU size. Please enter a valid size.")

print(f"Cylinder Cap Diameter: {Cylinder_Cap_Diameter}")
print(f"Cylinder Rod Diameter: {Cylinder_Rod_Diameter}")
Cylinder_Cap_Diameter = 300
Cylinder_Rod_Diameter = 200
Cylinder_cap_side_area = Cylinder_cap_area (Cylinder_Cap_Diameter)
print(f"cylinder cap side area: {Cylinder_cap_side_area} mm^2")
Cylinder_rod_side_area = Cylinder_rod_area (Cylinder_Cap_Diameter,Cylinder_Rod_Diameter)
print(f"cylinder rod side area: {Cylinder_rod_side_area} mm^2")
print(f"Screw stroke: {Cylinder_Stroke_length} mm")
Cylinder_extension_velocity = Pump_Flow_rate_in_mm_cube_per_second/Cylinder_cap_side_area
Cylinder_retraction_velocity = Pump_Flow_rate_in_mm_cube_per_second/Cylinder_rod_side_area
print (f"Cylinder extention velocity : {Cylinder_extension_velocity} mm/s")
print (f"Cylinder retracion velocity : {Cylinder_retraction_velocity} mm/s")



