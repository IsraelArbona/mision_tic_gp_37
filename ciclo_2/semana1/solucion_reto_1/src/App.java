public class App {
    public static void main(String[] args) throws Exception {
        /*
         * BecaUniversitaria becaUniversitaria = new BecaUniversitaria();
         * 
         * System.out.println(becaUniversitaria.calcularInteresSimple());
         * System.out.println(becaUniversitaria.calcularInteresCompuesto());
         */

        /* 
        BecaUniversitaria becaUniversitaria = new BecaUniversitaria();
        System.out.println(becaUniversitaria.calcularInteresSimple());
        System.out.println(becaUniversitaria.calcularInteresCompuesto());
        System.out.println(becaUniversitaria.compararInversion(60, 13000, 1.4));
        */
    }
}

class BecaUniversitaria {

    // -------------------------------------
    // Atributos
    // -------------------------------------

    /**
     * valor del tiempo
     */
    private int tiempo;

    /**
     * valor de la Beca Universitaria
     */
    private double monto;

    /**
     * tasa de interés efectiva mensual del proyecto
     */
    private double interes;

    /**
     * Construye el proyecto valores por defecto
     */
    public BecaUniversitaria() {
        tiempo = 0;
        monto = 0;
        interes = 0;
    }

    public BecaUniversitaria(int pTiempo, double pMonto, double pInteres) {
        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;
    }

    /**
     * Retorna el interes simple, monto, en una cadena de texto.
     * 
     * @return el total de interes simple generado en número.
     */
    public double calcularInteresSimple() {
        double interesSimple = monto * (interes / 100) * tiempo;
        return Math.round(interesSimple);
    }

    /**
     * Retorna el interes compuesto, monto en una cadena de texto.
     * 
     * @return El total de interes compuesto generado en número.
     */
    public double calcularInteresCompuesto() {
        double interesCompuesto = monto * (Math.pow(1 + interes / 100, tiempo) - 1);
        return Math.round(interesCompuesto);
    }

    /**
     * Metodo para comparar la diferencia en el total de intereses generado para el
     * proyecto
     * 
     * @return respuesta al reto 1
     */
    public String compararInversion(int pTiempo, double pMonto, double pInteres) {
        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;

        // Cálculo de la diferencia entre tipos de tasas de interes.
        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();

        if (diferencia != 0) {
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        } else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }

    public String compararInversion() {
        double diferencia = 0;

        // Cálculo de la diferencia entre tipo de tasas
        diferencia = calcularInteresCompuesto() - calcularInteresSimple();

        // Revisar la diferencia obtenida
        if (diferencia != 0) {
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        } else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }

}
