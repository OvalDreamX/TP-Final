# Creo la base de datos y la tabla. Si ambas estan creadas, saltará un aviso
from tkinter import *
from tkinter.messagebox import *
import mysql.connector
from tkinter import ttk


veces = 0


class dbClass:
    def crear(self):
        try:
            self.mibase = mysql.connector.connect(
                host="localhost", user="root", passwd="")
            self.micursor = self.mibase.cursor()
            self.micursor.execute("CREATE DATABASE baseDeDatos1")

        except:
            showinfo("Advertencia", message="La Base de datos ya existe")

        try:
            self.mibase = mysql.connector.connect(
                host="localhost", user="root", passwd="", database="baseDeDatos1")
            self.micursor = self.mibase.cursor()
            self.micursor.execute(
                "CREATE TABLE tabla(id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL)")

        except:
            showinfo("Advertencia", message="La Tabla ya existe")
