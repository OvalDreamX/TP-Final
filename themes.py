# Funcion con variables para la seleccion de temas
def themesFunc(label0, label1, label3, window, themeSel):
    if themeSel == 1:
        window["bg"] = "dark orange"
        label0.config(bg="dark orange")
        label1.config(bg="dark orange")
        label3.config(bg="dark orange")
    elif themeSel == 2:
        window["bg"] = "green"
        label0.config(bg="green")
        label1.config(bg="green")
        label3.config(bg="green")
    else:
        window["bg"] = "blue"
        label0.config(bg="blue")
        label1.config(bg="blue")
        label3.config(bg="blue")
