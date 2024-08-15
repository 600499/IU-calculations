import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importing from Pillow
from datetime import datetime

custom_font = ("Calibri", 15, "bold", "underline")
custom_font_1 = ("Calibri", 11, "bold")
custom_font_2 = ("Calibri", 13, "bold", "underline")

# Defining the event handling function
def combo_selction(event):
    selected_combo = event.widget  # Get the widget that triggered the event
    selected_option = selected_combo.get()  # Get the selected option
    # Update the corresponding label based on the ComboBox that triggered the event
    if selected_combo == combobox_for_Power_pack:
        style.configure("TCombobox2.TCombobox", fieldbackground="magenta", background="magenta")
        selected_combo.config(style="TCombobox2.TCombobox")
        Power_pack_lable.config(text=f"{selected_option} Powerpack is selected")
    elif selected_combo == combobox_for_IU_size:
        IU_SIZE_lable.config(text=f"{selected_option} is selected")
        style.configure("TCombobox2.TCombobox", fieldbackground="magenta", background="magenta")
        selected_combo.config(style="TCombobox2.TCombobox")
    elif selected_combo == combobox_for_Materialselection:
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
#function for parameters inside the frame 3
def parameters_inside_label3(num2):
    label_for_IU_parameters=ttk.Label(frame3, text=num2,font=custom_font_1,foreground="ghostwhite", background="dark blue")
    return label_for_IU_parameters
#function for Spinbox inside the frame 3
def spinbox_inside_label3(num1):
    spinbox_inside_farame3=ttk.Spinbox(frame3, from_=0, to=250,foreground="ghostwhite",background="blue",font=("calibre",10),width=10)
    return spinbox_inside_farame3 

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
frame2 = tk.Frame(Application, highlightbackground="white", highlightthickness=1,background= "dark blue",width=380, height=420)
frame2.place(x=20,y=275)
# Prevent the frame from resizing to fit its children
frame2.grid_propagate(False)
# Frame for injection unit parameters
frame3 = tk.Frame(Application, highlightbackground="white", highlightthickness=1,background= "dark blue",width=380, height=420)
frame3.place(x=420,y=275)
# Prevent the frame from resizing to fit its children
frame3.grid_propagate(False)
# Frame for header
frame4 = tk.Frame(Application, highlightbackground="white", highlightthickness=1,background= "#7d7f9f",width=960, height=130)
frame4.grid(column=0,row=1,columnspan=5,pady=5)
# Prevent the frame from resizing to fit its children
frame4.grid_propagate(False)
# Frame for result
frame5 = tk.Frame(Application, highlightbackground="white", highlightthickness=1,background= "#7d7f9f",width=175, height=450)
frame5.place(x=807,y=245)
# Prevent the frame from resizing to fit its children
frame5.grid_propagate(False)

print_button=ttk.Button(frame5,text="Print",width=15)
print_button.place(x=35,y=120)

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
image_path = "D:\Hydraulics\Td Ts secification calulation\shibaura_new.png" 
Shibaura_logo = Image.open(image_path)
Shibaura_logo = Shibaura_logo.resize((300, 40), Image.LANCZOS)  # Resize the image to 200x150 pixels
photo = ImageTk.PhotoImage(Shibaura_logo)
label_for_shibauralogo = tk.Label(frame4, image=photo)
label_for_shibauralogo.image = photo  # Keep a reference to avoid garbage collection
label_for_shibauralogo.place(x=30,y=50)
# Create a Combobox
Power_pack_values = [11,22,30,37]
IU_size_values = ["430IU","600IU","900IU","1400IU","2350IU"]
Material_selection = ["PVC", "PP", "GPPS", "CPVC","RPVC"]
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
spinbox_for_ratedflow=tk.Spinbox(frame2, from_=0, to=250, bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_ratedflow.place(x=200,y=50)
spinbox_for_capdiameter=tk.Spinbox(frame2, from_=0, to=250, bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_capdiameter.place(x=200,y=80)
spinbox_for_capside_area=tk.Spinbox(frame2, from_=0, to=250, bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_capside_area.place(x=200,y=110)
spinbox_for_roddiameter=tk.Spinbox(frame2, from_=0, to=250, bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_roddiameter.place(x=200,y=140)
spinbox_for_rodside_area=tk.Spinbox(frame2, from_=0, to=250, bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_rodside_area.place(x=200,y=170)
spinbox_for_arearatio=tk.Spinbox(frame2, from_=0, to=250, bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_arearatio.place(x=200,y=200)
spinbox_for_suckbackstroke=tk.Spinbox(frame2, from_=0, to=250, bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_suckbackstroke.place(x=200,y=230)
spinbox_for_extension_veloity=tk.Spinbox(frame2, from_=0, to=250, bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_extension_veloity.place(x=200,y=260)
spinbox_for_retraction_velocity=tk.Spinbox(frame2, from_=0, to=250, bg="blue", fg="white",font=("calibre",10),width=10)
spinbox_for_retraction_velocity.place(x=200,y=290)


# Add a label widget

units("LPM").place(x=300, y=50)
units("mm").place(x=300, y=80)
units("mm\u00b2").place(x=300, y=110)
units("mm").place(x=300, y=140)
units("mm\u00b2").place(x=300, y=170)
units("mm").place(x=300, y=230)
units("mm\u00b2/s").place(x=300, y=260)
units("mm\u00b2/s").place(x=300, y=290)

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
Actuator_parameters_label.place(x=470,y=250)
IU_parameters_label = ttk.Label(Application, text="IU PARAMETERS",font=custom_font_2, foreground="Magenta", background=Application.cget("bg") )
IU_parameters_label.place(x=150,y=250) 

no_of_cylinders_lable = ttk.Label(frame2, text="NO OF CYLINDERS",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
no_of_cylinders_lable.place(x=20,y=20)
Rated_flow_lable = ttk.Label(frame2, text="RATED FLOW",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
Rated_flow_lable.place(x=20,y=50)
Cap_dia_lable = ttk.Label(frame2, text="CAP SIDE DIAMETER",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
Cap_dia_lable.place(x=20,y=80)
Cap_side_area_lable = ttk.Label(frame2, text="CAP SIDE AREA",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
Cap_side_area_lable.place(x=20,y=110)
Rod_Diameter_lable = ttk.Label(frame2, text="ROD SIDE DIAMETER",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
Rod_Diameter_lable.place(x=20,y=140)
Rod_side_area_lable = ttk.Label(frame2, text="ROD SIDE AREA",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg") )
Rod_side_area_lable.place(x=20,y=170)
Area_ratio_lable = ttk.Label(frame2, text="AREA RATIO",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg"))
Area_ratio_lable.place(x=20,y=200)
Suck_backstroke_lable = ttk.Label(frame2, text="SUCKBACK STROKE",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg"))
Suck_backstroke_lable.place(x=20,y=230)
cylinder_extension_velocity_lable = ttk.Label(frame2, text="EXTENSION VELOCITY",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg"))
cylinder_extension_velocity_lable .place(x=20,y=260)
cylinder_retraction_velocity_lable = ttk.Label(frame2, text="RETRACTION VELOCITY",font=custom_font_1, foreground="Ghostwhite", background=Application.cget("bg"))
cylinder_retraction_velocity_lable.place(x=20,y=290)
#label inside frame 3
parameters_inside_label3("DOSING FLOW RATE").place(x=10, y=20)
parameters_inside_label3("INJECTION FLOW RATE").place(x=10, y=50)
parameters_inside_label3("SUCKBACK FLOW RATE").place(x=10, y=80)
parameters_inside_label3("INJECTION VELOCITY").place(x=10, y=110)
parameters_inside_label3("SUCK BACK VELOCITY").place(x=10, y=140)
parameters_inside_label3("SCREW SPEED").place(x=10, y=170)
parameters_inside_label3("INJECTION RATE").place(x=10, y=200)
parameters_inside_label3("PLASTICIZING RATE").place(x=10, y=230)
parameters_inside_label3("SHOT WEIGHT").place(x=10, y=260)
parameters_inside_label3("SCREW PROJECTED AREA").place(x=10, y=290)
parameters_inside_label3("CYLINDER HEAD VOLUME").place(x=10, y=320)
parameters_inside_label3("INJECTION POWER").place(x=10, y=350)
parameters_inside_label3("OVER LOAD FACTOR").place(x=10, y=380)
#spinbox inside frame 3
spinbox_inside_label3("spinbox for dosign flow rate ").place(x=200, y=20)
spinbox_inside_label3("spinbox for injection flow rate ").place(x=200, y=50)
spinbox_inside_label3("spinbox for suckback flow rate ").place(x=200, y=80)
spinbox_inside_label3("spinbox for injection velocity ").place(x=200, y=110)
spinbox_inside_label3("spinbox for suck back velocity").place(x=200, y=140)
spinbox_inside_label3("spinbox for screw speed").place(x=200, y=170)
spinbox_inside_label3("spinbox for injection rate").place(x=200, y=200)
spinbox_inside_label3("spinbox for plasticizing rate ").place(x=200, y=230)
spinbox_inside_label3("spinbox for shot weight").place(x=200, y=260)
spinbox_inside_label3("spinbox for screw projected area").place(x=200, y=290)
spinbox_inside_label3("spinbox for cylinder head volume").place(x=200, y=320)
spinbox_inside_label3("spinbox for injection power").place(x=200, y=350)
spinbox_inside_label3("spinbox for overload factor").place(x=200, y=380)
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
units_frame3("kW").place(x=310,y=350)
#sourse code
#event calling function for power pack selection
def flowrate_update (event):
    Power_pack=int(combobox_for_Power_pack.get())
    if Power_pack==22:
        Flow_rate =100
    elif Power_pack == 30:
        Flow_rate =140
    elif Power_pack==37:
        Flow_rate=200
    elif Power_pack ==45:
        Flow_rate=240
    elif Power_pack==11:
        Flow_rate=65
    spinbox_for_ratedflow.delete(0, tk.END)  # Clear the current value in the Spinbox
    spinbox_for_ratedflow.insert(0, Flow_rate)  # Insert the new result into the Spinbox
    # code to change the color and update the text
    style.configure("TCombobox2.TCombobox", fieldbackground="magenta", background="magenta")
    combobox_for_Power_pack.config(style="TCombobox2.TCombobox")
    Power_pack_lable.config(text=f"{Power_pack} Powerpack is selected")   
combobox_for_Power_pack.bind("<<ComboboxSelected>>", flowrate_update)
#event calling function for IU selection
def IU_selection (event):
    IU_size=(combobox_for_IU_size.get())
    Replaced_IU_size=int(IU_size.replace("IU",""))
    if Replaced_IU_size == 600 :
        Cylinder_Cap_Diameter = 115
        Cylinder_Rod_Diameter = 55
        Cylinder_Stroke_length = 1250
    elif Replaced_IU_size == 900:
        Cylinder_Cap_Diameter = 130  
        Cylinder_Rod_Diameter = 60
        Cylinder_Stroke_length = 225
    elif Replaced_IU_size == 1400:
        Cylinder_Cap_Diameter = 150
        Cylinder_Rod_Diameter = 75
        Cylinder_Stroke_length = 290
    elif Replaced_IU_size == 2350:
        Cylinder_Cap_Diameter =  180 
        Cylinder_Rod_Diameter = 80
        Cylinder_Stroke_length = 325
    elif Replaced_IU_size == 430 :
        Cylinder_Cap_Diameter = 107.5  
        Cylinder_Rod_Diameter = 55
        Cylinder_Stroke_length = 203
    spinbox_for_capdiameter.delete(0, tk.END) 
    spinbox_for_capdiameter.insert(0, Cylinder_Cap_Diameter)
    spinbox_for_roddiameter.delete(0, tk.END)
    spinbox_for_roddiameter.insert(0, Cylinder_Rod_Diameter)
    spinbox_for_suckbackstroke.delete(0,tk.END)
    spinbox_for_suckbackstroke.insert(0,Cylinder_Stroke_length)
    style.configure("TCombobox2.TCombobox", fieldbackground="magenta", background="magenta")
    combobox_for_IU_size.config(style="TCombobox2.TCombobox")
    IU_SIZE_lable.config(text=f"{IU_size} IU is selected") 
combobox_for_IU_size.bind("<<ComboboxSelected>>",IU_selection)
import math 
def Cylinder_parameters():
    Cylinder_Cap_Diameter=int(spinbox_for_capdiameter.get())
    Cylinder_Rod_Diameter=int(spinbox_for_roddiameter.get())
    Cylinder_cap_side_area = (math.pi/4*Cylinder_Cap_Diameter**2)
    Cylinder_rod_side_area = (math.pi/4*(Cylinder_Cap_Diameter-Cylinder_Rod_Diameter)**2)
    spinbox_for_capside_area.delete(0,tk.END)
    spinbox_for_capside_area.insert(0,round(Cylinder_cap_side_area,2))
    spinbox_for_rodside_area.delete(0,tk.END)
    spinbox_for_rodside_area.insert(0,round(Cylinder_rod_side_area,2))
    Flow_rate = int(spinbox_for_ratedflow.get())
    Pump_Flow_rate_in_mm_cube_per_second =(Flow_rate*10**6)/60
    Cylinder_cap_side_area=float(spinbox_for_capside_area.get())
    Cylinder_rod_side_area=float(spinbox_for_rodside_area.get())
    Area_ratio=Cylinder_cap_side_area/Cylinder_rod_side_area
    spinbox_for_arearatio.delete(0,tk.END)
    spinbox_for_arearatio.insert(0,round(Area_ratio,2))
    Cylinder_extension_velocity = Pump_Flow_rate_in_mm_cube_per_second/Cylinder_cap_side_area
    Cylinder_retraction_velocity = Pump_Flow_rate_in_mm_cube_per_second/Cylinder_rod_side_area
    spinbox_for_extension_veloity.delete(0,tk.END)
    spinbox_for_extension_veloity.insert(0,round(Cylinder_extension_velocity,2))
    spinbox_for_retraction_velocity.delete(0,tk.END)
    spinbox_for_retraction_velocity.insert(0,round(Cylinder_retraction_velocity,2))




calculate_button=ttk.Button(frame5,text="Calculate",width=15, command=Cylinder_parameters)
calculate_button.place(x=35,y=70)
Application.mainloop()