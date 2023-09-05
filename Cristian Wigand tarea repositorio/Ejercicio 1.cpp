#include<stdio.h>

class circulo{
	public:
		float radio;
		circulo(float radio1){
			radio=radio1;
		};
    	float calcularArea(){
	    	return 3.14*(radio*radio);
	    };
	    float calcularPerimetro(){
		    return 6.28*radio;
	    };
        float cambiarRadio(float radio2){
    	    return radio=radio2;
	    };
};

int main(){
	float n;
	printf("Ingresar radio del circulo: ");
	scanf("%f",&n);	
    circulo pelota(n);
    
    printf("El area del circulo es: %.2f \nEl perimetro del circulo es: %.2f",pelota.calcularArea(),pelota.calcularPerimetro());
    pelota.cambiarRadio(5.0);
    printf("\nEl nuevo valor del radio es: %.2f",pelota.radio);
    printf("\nEl area del circulo es: %.2f \nEl perimetro del circulo es:%.2f",pelota.calcularArea(),pelota.calcularPerimetro());
	
	return 0;
}
