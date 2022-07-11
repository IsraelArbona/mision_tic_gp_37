package co.edu.utp.misiontic2022.c2;

public class PrecioTotal {

    private Double totalComputadores = 0.0;
    private Double totalComputadoresMesa = 0.0;
    private Double totalComputadoresPortatiles = 0.0;

    private Computadores[] lisComputadores;

    // Constructor
    public PrecioTotal(Computadores[] pComputadores){
        this.lisComputadores = pComputadores;
    }

    public void mostrarTotales(){
        for(int i = 0; i < lisComputadores.length; i++){
            if (lisComputadores[i] instanceof Computadores){
                totalComputadores += lisComputadores[i].calcularPrecio();
            }
            if (lisComputadores[i] instanceof ComputadoresMesa){
                totalComputadoresMesa += lisComputadores[i].calcularPrecio();
            }
            if (lisComputadores[i] instanceof ComputadoresPortatiles){
                totalComputadoresPortatiles += lisComputadores[i].calcularPrecio();
            }
        }

        // Mostramos los resultados 
        System.out.println("La suma del precio de los computadores es de " + totalComputadores);
        System.out.println("La suma del precio de los computadores de mesa es de " + totalComputadoresMesa);
        System.out.print("La suma del precio de los computadores portátiles es de " + totalComputadoresPortatiles);

    }

}
