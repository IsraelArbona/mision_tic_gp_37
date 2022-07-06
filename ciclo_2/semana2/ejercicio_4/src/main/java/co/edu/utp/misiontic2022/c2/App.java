package co.edu.utp.misiontic2022.c2;

/**
 * Array
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        /* 
            // declarar array
            int[] miArray;
            // inicializar el array
            miArray = new int[5];

            int[] intArray = {1,2,3,4,5,6,7,8,9};

            int[] miArray2 = new int[2];

            miArray2[0] = 10;
            miArray2[1] = 11;

            for(int i = 0; i < miArray2.length; i++){
                System.out.println(miArray2[i]);
            }

            System.out.println("");
            for(int i = 0; i < intArray.length; i++){
                System.out.println(intArray[i]);
            }

            int[][] matrizCuadrada = new int[3][3];
            int[][] matrizIrregular = new int[3][];

            matrizIrregular[0] = new int[3];
            matrizIrregular[1] = new int[20];
            matrizIrregular[2] = new int[2];

            matrizCuadrada[2][1] = 10;
            matrizIrregular[1][15] = 21;

            System.out.println("");
            System.out.println(matrizCuadrada[2][1]);
            System.out.println(matrizIrregular[1][15]);
        */

        ImpresoraTinta[] impresoraTintas = new ImpresoraTinta[3];

        impresoraTintas[0] = new ImpresoraTinta(10);
        impresoraTintas[1] = new ImpresoraTinta(20);
        impresoraTintas[2] = new ImpresoraTinta(30);

        for(int j = 0; j < impresoraTintas.length; j++){
            System.out.println("Velocidad : " + impresoraTintas[j].getVelocidad());
            System.out.println(impresoraTintas[j].toString());
        }

    }
}
