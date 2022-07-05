package co.edu.utp.misiontic2022.c2;

public abstract class Figura {

    private String color;

    // constructor: define atributo "color" con la palabra reservada "this", haciendo las veces de setter (mutación)
    public Figura(String color){
        this.color = color;
    }

    // Método vacio para ser implementado desde las clases hijas.
    public abstract double calcularArea();

    // getter, para acceder al color
    public String getColor(){
        return color;
    }
    
}
