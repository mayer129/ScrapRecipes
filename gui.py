from tkinter import *

rs_dict = { 
"wood_1": ["2 wood_scrap"], "wood_2": ["1.5 wood_1", ".1 metal_2"], "wood_3": ["1.5 wood_2", ".1 metal_3"], 
"metal_1": ["1.5 metal_scrap"], "metal_2": ["1.5 metal_1", ".1 ember", ".2 water"], "metal_3": ["2 metal_2", ".2 ember", ".4 water"],
"concrete_1": ["1 stone", ".4 water", ".2 chemical"], "concrete_2": ["1.5 concrete_1", ".2 metal_2"], "concrete_3": ["1.5 concrete_2", ".2 metal_3"],
"bearing": ["5 metal_scrap"], "switch": ["1 metal_scrap", "2 circuit_board"], "button": ["1 metal_scrap", "2 circuit_board"],
"sensor": ["1 metal_1", "1 glass", "2 circuit_board", "2 glue"], "sport_suspension_1": ["5 metal_2", "2 oil"], "piston_1": ["10 metal_2", "2 oil", "2 circuit_board", "1 component_kit"],
"gas_engine_1": ["20 metal_2", "5 oil", "5 circuit_board", "3 component_kit"], "electric_engine_1": ["20 metal_2", "5 battery", "10 circuit_board", "5 component_kit"],
"wheel": ["15 wood_1", "5 metal_1", "6 beeswax"], "big_wheel": ["40 wood_1", "10 metal_1", "8 beeswax"],
"driver_seat_1": ["10 cotton", "5 metal_1", "3 circuit_board", "1 component_kit"], "controller_1": ["5 metal_1", "5 circuit_board", "1 component_kit", "3 glue"],
"logic_gate": ["1 metal_1", "1 circuit_board", "1 glue"], "timer": ["2 metal_1", "2 circuit_board", "1 glue"],
"headlight": ["1 metal_1", "1 glass", "2 circuit_board", "1 glue"], 
"chest": ["40 metal_1", "2 glue"], "large_chest": ["60 metal_1", "5 circuit_board", "3 component_kit", "5 glue"], 
"vacuum_pump": ["10 metal_2", "5 beeswax", "5 circuit_board", "3 component_kit"],
"water_container": ["10 metal_1", "10 beeswax", "5 circuit_board", "2 glue"], "water_cannon": ["10 metal_2", "10 beeswax", "2 component_kit"]


}

use_dict = {}
OPTIONS = list(rs_dict.keys())


def list_contains(List1, List2):
    for m in List1.keys():
        for n in List2.keys():
            if m == n:
                return m
    return -1

def submit():
    use_dict[variable.get()] = e.get()
    text.insert(END, e.get() + " " + variable.get() + "\n")

def calculate():
    while (True):
        temp = list_contains(use_dict, rs_dict)
        if (temp != -1):
            tempVal = rs_dict.get(temp)
            tempNum = use_dict.get(temp)
            del use_dict[temp]
            for item in tempVal:
                tempList = item.split(" ")
                if tempList[1] in use_dict:
                    use_dict[tempList[1]] = round((float(tempList[0]) * float(tempNum)) + float(use_dict[tempList[1]]), 5)
                else:
                    use_dict[tempList[1]] = round(float(tempList[0]) * float(tempNum), 5)
        else:
            text.insert(END, "\n")
            text.insert(END, [(k, use_dict[k]) for k in use_dict])
            text.insert(END, "\n\n")
            break



master = Tk()

e = Entry(master)
e.grid(row = 0, column = 0)

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value
w = OptionMenu(master, variable, *OPTIONS)
w.grid(row = 0, column = 1)


buttonSubmit = Button(master, text="OK", command=submit)
buttonSubmit.grid(row = 1, column = 0)

buttonDone = Button(master, text="Done", command=calculate)
buttonDone.grid(row = 1, column = 1)

text = Text(master, height = 30, width = 60)
text.grid(row = 2, column = 0, columnspan = 2)


mainloop()