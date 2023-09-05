#include<stdio.h>

class rectangulo{
	public:
		float longitud,ancho;
		rectangulo(float longitud1, float ancho1){
			if(longitud1==ancho1){
				printf("Es un cuadrado\n");
			}
			longitud=longitud1;
			ancho=ancho1;
		};
    	float calcularArea(){
	    	return ancho*longitud;
	    };
	    float calcularPerimetro(){
		    return (2*ancho) + (2*longitud);
	    };
        float cambiarLongitud(float longitud2){
        	longitud=longitud2;
			if(longitud==ancho){
				printf("Es un cuadrado\n");
			};
    	    return 0;
	    };
	    float cambiarAncho(float ancho2){
	    	ancho=ancho2;
			if(longitud==ancho){
				printf("Es un cuadrado\n");
			}
    	    return 0;
	    };
};

int main(){
	float n,m;
	printf("Ingresar longitud del rectangulo: ");
	scanf("%f",&n);	
    printf("Ingresar radio del circulo: ");
	scanf("%f",&m);	
    rectangulo caja(n,m);
    
    printf("El area del rectangulo es: %.2f \nEl perimetro del rectangulo es: %.2f\n\n",caja.calcularArea(),caja.calcularPerimetro());
    caja.cambiarAncho(2);
    caja.cambiarLongitud(2);
    printf("El nuevo valor del ancho es:%.2f y el nuevo valor de la longitud es: %.2f",caja.ancho,caja.longitud);
    printf("\nEl area del rectangulo es: %.2f \nEl perimetro del rectangulo es:%.2f",caja.calcularArea(),caja.calcularPerimetro());
	return 0;
}
