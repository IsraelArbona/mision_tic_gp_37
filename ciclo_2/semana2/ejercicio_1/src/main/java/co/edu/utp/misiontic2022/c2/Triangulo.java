package co.edu.utp.misiontic2022.c2;

public class Triangulo extends Figura {

    // Se define los atributos : base y altura
    private double base;
    private double altura;

    public Triangulo(String color, double base, double altura){
        // Toma de la clase abtracta "Figura" (super) el metodo contructor
        super(color);
        this.base = base;
        this.altura = altura;
    }

    @Override
    public double calcularArea() {
        // TODO Auto-generated method stub
        return ((base * altura) / 2);
    }
    
}
