package co.edu.utp.misiontic2022.c2;

/**
 * Enum
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        // System.out.println(Color.Blanco);

        Transporte tp;
        tp = Transporte.TREN;
        
        /* 
            System.out.println("Valor de tp: " + tp);

            if (tp == Transporte.BARCO)
                System.out.println("tp tiene el valor de BARCO");
            else 
                System.out.println("tp tiene el valor de: " + tp);
        */
        
        switch(tp){
            case COCHE:
                System.out.println("Respuesta de un COCHE.");
                break;
            case CAMION:
                System.out.println("Respuesta de un CAMION.");
                break;
            case AVION:
                System.out.println("Respuesta de un AVION.");
                break;
            case TREN:
                System.out.println("Respuesta de un TREN.");
                break;
            default:
                System.out.println("Respuesta el BARCO.");
        }
    }
}
