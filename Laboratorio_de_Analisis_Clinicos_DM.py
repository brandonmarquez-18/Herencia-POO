#-*-coding:utf-8-*-
try:
    #Intentar importar toda la librería de TKinder
    from Tkinter import *
except:
    from tkinter import *
#Tkinter es el paquete(Librería) más utilizado para crear interfaces gráficas en Python.
#Es una capa orientada a objetos basada en Tcl (sencillo y versátil lenguaje de programación open-source)
#y Tk (la herramienta GUI estándar para Tcl).

ventana = Tk() #Creando una instancia
ventana.title("Laboratorio de Análisis Clínicos DM")#TIULO DE LA VENTANA
ventana.geometry("1366x768")#TAMAÑO DE LA VENTANA
#INDICA QUE SI SE PUEDA INDICAR LAS DIMENSIONES
ventana.resizable(1, 1)#INDICA SI S PUEDE MODIFICAR LA VENTANA O NO

#CREANDO LA CLASE MADRE QUE HEREDARA PROPIEDADES A SUBCLASES
class Padre:
    def __init__(self):#CONSTRUCTOR
        self.titulo="Laboratorio de Análisis Clínicos DM"

    #METODO DONDE SE DEFINEN PROPIEDADES AHEREDAR
    def pedir_datos(self):
        self._glucosa = IntVar()
        self._acido = IntVar()
        self._colesterol = IntVar()
        self._urea = IntVar()
        self._trigliceridos = IntVar()
        self._creatinina = IntVar()

        #OBJETOS A HEREDAR
        self.ventana = Toplevel(ventana)
        self.ventana.title = ("Laboratorio de Análisis Clínicos DM")
        self.ventana.geometry("1366x768")
        Label(self.ventana, text = "Elíga en unidades el estudio que desea convertír de mmol/L a mg/dL:", font = ("Arial", 24), fg="red").place(x=200, y=10)

        #OBJETOS VISUALES PARA GLUCOSA
        Label(self.ventana, text = "Glucosa: ", font = ("Arial", 24), fg="blue").place(x=20, y=100)
        Entry(self.ventana, textvariable = self._glucosa, font = ("Arial", 16), width = 10).place(x=150 , y=100)
        Button(self.ventana, text = "Convertir", font = ("Arial", 16), width = 10, height = 1, fg = "blue", command = self.convertirGlucosa).place(x = 280, y = 100)

        #OBJETOS VISUALES PARA EL ACIDO URICO
        Label(self.ventana, text = "Ácido úrico: ", font = ("Arial", 24), fg="blue").place(x=20, y=200)
        Entry(self.ventana, textvariable = self._acido, font = ("Arial", 16), width = 10).place(x=200 , y=200)
        Button(self.ventana, text = "Convertir", font = ("Arial", 16), width = 10, height = 1, fg = "blue", command = self.convertirAcido).place(x = 330, y = 200)

        #OBJETOS VISUALES PARA COLESTEROL
        Label(self.ventana, text = "Colesterol: ", font = ("Arial", 24), fg="blue").place(x=20, y=300)
        Entry(self.ventana, textvariable = self._colesterol, font = ("Arial", 16), width = 10).place(x=200 , y=300)
        Button(self.ventana, text = "Convertir", font = ("Arial", 16), width = 10, height = 1, fg = "blue", command = self.convertirColesterol).place(x = 330, y = 300)

    def p(self):
        self._glucosa = IntVar()
        self._acido = IntVar()
        self._colesterol = IntVar()
        self._urea = IntVar()
        self._trigliceridos = IntVar()
        self._creatinina = IntVar()
        self.ventana = Toplevel(ventana)
        self.ventana.title = ("Laboratorio de Análisis Clínicos DM")
        self.ventana.geometry("1366x768")
        Label(self.ventana, text = "Elíga en unidades el estudio que desea convertír de mmol/L a mg/dL:", font = ("Arial", 24), fg="red").place(x=200, y=10)

        Label(self.ventana, text = "Glucosa: ", font = ("Arial", 24), fg="blue").place(x=20, y=100)
        Entry(self.ventana, textvariable = self._glucosa, font = ("Arial", 16), width = 10).place(x=150 , y=100)
        Button(self.ventana, text = "Convertir", font = ("Arial", 16), width = 10, height = 1, fg = "blue", command = self.convertirGlucosa).place(x = 280, y = 100)

        Label(self.ventana, text = "Ácido úrico: ", font = ("Arial", 24), fg="blue").place(x=20, y=200)
        Entry(self.ventana, textvariable = self._acido, font = ("Arial", 16), width = 10).place(x=200 , y=200)
        Button(self.ventana, text = "Convertir", font = ("Arial", 16), width = 10, height = 1, fg = "blue", command = self.convertirAcido).place(x = 330, y = 200)

        Label(self.ventana, text = "Colesterol: ", font = ("Arial", 24), fg="blue").place(x=20, y=300)
        Entry(self.ventana, textvariable = self._colesterol, font = ("Arial", 16), width = 10).place(x=200 , y=300)
        Button(self.ventana, text = "Convertir", font = ("Arial", 16), width = 10, height = 1, fg = "blue", command = self.convertirColesterol).place(x = 330, y = 300)

        #OBJETOS VISUALES PARA UREA
        Label(self.ventana, text = "Urea: ", font = ("Arial", 24), fg="blue").place(x=20, y=400)
        Entry(self.ventana, textvariable = self._urea, font = ("Arial", 16), width = 10).place(x=200 , y=400)
        Button(self.ventana, text = "Convertir", font = ("Arial", 16), width = 10, height = 1, fg = "blue", command = self.convertirUrea).place(x = 330, y = 400)

        #OBJETOS VISUALES PARA TRIGLICERIDOS
        Label(self.ventana, text = "Trigliceridos: ", font = ("Arial", 24), fg="blue").place(x=20, y=500)
        Entry(self.ventana, textvariable = self._trigliceridos, font = ("Arial", 16), width = 10).place(x=250 , y=500)
        Button(self.ventana, text = "Convertir", font = ("Arial", 16), width = 10, height = 1, fg = "blue", command = self.convertirTrigliceridos).place(x = 330, y = 500)

        #OBJETOS VISUALES PARA CREATININA
        Label(self.ventana, text = "Creatinina: ", font = ("Arial", 24), fg="blue").place(x=20, y=600)
        Entry(self.ventana, textvariable = self._creatinina, font = ("Arial", 16), width = 10).place(x=250 , y=600)
        Button(self.ventana, text = "Convertir", font = ("Arial", 16), width = 10, height = 1, fg = "blue", command = self.convertirCreatinina).place(x = 330, y = 600)


#CREANDO CLASE DE LA QUIMICA SANGUINEA 3 DICIENDOLE QUE VA HEREDAR LAS PROPIEDADES Y OBJETOS VISUALES
#DE LA CLASE PADRE
class Qst(Padre):
    #CONSTRUCTOR CON PROPIEDAES A HEREDAR
    def __init__(self, titulo):
        self.titulo=titulo#SIRVE PARA DESPUES CAMBIAR EL TITULO EN VENTANA
        self._glucosa = IntVar()
        self._acido = IntVar()
        self._colesterol = IntVar()

    #MÉTODOS
    def convertirGlucosa(self):
        #CONVERSIÓN DE mmol/L a mg/dL
        Label(self.ventana, text = str(self._glucosa.get() * 18.02), font = ("Arial", 20),fg="blue").place(x=450, y=100)
        Label(self.ventana, text = " mg/dL", font = ("Arial", 20), fg="brown").place(x=600, y=100)
    def convertirAcido(self):
        #CONVERSIÓN DE mmol/L a mg/dL
        Label(self.ventana, text = str(self._acido.get() * 0.02), font = ("Arial", 20),fg="blue").place(x=500, y=200)
        Label(self.ventana, text = " mg/dL", font = ("Arial", 20), fg="brown").place(x=600, y=200)
    def convertirColesterol(self):
        #CONVERSIÓN DE mmol/L a mg/dL
        Label(self.ventana, text = str(self._colesterol.get() * 380.66), font = ("Arial", 20),fg="blue").place(x=500, y=300)
        Label(self.ventana, text = " mg/dL", font = ("Arial", 20), fg="brown").place(x=600, y=300)

#CREANDO CLASE DE LA QUIMICA SANGUINEA 6 DICIENDOLE QUE VA HEREDAR LAS PROPIEDADES Y OBJETOS VISUALES
#DE LA CLASE PADRE
class Qss(Padre):
    #CONSTRUCTOR CON PROPIEDAES A HEREDAR
    def __init__(self, titulo):
        self.titulo=titulo#SIRVE PARA DESPUES CAMBIAR EL TITULO EN VENTANA
        self._glucosa = IntVar()
        self._acido = IntVar()
        self._colesterol = IntVar()
        self._urea = IntVar()
        self._trigliceridos = IntVar()
        self._creatinina = IntVar()
    #MÉTODOS
    def convertirGlucosa(self):
        #CONVERSIÓN DE mmol/L a mg/dL
        Label(self.ventana, text = str(self._glucosa.get() * 18.02), font = ("Arial", 20),fg="blue").place(x=450, y=100)
        Label(self.ventana, text = " mg/dL", font = ("Arial", 20), fg="brown").place(x=600, y=100)
    def convertirAcido(self):
        #CONVERSIÓN DE mmol/L a mg/dL
        Label(self.ventana, text = str(self._acido.get() * 0.02), font = ("Arial", 20),fg="blue").place(x=500, y=200)
        Label(self.ventana, text = " mg/dL", font = ("Arial", 20), fg="brown").place(x=600, y=200)
    def convertirColesterol(self):
        #CONVERSIÓN DE mmol/L a mg/dL
        Label(self.ventana, text = str(self._colesterol.get() * 380.66), font = ("Arial", 20),fg="blue").place(x=500, y=300)
        Label(self.ventana, text = " mg/dL", font = ("Arial", 20), fg="brown").place(x=600, y=300)
    def convertirUrea(self):
        #CONVERSIÓN DE mmol/L a mg/dL
        Label(self.ventana, text = str(self._urea.get() * 6.01), font = ("Arial", 20),fg="blue").place(x=500, y=400)
        Label(self.ventana, text = " mg/dL", font = ("Arial", 20), fg="brown").place(x=600, y=400)
    def convertirTrigliceridos(self):
        #CONVERSIÓN DE mmol/L a mg/dL
        Label(self.ventana, text = str(self._trigliceridos.get() * 87.5), font = ("Arial", 20),fg="blue").place(x=500, y=500)
        Label(self.ventana, text = " mg/dL", font = ("Arial", 20), fg="brown").place(x=600, y=500)
    def convertirCreatinina(self):
        #CONVERSIÓN DE mmol/L a mg/dL
        Label(self.ventana, text = str(self._creatinina.get() * 0.01), font = ("Arial", 20),fg="blue").place(x=500, y=600)
        Label(self.ventana, text = " mg/dL", font = ("Arial", 20), fg="brown").place(x=600, y=600)


#CREANDO INTANCIAS Y ASIGNANDO UN NUEVO TITULO A CADA TIPO DE ESTUDIO
Qst = Qst("Química Sanguínea 3")
Qss = Qss("Química Sanguínea 6")

#OBJETOS VISUALES DEL MENU PRINCIPAL Y HACIENDO REFERENCIA CON "command" HACIA EL METODO A ACCEDER
Label(ventana, text = "Laboratorio de Análisis Clínicos DM", font = ("Arial", 30), fg="red").place(x=100, y=50)
Button(ventana, text = "Química Sanguínea 3", font = ("Arial", 16), width = 20, height = 2,fg = "brown", command = Qst.pedir_datos).place(x=100, y=150)
Button(ventana, text = "Química Sanguínea 6", font = ("Arial", 16), width = 20, height = 2,fg = "brown", command = Qss.p).place(x=100, y=250)
#Genera un ciclo infinito para que no se rompa el programa
mainloop()
