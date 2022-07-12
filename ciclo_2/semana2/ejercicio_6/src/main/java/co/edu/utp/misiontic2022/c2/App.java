package co.edu.utp.misiontic2022.c2;

import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Conjunto set
 *
 */
public class App 
{
    private String colores[] = {"rojo","blanco","azul","verde","gris","blanco","gris","naranja"};

    public App(){
        List<String> lista = Arrays.asList(colores);
        System.out.printf("ArrayList %s \n", lista);
        imprimirSinDuplicar(lista);
    }

    private void imprimirSinDuplicar(Collection<String> coleccion){
        Set<String> conjunto = new HashSet<String>(coleccion);
        System.out.println("Los valores sin duplicados son: ");
        for (String string: conjunto){
            System.out.println(string);
        }
    }

    public static void main( String[] args )
    {
        
        Set<Integer> conjuntoEntero = new HashSet<>();

        conjuntoEntero.add(4);
        conjuntoEntero.add(5);
        conjuntoEntero.add(7);
        conjuntoEntero.add(4); // no se aceptan duplicados
        conjuntoEntero.add(2);

        /*
        for (Integer entero: conjuntoEntero){
            System.out.println("conjunto : " + entero);
        }
        */

        new App();

    }
}
