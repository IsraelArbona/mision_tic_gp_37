package co.edu.utp.misiontic2022.c2;


/**
 * public: todos tienen acceso.
 * final: Unica clase sin subclase
 */

public final class MiPrimeraClase {

    // Atributos

    private static final Double PI = 3.1416;
    private Integer contador;
    private Integer numHoras;

    // Constructor

    public MiPrimeraClase(){
        this.contador = 0;
    }

    public MiPrimeraClase(Integer contador){
        this.contador = contador;

    } 

    public MiPrimeraClase(Integer contador, Integer numHoras){
        this.contador = contador;
        this.numHoras = numHoras;
    }

    // Métodos

    // método para incrementar el atributo contador
    public void incrementarContador(Integer contador){
        this.contador += contador;
    }

    // método nos permite visualizar el valor de atributo contador
    public Integer getContador(){
        return contador;
    }

    // método nos permite asignar el valor al atributo contador
    public void setContador(Integer valor){
        this.contador = valor;
    }

    public Integer getNumHoras() {
        return numHoras;
    }

    public void setNumHoras(Integer numHoras) {
        this.numHoras = numHoras;
    }

    Integer metodoEntero(){
        int suma = 10+10;
        return suma;
    }

}
