import java.util.Scanner;

/* 
Programa que lea dos variables enteras N y m y le quite a N sus m ultimas cifras
Por Ejemplo, si N = 12345678 y m = 3 el nuevo valor de N es 12345 
 */

public class App {
    public static void main(String[] args) throws Exception {
        
        var sc = new Scanner(System.in);

        /* 
        int n;
        int m;
        int d;
        */

        int n, m ,d;

        System.out.print("Por favor ingrese el numero n: ");
        n = sc.nextInt();
        System.out.print("Por favor ingrese el numero m: ");
        m = sc.nextInt();

        d = (int)Math.pow(10,m);
        n = n/d;

        System.out.println("Número modificado " + n);
        
    }
}
