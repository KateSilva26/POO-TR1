
# TRABAJO FINAL - POO

# La empresa FERROTEK SAC se dedica a la producción de balones de gas. Cuenta con trabajadores de la categoría A, B y C. El sueldo de los trabajadores y el pago por hora extra está en función de su categoría:

#        CATEGORIA      |      SUELDO       |    PAGO POR HORAS
#                       |     BASICO(SB)    |     EXTRAS(PHX)
#            A          |    S/ 3000.00     |       PH x 4
#            B          |    S/ 2500.00     |       PH x 3
#            C          |    S/ 2000.00     |       PH x 2
# ---------------------------------------------------------------
#     Donde: PH (Pago por Hora) = (Sueldo Básico / 240 hrs.)
# ---------------------------------------------------------------






class Trabajador:
    def __init__(self):
        nombre = input("NOMBRE Y APELLIDO DEL TRABAJADOR :    ")
        ctg = input("CATEGORIA DEL TRABAJADOR         :    ")
        hrx = int(input("INGRESAR HORAS EXTRAS            :    "))
        tard = int(input("INGRESAR TARDANZA   (MINUTOS)    :    "))
        self.nombre = nombre
        self.cat = ctg
        self.hrx = hrx
        self.tar = tard
        
