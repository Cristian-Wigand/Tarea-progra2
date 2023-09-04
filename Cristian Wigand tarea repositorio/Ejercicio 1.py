#Ejercicio 1:
#Crea una clase Circulo.
#Define un atributo llamado radio.
#Define los siguientes metodos:

#Define un metodo constructor el cual inicialice el valor del atributo llamado radio.
#calcularArea() -> Este metodo retorna el area del circulo.
#calcularPerimetro() -> Este metodo retorna el perimetro del circulo.
#cambiarRadio() -> Este metodo permite cambiar el radio del circulo.
#Fuera de la clase, instancia un objeto de clase Circulo, asignandole un radio inicial.

#Muestra por pantalla el area de ese circulo.
#Muestra por pantalla el perimetro de ese circulo.

class Circulo:

    # Constructor
    def __init__(self, radio):
        # Atributos del objeto (tambien conocidos como atributos de instancia)
        self.radio = radio

    # Metodo
    def calcularArea(self):
        return 3.14*(self.radio**2)
    def calcularPerimetro(self):
        return 6.28*self.radio
    def cambiarRadio(self,radio):
        self.radio=radio

aux=float(input("Ingresar radio del circulo:"))
    
pelota = Circulo(aux)
print("El area del circulo es: ",pelota.calcularArea(),"\nEl perimetro del circulo es:",pelota.calcularPerimetro())
pelota.cambiarRadio(5)
print("El nuevo valor del radio es:",pelota.radio)
print("El area del circulo es: ",pelota.calcularArea(),"\nEl perimetro del circulo es:",pelota.calcularPerimetro())