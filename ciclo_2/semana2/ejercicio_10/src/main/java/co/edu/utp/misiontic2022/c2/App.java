package co.edu.utp.misiontic2022.c2;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Excepcion
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        /*
            int[] array = new int[20];
            try {
                array[0] = 10;
                int b = 0;
                int a = 23/b;     
            } catch (ArrayIndexOutOfBoundsException | ArithmeticException ex) {
                //TODO: handle exception
                System.out.println("Error de Indice en el array o división por 0");
            }
        */

        Scanner sc = new Scanner(System.in);
        int numero;

        try {
            System.out.println("Ingrese un valor entero: ");
            numero = sc.nextInt();
            int cuadrado = numero * numero;
            System.out.println("El cuadrado de " + numero + " es : " + cuadrado);
        } catch (InputMismatchException e) {
            System.out.println("Debe ingresar un número entero");
        }
    }
}
