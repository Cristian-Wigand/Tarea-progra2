#Ejercicio 2:

#Crea una clase Rectangulo.

#Define los atributos llamados longitud y ancho.

#Define los siguientes métodos:

#Define un método constructor el cual inicialice los valores de sus atributos.
#calcularArea() -> Este método retorna el área del rectángulo.
#calcularPerimetro() -> Este método retorna el perímetro del rectángulo.
#cambiarLongitud() -> Este método permite cambiar la longitud del rectángulo.
#cambiarAncho() -> Este método permite cambiar el ancho del rectángulo.
#Fuera de la clase, instancia un objeto de clase Rectangulo, asignándole los valores iniciales.

#Muestra por pantalla el área de ese rectángulo.

#Muestra por pantalla el perímetro de ese rectángulo.

class Rectangulo:
    # Atributo de clase
    numero_de_ruedas = 4

    # Constructor
    def __init__(self, longitud, ancho):
        # Atributos del objeto (también conocidos como atributos de instancia)
        if longitud == ancho:
            print("Es un cuadrado")
        self.longitud = longitud
        self.ancho = ancho

    # Métodos
    def calcularArea(self):
        return self.ancho*self.longitud
    def calcularPerimetro(self):
        return (2*self.ancho) + (2*self.longitud)
    def cambiarLongitud(self,longitud):
        self.longitud = longitud
        if self.longitud==self.ancho:
            print("Es un cuadrado")
    def cambiarAncho(self,ancho):
        self.ancho = ancho
        if self.longitud==self.ancho:
            print("Es un cuadrado")
        
long=float(input("Ingresar longitud del rectangulo:"))
anch=float(input("Ingresar ancho del rectangulo:"))

caja=Rectangulo(long,anch)
print("El area del rectangulo es:", caja.calcularArea(), "\nEl perimetro del rectangulo es:", caja.calcularPerimetro(),"\n")
caja.cambiarAncho(2)
caja.cambiarLongitud(2)
print("El area del rectangulo es:", caja.calcularArea(), "\nEl perimetro del rectangulo es:", caja.calcularPerimetro())