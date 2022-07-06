package co.edu.utp.misiontic2022.c2;

import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        /* 
            MiPrimeraClase mpc = new MiPrimeraClase();
            MiPrimeraClase mpc2 = new MiPrimeraClase(50);
            MiPrimeraClase mpc3 = new MiPrimeraClase(10,20);

            mpc.incrementarContador(5);
            System.out.println("Valor atributo contador : " + mpc.getContador());
            mpc.setContador(20);
            System.out.println("Valor del atributo : " + mpc.getContador());

            System.out.println("mpc2 atributo : " + mpc2.getContador());
            mpc2.incrementarContador(50);
            System.out.println("mpc2 atributo : " + mpc2.getContador());

            System.out.println("mpc3 atributo : " + mpc3.getContador());
            System.out.println("mpc3 atributo numero horas : " + mpc3.getNumHoras());
        */

        /* 

            // declarar variables

            String colorTriangulo;
            double baseTriangulo;
            double alturaTriangulo;

            // Se instancia la clase Scanner
            var sc = new Scanner(System.in);

            System.out.print("Introduzca el color del triángulo: ");
            colorTriangulo = sc.nextLine();
            System.out.print("Introduzca la base del triángulo: ");
            baseTriangulo = sc.nextDouble();
            System.out.print("Introduzca la altura del triángulo: ");
            alturaTriangulo = sc.nextDouble();

            Triangulo triangulo = new Triangulo(colorTriangulo, baseTriangulo, alturaTriangulo);
            System.out.printf("El área del triángulo %s es: %f", triangulo.getColor(),triangulo.calcularArea());
            sc.close();

        */

        // declarar variables

        String colorCuadrado;
        double ladoCuadrado;

        // Se instancia la clase Scanner
        Scanner sc = new Scanner(System.in);

        System.out.print("Introduzca el color del cuadrado: ");
        colorCuadrado = sc.nextLine();
        System.out.print("Introduzca el lado del cuadrado: ");
        ladoCuadrado = sc.nextDouble();

        Cuadrado cuadrado = new Cuadrado(colorCuadrado, ladoCuadrado);
        System.out.printf("El área del cuadrado %s es: %f", cuadrado.getColor(),cuadrado.calcularArea());
        sc.close();
        
    }
}
