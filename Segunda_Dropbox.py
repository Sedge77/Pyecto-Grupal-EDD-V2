from tkinter import *
from tkinter import ttk ##Para combobox

root = Tk()
root.title('Menu de dropdowns!')
root.geometry("400x400") ##TAMAÑO DE LA VENTANA

options = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

##FUNCION PARA MOSTRAR LO CLICKEADO
def selected(event): ##EVENT ES PARA AGARRAR LO CLICKEADO, SIN PRESIONAR BOTON
    #myLabel = Label(root, text=clicked.get()).pack() ##Aqui el text es lo quen mostrara, y mostrara lo clickeado, y pack es para mostrar el label

    ##IFs dentro de mi funcion cuando selecciono algo
    if clicked.get() == 'Viernes':  ###
        myLabel = Label(root, text="Si Hoy es pinche viernes").pack() ##Este muestra un mensaje si es viernes
    else:
        myLabel = Label(root, text=clicked.get()).pack()  ##Este muestra lo seleccionado

def comboclick(event): 
    if myCombo.get() == 'Viernes':  ###
        myLabel = Label(root, text="Si Hoy es pinche viernes").pack() ##Este muestra un mensaje si es viernes
    else:
        myLabel = Label(root, text=myCombo.get()).pack()  ##Este muestra lo seleccionado
    



## Este es mi metodo para obtener lo clickeado
clicked = StringVar()##VARIABLE QUE OBTIENE LO CLICKEADO, la opcion
clicked.set(options[0]) ##ESTA ES LA OPCION QUE SE MUESTRA POR DEFAULT, LAS CASILLA 0 DE LA LISTA


##ESTE ES EL DROPDOWN MENU "Command puede llamar a una funcion", este es en forma de boton
drop = OptionMenu(root, clicked, *options,command=selected) ##ESTO MOSTRARA Y CREARA MI VENTANA DESPLEGABLE, EN LOS PARENTESIS PONDRE EN DONDE QUIERO QUE ESTE, QUE VARIABLE Y LOS VALORES QUE QUIERA PONER
drop.pack(pady=20) ##ESTO ES LO QUE MUESTRA MI DROPBOX


#####BOTON PARA SELECCIONA LO ESCOJIDO EN EL DROPDOWN MENU
#myButton = Button(root, text="select from list", command=selected) ##Al final se declara una funcion que esta mas arriba, ESTE BOTON ES PARA SELECCIONAR LO ELEJIDO EN EL DROPDOWN
#myButton.pack() ##MUSTRA mYbUTTON


##PARA COMBOBOX Este es otro tipo de Dropdown Menu pero sin ser boton
myCombo = ttk.Combobox(root,value=options)
myCombo.current(0) ##La opcion por defecto del combobox
myCombo.bind("<<ComboboxSelected>>",comboclick) ##Comboclick es una funcion que esta arriba
myCombo.pack() ##Para que salga




root.mainloop() ##SIEMPRE LLEVA ESTO