package co.edu.utp.misiontic2022.c2;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Listas
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        // var listaEnteros = new ArrayList<>();
        ArrayList <Integer> listaEnteros = new ArrayList<>();

        listaEnteros.add(5);
        listaEnteros.add(6);
        listaEnteros.add(7);
        listaEnteros.add(2,8);

        System.out.println("La longitud de la lista es de : " + listaEnteros.size());

        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese un numero a buscar ");
        int numBuscar = sc.nextInt();

        // listaEnteros.clear();
        System.out.println(listaEnteros.isEmpty());

        if (!listaEnteros.isEmpty()){

            if (listaEnteros.contains(numBuscar) == true){
                System.out.println(numBuscar + " Si esta");
            } else {
                System.out.println(numBuscar + " No esta");
            }

            System.out.println("Introduzca un número para devolver la posición: ");
            int numBuscar2 = sc.nextInt();

            for (Integer entero: listaEnteros){
                if (entero == numBuscar2){
                    System.out.println(numBuscar2 + " esta en la posición: " + listaEnteros.indexOf(numBuscar2));
                }
            }

            for (int i = 0; i <= listaEnteros.size(); i++){
                if (listaEnteros.get(i) == numBuscar2){
                    System.out.println(numBuscar2 + " esta en la posición: " + listaEnteros.indexOf(numBuscar2));
                    break;
                } else {
                    System.out.println(numBuscar2 + " no esta");
                    break;
                }
            }

        } else {
            System.out.println("La lista esta vicia.");
        }

        sc.close();

    }
}
