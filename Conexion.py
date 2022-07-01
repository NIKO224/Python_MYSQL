from tkinter import*
import mysql.connector

conexion = mysql.connector.connect(
    user='...', 
    password='...', 
    host='...', 
    database='pythonbd', 
    port='...'
    )

raiz = Tk()
raiz.title("Formulario")
raiz.configure(background="#666666")
cursor = conexion.cursor()
ingresar = "a"

#Funciones
def insertar ():
    global ingresar
    ingresar = "INSERT INTO persona(ID, Nombre, Apellido, Edad, Direccion, Celular) VALUES ('"+ textoID.get() + "', '" + texto_nom.get() + "', '" + texto_ap.get() + "', '" + texto_ed.get() + "', '" + texto_dir.get() + "', '" + texto_tel.get() + "')"
    cursor.execute(ingresar)
    conexion.commit()
    textoID.delete(0, 'end')
    texto_nom.delete(0, 'end')
    texto_ap.delete(0, 'end')
    texto_ed.delete(0, 'end')
    texto_dir.delete(0, 'end')
    texto_tel.delete(0, 'end')

def consultar ():
    global ingresar
    ingresar = "SELECT * FROM persona where id='" + textoID.get() + "';"
    cursor.execute(ingresar)
    resultado = cursor.fetchall() 
    for fila in resultado:
        texto_nom.insert(0, fila[1])
        texto_ap.insert(0, fila[2])
        texto_ed.insert(0, fila[3])
        texto_dir.insert(0, fila[4])
        texto_tel.insert(0, fila[5])
    conexion.commit()

def borrar ():
    textoID.delete(0,'end')
    texto_nom.delete(0,'end')
    texto_ap.delete(0,'end')
    texto_ed.delete(0,'end')
    texto_dir.delete(0,'end')
    texto_tel.delete(0,'end')

def modificar():
   # consultar()
    global ingresar
    ingresar = "UPDATE `pythonbd`.`persona` SET `Nombre` = '" + texto_nom.get() + "', `Apellido` = '" + texto_ap.get() + "', `Edad` = '" + texto_ed.get() + "', `Direccion` = '" + texto_dir.get() + "', `Celular` = '" + texto_tel.get() + "' WHERE (`ID` = '" + textoID.get() + "');"
    cursor.execute(ingresar)
#ID 
lblID = Label(raiz, text="CI", bg="#A4A4A4")
lblID.grid(row = 10, columnspan = 3, padx = 10, pady = 10)

textoID = Entry(raiz, font=("Calibri 12"), bg="#A4A4A4")
textoID.grid(row = 10, column = 40, columnspan = 3, padx = 5, pady = 10)

#Nombre
lbl_nom = Label(raiz, text="Nombre", bg="#A4A4A4")
lbl_nom.grid(row = 30, columnspan = 3, padx = 10, pady = 10)

texto_nom = Entry(raiz, font=("Calibri 12"), bg="#A4A4A4")
texto_nom.grid(row = 30, column = 40, columnspan = 3, padx = 5, pady = 10)

#Apellido
lbl_ap = Label(raiz, text="Apellido", bg="#A4A4A4")
lbl_ap.grid(row = 50, columnspan = 3, padx = 10, pady = 10)

texto_ap = Entry(raiz, font=("Calibri 12"), bg="#A4A4A4")
texto_ap.grid(row = 50, column = 40, columnspan = 3, padx = 5, pady = 10)

#Edad
lbl_ed = Label(raiz, text="Edad", bg="#A4A4A4")
lbl_ed.grid(row = 70, columnspan = 3, padx = 10, pady = 10)

texto_ed = Entry(raiz, font=("Calibri 12"), bg="#A4A4A4")
texto_ed.grid(row = 70, column = 40, columnspan = 3, padx = 5, pady = 10)

#Direccion
lbl_dir = Label(raiz, text="Dirección", bg="#A4A4A4")
lbl_dir.grid(row = 90, columnspan = 3, padx = 10, pady = 10)

texto_dir = Entry(raiz, font=("Calibri 12"), bg="#A4A4A4")
texto_dir.grid(row = 90, column = 40, columnspan = 3, padx = 5, pady = 10)

#Celular
lbl_tel = Label(raiz, text="Celular", bg="#A4A4A4")
lbl_tel.grid(row = 110, columnspan = 3, padx = 10, pady = 10)

texto_tel = Entry(raiz, font=("Calibri 12"), bg="#A4A4A4")
texto_tel.grid(row = 110, column = 40, columnspan = 3, padx = 10, pady = 10)

#botones
btn1 = Button(raiz, text = "Cargar", bg="#A4A4A4", width = 10, height = 2, command = lambda: insertar())
btn1.grid(row = 140, column = 40, padx = 10, pady = 15)

btn2 = Button(raiz, text = "Consultar CI", bg="#A4A4A4", width = 10, height = 2, command = lambda: consultar())
btn2.grid(row = 140, column = 41, padx = 10, pady = 15)

btn3 = Button(raiz, text = "Modificar", bg="#A4A4A4", width = 10, height = 2, command = lambda: modificar())
btn3.grid(row = 140, column = 42, padx = 10, pady = 15)

btn4 = Button(raiz, text = "Cancelar", bg="#A4A4A4", width = 10, height = 2, command = lambda: borrar())
btn4.grid(row = 140, column = 43, padx = 10, pady = 15)

raiz.mainloop()