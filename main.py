from tkinter import *
from tkinter.messagebox import *
import mysql.connector
from tkinter import ttk

import valid
import db
import re
import themes
import guardar
import eliminar
import actualizar


class Admin:
    ID = 0
    # Ventana Principal

    def __init__(self, window):
        self.master = window
        self.dataBase = db.dbClass()

        window.config(bg="darkblue")

        self.label0 = Label(self.master, text="Titulo")
        self.label0.grid(row=1, column=0, sticky=W)
        self.label1 = Label(self.master, text="Descripcion")
        self.label1.grid(row=2, column=0, sticky=W)
        self.label3 = Label(self.master, bg='indian red',
                            width=10, text="Ingrese sus datos")
        self.label3.grid(row=0, column=0, columnspan=4,
                         padx=1, pady=1, sticky=W+E)

        self.tit, self.desc = StringVar(), StringVar()

        self.e1 = Entry(self.master, textvariable=self.tit)
        self.e3 = Entry(self.master, textvariable=self.desc)
        self.e1.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)

        self.tree = ttk.Treeview(self.master)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=80, minwidth=80)
        self.tree.column("col2", width=80, minwidth=80)
        self.tree.column("col3", width=100, minwidth=100)

        self.scroll = ttk.Scrollbar(
            self.master, orient="vertical", command=self.tree.yview)
        self.scroll.grid(row=4, column=5, rowspan=1, sticky=NSEW)
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.tree.grid(row=4, column=0, columnspan=5, rowspan=1, sticky=NSEW)

        self.label4 = Label(self.master, text="Temas", borderwidth='3',
                            bg="darkblue", fg="white", font=(18), width=50)
        self.label4.grid(row=9, column=0, columnspan=3, sticky=EW)

        # Ventana y botones de temas
        self.windowTheme = Label(self.master, bg="blue", width=50)
        self.windowTheme.grid(row=10, column=0, columnspan=3, sticky=EW)

        self.themeSel = IntVar()

        self.option1 = Radiobutton(self.master, variable=self.themeSel, text="Tema 1", bg="blue", fg="white", value=1, command=lambda: themes.themesFunc(
            self.label0, self.label1, self.label3, self.master, self.themeSel.get()))
        self.option1.grid(row=10, column=0, columnspan=3, sticky=EW)

        self.option2 = Radiobutton(self.master, variable=self.themeSel, text="Tema 2", bg="blue", fg="white", value=2, command=lambda: themes.themesFunc(
            self.label0, self.label1, self.label3, self.master, self.themeSel.get()))
        self.option2.grid(row=11, column=0, columnspan=3, sticky=EW)

        self.option3 = Radiobutton(self.master, variable=self.themeSel, text="Tema 3", bg="blue", fg="white", value=3, command=lambda: themes.themesFunc(
            self.label0, self.label1, self.label3, self.master, self.themeSel.get()))
        self.option3.grid(row=12, column=0, columnspan=3, sticky=EW)

        # Conexion a base de datos
        def regiC(self):
            try:
                self.mibase = mysql.connector.connect(
                    host="localhost", user="master", passwd="", database="baseDeDatos1")
                self.micursor = self.mibase.cursor()
                self.micursor.execute("SELECT * FROM producto")
                self.base = self.micursor.fetchall()
                for row in base:
                    self.tree.insert(
                        '', 0, text=row[0], values=(row[1], row[2]))
            except:
                print('nope')
                return None

            regiC(self)

        # Toma de datos
        def tomarDatos():
            if valid.validar(self.tit.get()) == True:
                try:
                    self.mibase = mysql.connector.connect(
                        host="localhost", user="master", passwd="", database="baseDeDatos1")
                    self.micursor = self.mibase.cursor()
                    self.data = (self.tit.get(), self.desc.get())
                    self.micursor.execute(
                        "INSERT INTO tabla (titulo, descripcion) VALUES (%s, %s)", self.data)
                    self.mibase.commit()
                    print(self.micursor.rowcount, showinfo(
                        "Exito", message="Datos Guardados"))
                    fagregar(self)
                    clear(self)
                except:
                    showerror(
                        "Error", message="Error conectandose a base de Datos")
            else:
                clear(self)

    # Funciones llamables
        def fagregar(self):
            global ID
            self.ID += 1
            self.tree.insert("", "end", text=str(self.ID),
                             values=(self.e1.get(), self.e3.get()))

        # Funcion de limpieza de campos
        def clear(self): return self.tit.set(""), self.desc.set("")

        # Botones de interaccion con base de datos
        button1 = Button(self.master, text="Alta", command=tomarDatos)
        button1.grid(row=5, column=1)
        button3 = Button(self.master, text="Crear Base de Datos",
                         command=lambda: self.dataBase.crear())
        button3.grid(row=5, column=0)
        self.tree.grid(column=0, row=4, columnspan=4)


root = Tk()
root.title("Tarea POO")
app = Admin(root)
root.mainloop()
