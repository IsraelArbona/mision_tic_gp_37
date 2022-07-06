package co.edu.utp.misiontic2022.c2;

public class Cuadrado extends Figura {

    // Se define un atributo "lado"
    private double lado;

    // Constructor de la clase "Cuadradro"
    public Cuadrado(String color, double lado){
        // Tomamos de la clase abstracta "Figura" (super) el (metodo) constructor "color"
        super(color);
        this.lado = lado;
    }

    // Método que fue definido en la clase abstracta
    public double calcularArea(){
        return lado * lado;
    }

    
}
