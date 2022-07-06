package co.edu.utp.misiontic2022.c2;

/**
 * Interfases
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        DeDos obj = new DeDos();

        for (int i = 0; i < 3; i++)
            System.out.println("El siguiente valor es: " + obj.getSiguiente());
            System.out.println("El valor anterior a " + obj.getSiguiente() + " es " + obj.getAnterior());
        
        System.out.println("\nReiniciando..");
        obj.reiniciar();

        for (int i = 0; i < 3; i++)
            System.out.println("El siguiente valor es: " + obj.getSiguiente());
            System.out.println("El valor anterior a " + obj.getSiguiente() + " es " + obj.getAnterior());
            System.out.println("\nIniciando en 100");
        
        obj.setComenzar(100);

        for (int i = 0; i < 3; i++)
            System.out.println("El siguiente valor es: " + obj.getSiguiente());
            System.out.println("El valor anterior a " + obj.getSiguiente() + " es " + obj.getAnterior());
        
    }
}
