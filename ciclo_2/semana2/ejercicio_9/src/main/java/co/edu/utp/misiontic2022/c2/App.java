package co.edu.utp.misiontic2022.c2;

/**
 * Clase Genérica.
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        // Crear una referencia de Gen para Integers
        Gen<Integer> iOb;

        // Crear un objeto Gen<Integer> y asignamos su referencia a iOb
        iOb = new Gen<Integer>(37);

        // Mostrar el tipo de dato utilizado por iOb
        iOb.mostrarTipo();

        // Obtener el valor de iOb
        // Nos podemos fijar que no se necesita hacer conversión
        int v = iOb.getOb();
        System.out.println("Valor: " + v);

        //Crear un objeto de tipo string
        Gen<String> strOb = new Gen<String>("Prueba grupo_37");

        // Mostramos el tipo dato del strOb
        strOb.mostrarTipo();

        // Obtener el valor de strOb
        // nuevamente no se necesita hacer conversión
        String cadena = strOb.getOb();
        System.out.println("Cadena: " + strOb.getOb());

    }
}


// T es un parámetro de tipo que será reemplazado por un tipo real cuando se crea un objeto de tipo Gen.

class Gen<T> {

    // T es el parametro de tipo genérico
    T ob;

    // Pasar al constructor una referencia a un objeto de tipo T.
    Gen(T o){
        ob = o;
    }

    T getOb(){
        return ob;
    }

    // Muestra el tipo de T
    void mostrarTipo(){
        System.out.println("El tipo de T es: " + ob.getClass().getName());
    }

}
