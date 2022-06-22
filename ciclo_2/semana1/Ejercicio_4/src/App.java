public class App {
    public static void main(String[] args) throws Exception {
        // Ciclo de for

        /*
         for (inicializacion; condicion; incremento) {
            instrucciones
         }
        */

        /* 
        for (int i = 0; i < 10; i++) {
            System.out.println("numero es: " + i);
        }
        */
        
        // Ciclo del while

        /* 
        var numero = 0;
        while (numero < 10){
            System.out.println("Numero while es: " + numero);
            numero++;
        }
        */

        // Ciclo de do while

        /* 
        var numero2 = 0;
        do {
            if ((numero2 >=100) && (numero2 <= 120)) {
                System.out.println("Número de do while es: " + numero2);
            }
            numero2++;
        } while (numero2 < 200);
        */

        var a = 5;
        var b = a++;

        System.out.println("El valor de a : " + a);
        System.out.println("El valor de b : " + b);

        var c = 5;
        var d = ++c;

        System.out.println("El valor de c : " + c);
        System.out.println("El valor de d : " + d);
    }
}
