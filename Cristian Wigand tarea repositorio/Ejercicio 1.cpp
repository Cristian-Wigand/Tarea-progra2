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
	scanf("%f",&n);	
    circulo pelota(n);
    
    printf("El area del circulo es: %f \nEl perimetro del circulo es: %f",pelota.calcularArea(),pelota.calcularPerimetro());
    pelota.cambiarRadio(5.0);
    printf("El nuevo valor del radio es: %f",pelota.radio);
    printf("El area del circulo es: %f \nEl perimetro del circulo es:%f",pelota.calcularArea(),pelota.calcularPerimetro());
	
	return 0;
}
