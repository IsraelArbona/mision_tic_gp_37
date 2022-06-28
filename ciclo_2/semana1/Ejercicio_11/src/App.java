import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner sc = new Scanner(System.in);

        int dia, mes, ano, numSuerte, sumaFecha, cf1, cf2, cf3, cf4;

        System.out.println("Por favor ingrese la fecha de nacimiento");
        System.out.print("día: " );
        dia = sc.nextInt();
        System.out.print("mes: ");
        mes = sc.nextInt();
        System.out.print("año: ");
        ano = sc.nextInt();

        sumaFecha = dia + mes + ano;

        cf1 = sumaFecha / 1000;         // Obtiene la primera cifra
        cf2 = sumaFecha / 100 % 10;     // Obtiene la segunda cifra
        cf3 = sumaFecha / 10 % 10;      // Obtener la tercera cifra
        cf4 = sumaFecha % 10;           // Obtener la cuarta cifra

        numSuerte = cf1 +cf2 + cf3 + cf4;

        System.out.println("Su número de la suerte es: " + numSuerte);

    }
}
