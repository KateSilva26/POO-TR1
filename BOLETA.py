
class Boleta():
    def __init__(self):
        nombre = input("NOMBRE Y APELLIDO DEL TRABAJADOR :    ")
        ctg = input("CATEGORIA DEL TRABAJADOR         :    ")
        hrx = int(input("INGRESAR HORAS EXTRAS            :    "))
        tard = int(input("INGRESAR TARDANZA   (MINUTOS)    :    "))
        self.nombre = nombre
        self.cat = ctg
        self.hrx = hrx
        self.tar = tard
        self.sueldobasico = 0
        self.valorA = 0
        self.valorB = 0
        self.Adesc = 0
        self.Ahrx= 0
        self.Sneto = 0
        
    
    def nom_trab(self):
        print("- NOMBRE Y APELLIDO      :  ", self.nombre)
        
    def categoria(self):
        if self.cat == "A":
            self.sueldobasico = 3000
            print("- CATEGORIA              :  ", self.cat)
            print("- SUELDO BÁSICO          :  ", self.sueldobasico)
        if self.cat == "B":
            self.sueldobasico = 2500
            print("- CATEGORIA              :  ", self.cat)
            print("- SUELDO BÁSICO          :  ", self.sueldobasico)
        elif self.cat == "C":
            self.sueldobasico = 2000
            print("- CATEGORIA              :  ", self.cat)
            print("- SUELDO BÁSICO          :  ", self.sueldobasico)
        else:
            print("- CATEGORIA              :   CATEGORIA INCORRECTA")
            print("- SUELDO BÁSICO          :   NO HAY CATEGORIA")
            
    def Pph(self):
        self.valorA = self.sueldobasico/240
        self.Ahrx = self.valorA * self.hrx
        print("- PAGO POR HORAS EXTRAS  :  ", self.Ahrx)
        
    def DescuentoT(self):
        self.valorB = self.tar/60
        self.Adesc = self.valorB * self.valorA
        print("- DESCUENTO TARDANZAS    :  ", self.Adesc)
        
    def SueldoNeto(self):
        self.Sneto = (self.sueldobasico + self.Ahrx) - self.Adesc
        print("- SUELDO NETO            :  ", self.Sneto)
        
