import re
from tkinter.messagebox import *

# Funcion de validacion


def validar(tit):
    patron = "^[A-Za-z]+(?: [_-][A-Za-z]+)*$"
    if bool(re.search(patron, tit))is False:
        showerror("Error", message="Ingreso no válido")
    else:
        return True
