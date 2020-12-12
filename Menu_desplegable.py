import tkinter as tk

ventana = tk.Tk()
ventana.title("Lista desplegable") ##TITULO DE LA VENTANA


ventana.geometry('1000x600+600+100') ##POSICION DE LA VENTANA (ANCHO X ALTO, TAMAÑO x Y y)
ventana.configure(background='dark turquoise') ##Color del fondo

var=tk.StringVar(ventana)

var.set('Elije una opcion') ##AQUI LE PONGO LAS OPCIONES A EL DROPDOWN, ESTA ES LA PRIMERA QUE APARECERA

##AQUI LE PONGO LAS OPCIONES A EL DROPDOWN

opciones=['azul','Rosa','Amarillo','Verde','Blanco','Morado']

####################Dropdown::

opcion=tk.OptionMenu(ventana,var,*opciones) ##ESTO MOSTRARA Y CREARA MI VENTANA DESPLEGABLE, EN LOS PARENTESIS PONDRE EN DONDE QUIERO QUE ESTE, QUE VARIABLE Y LOS VALORES QUE QUIERA PONER
opcion.config(width=20) ##Este es el tamaño de mi dropdown
opcion.pack(side='left',padx=30,pady=30) ##Esto configura de que lado y los margenes del dropdown

####################ETIQUETAS:: Los labels y os campos

el=tk.Label(ventana,text="Color seleccionado:",bg="pink",fg="white") ##bg es color de bachground, fg es el color de las letras
el.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X) ##esto es para sus dimensiones del label

##AHORA EL CAMPO:
color=tk.Label(ventana,bg="plum",textvariable=var,padx=5,pady=5,width=50)
color.pack()


ventana.mainloop() ####ESTA LINEA SIEMPRE LA LLEVA AL FINAL DEL TKINDERF













