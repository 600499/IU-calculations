import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importing from Pillown
from datetime import datetime
import os
custom_font = ("Calibri", 15, "bold", "underline")
custom_font_1 = ("Calibri", 11, "bold")
custom_font_2 = ("Calibri", 13, "bold", "underline")

# Defining the event handling function
def combo_selction(event):
    selected_combo = event.widget  # Get the widget that triggered the event
    if selected_combo == combobox_for_Materialselection:
        style.configure("TCombobox2.TCombobox", fieldbackground="magenta", background="magenta")
        selected_combo.config(style="TCombobox2.TCombobox")
    elif selected_combo == combobox_for_no_of_Cylinders:
        style.configure("TCombobox2.TCombobox", fieldbackground="magenta", background="magenta")
        selected_combo.config(style="TCombobox2.TCombobox")      
#function for units inside frame 2
def units(num1):
    units_lable=ttk.Label(frame2, text=num1,font=custom_font_1,foreground="ghostwhite", background="dark blue")
    return units_lable
#function for units inside frame 3
def units_frame3(num1):
    units_lable_frame3=ttk.Label(frame3, text=num1,font=custom_font_1,foreground="ghostwhite", background="dark blue")
    return units_lable_frame3
# function for parameter inside frame2
def parameters_inside_frame2(num1):
    label_for_Cylinder_parameters=ttk.Label(frame2,text=num1,font=custom_font_1,foreground="ghostwhite", background="dark blue")
    return label_for_Cylinder_parameters
#function for parameters inside the frame 3
def parameters_inside_frame3(num2):
    label_for_IU_parameters=ttk.Label(frame3,text=num2,font=custom_font_1,foreground="ghostwhite", background="dark blue")
    return label_for_IU_parameters
#function for Spinbox inside the frame 3 
spinboxes = {}
def spinbox_inside_frame3(Name):
    spinbox_inside_frame3=tk.Spinbox(frame3, from_=0, to=250, background="blue", foreground="white",font=("calibre",10),width=10)
    spinboxes[Name]=spinbox_inside_frame3
    return spinbox_inside_frame3 
spinboxes = {}
def spinbox_inside_frame2 (Name):
    spinbox_inside_frame2=tk.Spinbox(frame2, from_=0, to=250, background="blue", foreground="white",font=("callibre", 10), width=10)
    spinboxes[Name]=spinbox_inside_frame2
    return spinbox_inside_frame2

Application = tk.Tk()
Application.title("IU specification calculation")
Application.geometry("1000x800+400+100")
Application.configure(background="Dark blue")
# Frame for input 
frame1 = tk.Frame(Application, highlightbackground="white", highlightthickness=1,background= "dark blue",width=960, height=100)
frame1.grid(row=2, column=0, padx=20, pady=0, columnspan=3)
# Prevent the frame from resizing to fit its children
frame1.grid_propagate(False)
# Frame for cylinder calculations
frame2 = tk.Frame(Application, highlightbackground="white", highlightthickness=1,background= "dark blue",width=380, height=440)
frame2.place(x=20,y=275)
# Prevent the frame from resizing to fit its children
frame2.grid_propagate(False)
# Frame for injection unit parameters
frame3 = tk.Frame(Application, highlightbackground="white", highlightthickness=1,background= "dark blue",width=380, height=440)
frame3.place(x=420,y=275)
# Prevent the frame from resizing to fit its children
frame3.grid_propagate(False)
# Frame for header
frame4 = tk.Frame(Application, highlightbackground="white", highlightthickness=1,background= "#7d7f9f",width=960, height=130)
frame4.grid(column=0,row=1,columnspan=5,pady=5)
# Prevent the frame from resizing to fit its children
frame4.grid_propagate(False)
# Frame for result
frame5 = tk.Frame(Application, highlightbackground="white", highlightthickness=1,background= "#7d7f9f",width=175, height=470)
frame5.place(x=807,y=245)
# Prevent the frame from resizing to fit its children
frame5.grid_propagate(False)

#function to displa current date and time
# Function to update date and time in the Entry widgets
def update_datetime():
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')
    date_entry.delete(0, tk.END)
    date_entry.insert(0, current_date)
    time_entry.delete(0, tk.END)
    time_entry.insert(0, current_time)
    # Call the function again after 1000 milliseconds (1 second)
    frame4.after(1000, update_datetime)
date_entry = tk.Entry(frame4, bg="black", font=('callibre', 11,),width=12,foreground="yellow")
date_entry.place(x=800, y=30)
time_entry = tk.Entry(frame4, bg="black", font=('callibre', 11,),width=12, foreground="yellow")
time_entry.place(x=800, y=60)
date_lable=ttk.Label(frame4, text="DATE",font=custom_font_1,background="#7d7f9f")
date_lable.place(x=750,y=30)
time_lable=ttk.Label(frame4, text="TIME",font=custom_font_1,background="#7d7f9f")
time_lable.place(x=750,y=60)
author=ttk.Label(frame4, text="PREPARED BY:ASK",font=custom_font_2,background="#7d7f9f")
author.place(x=750,y=100)

update_datetime()
# To chanage the column and row height and width
Application.columnconfigure(0, weight=0)
Application.columnconfigure(1, weight=0)
Application.columnconfigure(2, weight=0)
Application.columnconfigure(3, weight=0)
Application.columnconfigure(4, weight=0)
Application.rowconfigure(0, weight=0 )
Application.rowconfigure(1, weight=0)
Application.rowconfigure(2, weight=0)
Application.rowconfigure(3, weight=0)
# Load the shibaura machine image using PIL 
image_path = os.path.join(os.path.dirname(__file__), 'shibaura_new.png')
Shibaura_logo = Image.open(image_path)
Shibaura_logo = Shibaura_logo.resize((190, 70), Image.LANCZOS)  # Resize the image to 200x150 pixels
photo = ImageTk.PhotoImage(Shibaura_logo)
label_for_shibauralogo = tk.Label(frame4, image=photo)
label_for_shibauralogo.image = photo  # Keep a reference to avoid garbage collection
label_for_shibauralogo.place(x=30,y=40)
# Create a Combobox
Power_pack_values = ["11kW","22kW","30kW","37kW","45kW","55kW","75kW","90kW","110kW","135kW"]
IU_size_values = ["120IU","200IU","310IU","430IU","600IU","900IU","1400IU","2350IU","i19","i27","i39","i59","i110","i200"]
Material_selection = ["PVC","PP","GPPS","Low_Density_PE","RPVC","High_Density_PE","PC","PET"]
No_of_cylinders=["1","2"]
combobox_for_Power_pack = ttk.Combobox(frame1, values=Power_pack_values,width=10)
combobox_for_IU_size = ttk.Combobox(frame1, values=IU_size_values,width=10)
combobox_for_Materialselection = ttk.Combobox(frame1, values=Material_selection,width=12)
combobox_for_no_of_Cylinders = ttk.Combobox(frame2, values=No_of_cylinders,width=11)
combobox_for_Power_pack.place(x=240, y=10)
combobox_for_IU_size.place(x=240, y=40)
combobox_for_Materialselection.place(x=850, y=40)
combobox_for_no_of_Cylinders.place(x=200,y=20)
# Set default value 
combobox_for_Power_pack.current(3)
combobox_for_no_of_Cylinders.current(1)
# Customize appearance
style = ttk.Style()
style.theme_use('default')
combobox_for_Power_pack.bind("<<ComboboxSelected>>", combo_selction)
combobox_for_IU_size.bind("<<ComboboxSelected>>", combo_selction)
combobox_for_Materialselection.bind("<<ComboboxSelected>>", combo_selction)
combobox_for_no_of_Cylinders.bind("<<ComboboxSelected>>", combo_selction)
# code to create spin box
spinbox_for_injectionpressure=tk.Spinbox(frame1, from_=0, to=250, background="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_injectionpressure.place(x=550, y=40)   
spinbox_for_screwdiameter=tk.Spinbox(frame1, from_=0, to=250,bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_screwdiameter.place(x=550, y=10)   
spinbox_for_hydromotorCC=tk.Spinbox(frame1, from_=0, to=250,bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_hydromotorCC.place(x=850, y=10)
#spinbox inside frame2
spinbox_inside_frame2("spinbox_for_ratedflow").place(x=200,y=50)
spinbox_inside_frame2("spinbox_for_capdiameter").place(x=200,y=80)
spinbox_inside_frame2("spinbox_for_capside_area").place(x=200,y=110)
spinbox_inside_frame2("spinbox_for_roddiameter").place(x=200,y=140)
spinbox_inside_frame2("spinbox_for_rodside_area").place(x=200,y=170)
spinbox_inside_frame2("spinbox_for_arearatio").place(x=200,y=200)
spinbox_inside_frame2("spinbox_for_suckbackstroke").place(x=200,y=230)
spinbox_inside_frame2("spinbox_for_extension_veloity").place(x=200,y=260)
spinbox_inside_frame2("spinbox_for_retraction_velocity").place(x=200,y=290)
spinbox_inside_frame2("spinbox_for_Melt_correction_factor").place(x=200,y=320)
spinbox_inside_frame2("spinbox_for_injection_time").place(x=200,y=350)
spinbox_inside_frame2("spinbox_for_Dosing_time").place(x=200,y=380)
# Add a label widget
units("LPM").place(x=300, y=50)
units("mm").place(x=300, y=80)
units("mm\u00b2").place(x=300, y=110)
units("mm").place(x=300, y=140)
units("mm\u00b2").place(x=300, y=170)
units("mm").place(x=300, y=230)
units("mm/s").place(x=300, y=260)
units("mm/s").place(x=300, y=290)
units("gram/CC").place(x=300, y=320)
units("sec").place(x=300, y=350)
units("sec").place(x=300, y=380)

Title_lable = ttk.Label(frame4, text="IU SPECIFICATION CALCULATION SHEET",font=custom_font, foreground="black",background="#7d7f9f")
Title_lable.place(x=300,y=5)
Power_pack_lable = ttk.Label(frame1, text="SELECT THE MACHINE POWER PACK",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
Power_pack_lable.place(x=10, y=10)
IU_SIZE_lable = ttk.Label(frame1, text="SELECT THE INJECTION UNIT SIZE",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
IU_SIZE_lable.place(x=10, y=40)
Injectionpressure_lable = ttk.Label(frame1, text="ENTER INJECTION PRESSURE  [bar]",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
Injectionpressure_lable.place(x=330,y=40)
Screwdiameter_lable = ttk.Label(frame1, text="ENTER SCREW DIAMETER [mm]",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
Screwdiameter_lable.place(x=330,y=10)
hydromotorCC_lable = ttk.Label(frame1, text="ENTER THE HYDROMOTOR CC",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
hydromotorCC_lable.place(x=650,y=10)
Screwdiameter_lable = ttk.Label(frame1, text="SELECT THE MATERIAL",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
Screwdiameter_lable.place(x=650,y=40)
Actuator_parameters_label = ttk.Label(Application, text="INJECTION CYLINDER PARAMETERS",font=custom_font_2, foreground="Magenta", background=Application.cget("bg") )
Actuator_parameters_label.place(x=90,y=250)
IU_parameters_label = ttk.Label(Application, text="IU PARAMETERS",font=custom_font_2, foreground="Magenta", background=Application.cget("bg") )
IU_parameters_label.place(x=540,y=250) 

parameters_inside_frame2("NO OF CYLINDERS").place(x=20,y=20)
parameters_inside_frame2("RATED FLOW").place(x=20,y=50)
parameters_inside_frame2("CAP SIDE DIAMETER").place(x=20,y=80)
parameters_inside_frame2("CAP SIDE AREA").place(x=20,y=110)
parameters_inside_frame2("ROD SIDE DIAMETER").place(x=20,y=140)
parameters_inside_frame2("ROD SIDE AREA").place(x=20,y=170)
parameters_inside_frame2("AREA RATIO").place(x=20,y=200)
parameters_inside_frame2("SUCKBACK STROKE").place(x=20,y=230)
parameters_inside_frame2("EXTENSION VELOCITY").place(x=20,y=260)
parameters_inside_frame2("RETRACTION VELOCITY").place(x=20,y=290)
parameters_inside_frame2("MELT CORRECTION FACTOR").place(x=20,y=320)
parameters_inside_frame2("INJECTION TIME").place(x=20,y=350)
parameters_inside_frame2("DOSING TIME").place(x=20,y=380)
#label inside frame 3
parameters_inside_frame3("DOSING FLOW RATE").place(x=10, y=20)
parameters_inside_frame3("INJECTION FLOW RATE").place(x=10, y=50)
parameters_inside_frame3("SUCKBACK FLOW RATE").place(x=10, y=80)
parameters_inside_frame3("INJECTION VELOCITY").place(x=10, y=110)
parameters_inside_frame3("SUCK BACK VELOCITY").place(x=10, y=140)
parameters_inside_frame3("SCREW SPEED").place(x=10, y=170)
parameters_inside_frame3("INJECTION RATE").place(x=10, y=200)
parameters_inside_frame3("PLASTICIZING RATE").place(x=10, y=230)
parameters_inside_frame3("SHOT WEIGHT").place(x=10, y=260)
parameters_inside_frame3("SCREW PROJECTED AREA").place(x=10, y=290)
parameters_inside_frame3("CYLINDER HEAD VOLUME").place(x=10, y=320)
parameters_inside_frame3("INJECTION PRESSURE").place(x=10,y=350)
parameters_inside_frame3("INJECTION POWER").place(x=10, y=380)
parameters_inside_frame3("OVER LOAD FACTOR").place(x=10, y=410)
#spinbox inside frame 3
spinbox_inside_frame3("spinbox_for_dosign_flow_rate").place(x=200, y=20)
spinbox_inside_frame3("spinbox_for_injection_flow_rate").place(x=200, y=50)
spinbox_inside_frame3("spinbox_for_suckback_flow_rate").place(x=200, y=80)
spinbox_inside_frame3("spinbox_for_injection_velocity").place(x=200, y=110)
spinbox_inside_frame3("spinbox_for_suck_back_velocity").place(x=200, y=140)
spinbox_inside_frame3("spinbox for screw speed").place(x=200, y=170)
spinbox_inside_frame3("spinbox_for_injection_rate").place(x=200, y=200)
spinbox_inside_frame3("spinbox_for_plasticizing_rate").place(x=200, y=230)
spinbox_inside_frame3("spinbox_for_shot_weight").place(x=200, y=260)
spinbox_inside_frame3("spinbox_for_screw_projeced_area").place(x=200, y=290)
spinbox_inside_frame3("spinbox_for_cylinder_head_volume").place(x=200, y=320)
spinbox_inside_frame3("Spinbox_for_injection_pressure").place(x=200,y=350)
spinbox_inside_frame3("spinbox_for_injection_power").place(x=200, y=380)
spinbox_inside_frame3("spinbox_for_overload_factor").place(x=200, y=410)
#units inside frame 3
units_frame3("%").place(x=310,y=20)
units_frame3("%").place(x=310,y=50)
units_frame3("%").place(x=310,y=80)
units_frame3("mm/s").place(x=310,y=110)
units_frame3("mm/s").place(x=310,y=140)
units_frame3("rpm").place(x=310,y=170)
units_frame3("CC/s").place(x=310,y=200)
units_frame3("gram/s").place(x=310,y=230)
units_frame3("gram").place(x=310,y=260)
units_frame3("mm\u00b2").place(x=310,y=290)
units_frame3("mm\u00b3").place(x=310,y=320)
units_frame3("bar").place(x=310,y=350)
units_frame3("kW").place(x=310,y=380)
#sourse code
#event calling function for power pack selection
def flowrate_update (event):
    Power_pack=(combobox_for_Power_pack.get())
    Replaced_powerpack=int(Power_pack.replace("kW",""))
    if Replaced_powerpack==22:
        Flow_rate =101
    elif Replaced_powerpack == 30:
        Flow_rate =140
    elif Replaced_powerpack==37:
        Flow_rate=200
    elif Replaced_powerpack ==45:
        Flow_rate=240
    elif Replaced_powerpack==11:
        Flow_rate=65
    elif Replaced_powerpack==75:
        Flow_rate=400
    elif Replaced_powerpack==90:
        Flow_rate=480
    elif Replaced_powerpack==110:
        Flow_rate=600
    elif Replaced_powerpack==135:
        Flow_rate=720
    elif Replaced_powerpack==55:
        Flow_rate=300
    spinboxes["spinbox_for_ratedflow"].delete(0, tk.END)  # Clear the current value in the Spinbox
    spinboxes["spinbox_for_ratedflow"].insert(0, Flow_rate)  # Insert the new result into the Spinbox
    # code to change the color and update the text
    style.configure("TCombobox2.TCombobox", fieldbackground="magenta", background="magenta")
    combobox_for_Power_pack.config(style="TCombobox2.TCombobox")
    Power_pack_lable.config(text=f"{Power_pack} POWERPACK IS SELECTED")   
combobox_for_Power_pack.bind("<<ComboboxSelected>>", flowrate_update)
#event calling function for IU selection
def IU_selection (event):
    IU_size=combobox_for_IU_size.get()
    if IU_size == "600IU" :
        Cylinder_Cap_Diameter = 115
        Cylinder_Rod_Diameter = 55
        Cylinder_Stroke_length = 125
    elif IU_size == "900IU":
        Cylinder_Cap_Diameter = 130  
        Cylinder_Rod_Diameter = 60
        Cylinder_Stroke_length = 225
    elif IU_size == "1400IU":
        Cylinder_Cap_Diameter = 150
        Cylinder_Rod_Diameter = 75
        Cylinder_Stroke_length = 290
    elif IU_size == "2350IU":
        Cylinder_Cap_Diameter =  180 
        Cylinder_Rod_Diameter = 80
        Cylinder_Stroke_length = 325
    elif IU_size == "430IU" :
        Cylinder_Cap_Diameter = 107.5  
        Cylinder_Rod_Diameter = 55
        Cylinder_Stroke_length = 203
    elif IU_size == "120IU" :
        Cylinder_Cap_Diameter = 70 
        Cylinder_Rod_Diameter = 40
        Cylinder_Stroke_length = 125
    elif IU_size == "200IU" :
        Cylinder_Cap_Diameter = 85 
        Cylinder_Rod_Diameter = 50
        Cylinder_Stroke_length = 150
    elif IU_size == "310IU" :
        Cylinder_Cap_Diameter = 95 
        Cylinder_Rod_Diameter = 50
        Cylinder_Stroke_length = 175
    elif IU_size == "i19" :
        Cylinder_Cap_Diameter = 160  
        Cylinder_Rod_Diameter = 70
        Cylinder_Stroke_length = 330
    elif IU_size == "i27" :
        Cylinder_Cap_Diameter = 180  
        Cylinder_Rod_Diameter = 80
        Cylinder_Stroke_length = 325
    elif IU_size == "i39" :
        Cylinder_Cap_Diameter = 210  
        Cylinder_Rod_Diameter = 90
        Cylinder_Stroke_length = 425
    elif IU_size == "i59" :
        Cylinder_Cap_Diameter = 250 
        Cylinder_Rod_Diameter = 110
        Cylinder_Stroke_length = 445
    elif IU_size == "i110" :
        Cylinder_Cap_Diameter = 290  
        Cylinder_Rod_Diameter = 125
        Cylinder_Stroke_length = 632
    elif IU_size == "i200" :
        Cylinder_Cap_Diameter = 400 
        Cylinder_Rod_Diameter = 220
        Cylinder_Stroke_length = 770
    spinboxes["spinbox_for_capdiameter"].delete(0, tk.END) 
    spinboxes["spinbox_for_capdiameter"].insert(0, Cylinder_Cap_Diameter)
    spinboxes["spinbox_for_roddiameter"].delete(0, tk.END)
    spinboxes["spinbox_for_roddiameter"].insert(0, Cylinder_Rod_Diameter)
    spinboxes["spinbox_for_suckbackstroke"].delete(0,tk.END)
    spinboxes["spinbox_for_suckbackstroke"].insert(0,Cylinder_Stroke_length)
    style.configure("TCombobox2.TCombobox", fieldbackground="magenta", background="magenta")
    combobox_for_IU_size.config(style="TCombobox2.TCombobox")
    IU_SIZE_lable.config(text=f"{IU_size} IU IS SELECTED") 
combobox_for_IU_size.bind("<<ComboboxSelected>>",IU_selection)
# event calling function for melt correction factor
def Meltcorretion ():
    Material = combobox_for_Materialselection.get()
    if Material == "PP":
        Density = 0.89
    elif Material == "GPPS":
        Density = 1.04
    elif Material == "Low_Density_PE":
        Density = 0.91
    elif Material == "High_Density_PE":
        Density = 0.94
    elif Material == "PVC":
        Density = 1.16
    elif Material == "PC":
        Density = 1.2
    elif Material == "PET":
        Density = 1.35
    else:
        Density = 0  # Default if no match is found
    spinboxes["spinbox_for_Melt_correction_factor"].delete(0, tk.END)
    spinboxes["spinbox_for_Melt_correction_factor"].insert(0, Density)
    style.configure("TCombobox2.TCombobox", fieldbackground="magenta", background="magenta")
    combobox_for_Materialselection.config(style="TCombobox2.TCombobox")
combobox_for_Materialselection.bind("<<ComboboxSelected>>", lambda event: Meltcorretion())
import math 
def Cylinder_parameters():
    Cylinder_Cap_Diameter=int(spinboxes["spinbox_for_capdiameter"].get())
    Cylinder_Rod_Diameter=int(spinboxes["spinbox_for_roddiameter"].get())
    no_of_cylinders=int(combobox_for_no_of_Cylinders.get())
    Cylinder_cap_side_area = (math.pi/4*Cylinder_Cap_Diameter**2)*no_of_cylinders
    Cylinder_rod_side_area = (math.pi/4*((Cylinder_Cap_Diameter)**2-(Cylinder_Rod_Diameter)**2))*no_of_cylinders
    spinboxes["spinbox_for_capside_area"].delete(0,tk.END)
    spinboxes["spinbox_for_capside_area"].insert(0,round(Cylinder_cap_side_area,2))
    spinboxes["spinbox_for_rodside_area"].delete(0,tk.END)
    spinboxes["spinbox_for_rodside_area"].insert(0,round(Cylinder_rod_side_area,2))
    Flow_rate = int(spinboxes["spinbox_for_ratedflow"].get())
    Pump_Flow_rate_in_mm_cube_per_second =(Flow_rate*10**6)/60
    Cylinder_cap_side_area=float(spinboxes["spinbox_for_capside_area"].get())
    Cylinder_rod_side_area=float(spinboxes["spinbox_for_rodside_area"].get())
    Area_ratio=Cylinder_cap_side_area/Cylinder_rod_side_area
    spinboxes["spinbox_for_arearatio"].delete(0,tk.END)
    spinboxes["spinbox_for_arearatio"].insert(0,round(Area_ratio,2))
    Cylinder_extension_velocity = Pump_Flow_rate_in_mm_cube_per_second/Cylinder_cap_side_area
    Cylinder_retraction_velocity = Pump_Flow_rate_in_mm_cube_per_second/Cylinder_rod_side_area
    spinboxes["spinbox_for_extension_veloity"].delete(0,tk.END)
    spinboxes["spinbox_for_extension_veloity"].insert(0,round(Cylinder_extension_velocity,2))
    spinboxes["spinbox_for_retraction_velocity"].delete(0,tk.END)
    spinboxes["spinbox_for_retraction_velocity"].insert(0,round(Cylinder_retraction_velocity,2))
    Dosing_flow_percentage=float(spinboxes["spinbox_for_dosign_flow_rate"].get())/100
    #Flow_rate = int(spinboxes["spinbox_for_ratedflow"].get())
    Dosing_flow_rate=Dosing_flow_percentage*Flow_rate
    hydromotor_cc=int(spinbox_for_hydromotorCC.get())
    screw_speed=(Dosing_flow_rate/hydromotor_cc)*1000
    spinboxes["spinbox for screw speed"].delete(0,tk.END)
    spinboxes["spinbox for screw speed"].insert(0,round(screw_speed,2))
    Suckback_flow_percentage=float(spinboxes["spinbox_for_suckback_flow_rate"].get())/100
    Flow_rate = int(spinboxes["spinbox_for_ratedflow"].get())
    Suckback_flow_rate=Suckback_flow_percentage*Flow_rate
    Suckback_flow_rate_mm_s=(Suckback_flow_rate*10**6)/60
    Suck_back_velocity=(Suckback_flow_rate_mm_s/Cylinder_cap_side_area)
    spinboxes["spinbox_for_suck_back_velocity"].delete(0,tk.END)
    spinboxes["spinbox_for_suck_back_velocity"].insert(0,round(Suck_back_velocity,2)) 
    inject_flow_rate_percentage=float(spinboxes["spinbox_for_injection_flow_rate"].get())/100
    Injection_flow_rate=inject_flow_rate_percentage*Flow_rate
    Injection_flow_rate_in_mm_s=(Injection_flow_rate*10**6)/60  
    Injection_velocity=Injection_flow_rate_in_mm_s/Cylinder_rod_side_area
    spinboxes["spinbox_for_injection_velocity"].delete(0,tk.END)
    spinboxes["spinbox_for_injection_velocity"].insert(0,round(Injection_velocity,2))
    screw_diameter=float(spinbox_for_screwdiameter.get())
    screw_projected_area=math.pi/4*screw_diameter**2
    spinboxes["spinbox_for_screw_projeced_area"].delete(0,tk.END)
    spinboxes["spinbox_for_screw_projeced_area"].insert(0,round(screw_projected_area,2))
    cylinder_stroke_length=float(spinboxes["spinbox_for_suckbackstroke"].get())
    cylinder_head_volume=screw_projected_area*cylinder_stroke_length
    spinboxes["spinbox_for_cylinder_head_volume"].delete(0,tk.END)
    spinboxes["spinbox_for_cylinder_head_volume"].insert(0,round(cylinder_head_volume,2))
    injection_rate=screw_projected_area*Injection_velocity/1000
    spinboxes["spinbox_for_injection_rate"].delete(0,tk.END)
    spinboxes["spinbox_for_injection_rate"].insert(0,round(injection_rate,2))
    Density=float(spinboxes["spinbox_for_Melt_correction_factor"].get())
    shot_weight=Density*cylinder_head_volume/1000
    spinboxes["spinbox_for_shot_weight"].delete(0,tk.END)
    spinboxes["spinbox_for_shot_weight"].insert(0,round(shot_weight,2))
    injection_time=cylinder_stroke_length/Injection_velocity
    spinboxes["spinbox_for_injection_time"].delete(0,tk.END)
    spinboxes["spinbox_for_injection_time"].insert(0,round(injection_time,2))
    Plasticizing_rate=float(spinboxes["spinbox_for_plasticizing_rate"].get())
    Dosing_time=shot_weight/Plasticizing_rate
    spinboxes["spinbox_for_Dosing_time"].delete(0,tk.END)
    spinboxes["spinbox_for_Dosing_time"].insert(0,round(Dosing_time,2))
    Hydraulic_pressure=float(spinbox_for_injectionpressure.get())
    Injection_pressure=(Hydraulic_pressure*Cylinder_rod_side_area)/screw_projected_area
    spinboxes["Spinbox_for_injection_pressure"].delete(0,tk.END)
    spinboxes["Spinbox_for_injection_pressure"].insert(0,round(Injection_pressure, 2))
    Injection_power=(injection_rate*Injection_pressure)/10000
    spinboxes["spinbox_for_injection_power"].delete(0,tk.END)
    spinboxes["spinbox_for_injection_power"].insert(0,round(Injection_power,2))
    Power_pack=combobox_for_Power_pack.get()
    Replaced_power_pack=int(Power_pack.replace("kW", ""))
    Overload_factor=(Injection_power/Replaced_power_pack)
    spinboxes["spinbox_for_overload_factor"].delete(0,tk.END)
    spinboxes["spinbox_for_overload_factor"].insert(0, round(Overload_factor,2))

from PIL import ImageGrab
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import ImageGrab

def take_screenshot():
    # Get the coordinates of the Tkinter window
    x = Application.winfo_rootx()
    y = Application.winfo_rooty()
    width = x + Application.winfo_width()
    height = y + Application.winfo_height()

    # Take a screenshot of the window
    screenshot = ImageGrab.grab(bbox=(x, y, width, height))
    
    # Ask the user where to save the screenshot
    file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                                             title="Save Screenshot As")
    if file_path:  # If the user doesn't cancel the save dialog
        screenshot.save(file_path)
        messagebox.showinfo("Screenshot", f"Screenshot saved in: {file_path}")
    else:
        messagebox.showwarning("Screenshot", "Screenshot save canceled.")
print_button=ttk.Button(frame5,text="Print",width=15, command=take_screenshot)
print_button.place(x=35,y=120)

calculate_button=ttk.Button(frame5,text="Calculate",width=15, command=Cylinder_parameters)
calculate_button.place(x=35,y=70)
Application.mainloop()