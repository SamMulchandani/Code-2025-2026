from nicegui import ui

def clear():
    a_input.value = ""
    b_input.value = ""
    c_input.value = ""

    a_slider.value = 0
    b_slider.value = 0
    c_slider.value = 0

def slider_on_change():
    a_input.value = a_slider.value
    b_input.value = b_slider.value
    c_input.value = c_slider.value
    
    a = a_input.value
    b = b_input.value
    c = c_input.value

    if a == 0:
        a_input.value = ""
    if b == 0:
        b_input.value = ""
    if c == 0:
        c_input.value = ""

def input_on_change():
    a_slider.value = a_input.value
    b_slider.value = b_input.value
    c_slider.value = c_input.value

def calculate():
    a = a_input.value
    b = b_input.value
    c = c_input.value

    # if((a != "" and a != "0") and (b != "" and b != "0") and (c!= "" and c != "0")):
    if(a != ""and b != "" and c!= ""):
        ui.notify("Please leave one entry box blank")
    elif(a == "" and b == "" and c == ""):
        ui.notify("Please enter values to two boxes")
    elif(a != "" and b == "" and c == ""):
        ui.notify("Please enter values to two boxes")
    elif(a == "" and b != "" and c == ""):
        ui.notify("Please enter values to two boxes")
    elif(a == "" and b == "" and c != ""):
        ui.notify("Please enter values to two boxes")

    elif(a != "" and b!= ""):
        c_input.value = (int(a)**2 + int(b)**2)**(1/2)
    elif(a != "" and c!= ""):
        b_input.value = (int(c)**2 - int(a)**2)**(1/2)
    elif(b != "" and c!= ""):
        a_input.value = (int(c)**2 - int(b)**2)**(1/2)

    a_slider.value = a_input.value
    b_slider.value = b_input.value
    c_slider.value = c_input.value

ui.html('<strong>Pythagorean Theorem Calculator</strong>', sanitize=False)

with ui.row():
    a_input = ui.input('Leg a', on_change=input_on_change)
    a_slider = ui.slider(min=0, max=50, value=0, on_change=slider_on_change)

with ui.row():
    b_input = ui.input('Leg b', on_change=input_on_change)
    b_slider = ui.slider(min=0, max=50, value=0, on_change=slider_on_change)

with ui.row():    
    c_input = ui.input('Hypoteneuse', on_change=input_on_change)
    c_slider = ui.slider(min=0, max=50, value=0, on_change=slider_on_change)

with ui.row():
    clear_button = ui.button("Clear", on_click=clear)
    calculate_button = ui.button('Calculate', on_click=calculate)

ui.run()