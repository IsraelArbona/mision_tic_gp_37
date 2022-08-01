package co.edu.utp.misiontic2022.c2;

import static java.nio.file.StandardOpenOption.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class App 
{
    public static void main( String[] args )
    {

        /* 
        File f = new File("prueba.txt");

        System.out.println("pathSeparator : " + File.pathSeparator);
        System.out.println("separator : " + File.separator);
        System.out.println("separatorChar" + File.pathSeparatorChar);

        try {
            System.out.println("canRead : " + f.canRead());
            System.out.println("canWrite : " + f.canWrite());
            System.out.println("exists : " + f.exists());
            System.out.println("getName : " + f.getName());

            System.out.println("getParent : " + f.getParent());
            System.out.println("isDirectory : " + f.isDirectory());
            System.out.println("isFile : " + f.isFile());
            System.out.println("length : " + f.length());

        } catch (Exception e) {
            System.out.println(e);
        }
        */

         
        try {
            File archivo = new File("Numeros.txt");
            if (archivo.createNewFile()){
                System.out.println("Archivo creado: " + archivo.getName());
            } else {
                System.out.println("El archivo ya existe");
            }
            
        } catch (Exception e) {
            System.out.println("Errores encontrados: ");
            e.printStackTrace();
        }
        


        /*
        // Convertir el String a byte array
        String s = "Grupo 37";

        byte datos[] = s.getBytes();

        Path p = Paths.get("./prueba2.txt");

        // Un archivo bytes a bytes desde el BufferedOutputStream quien los convierte a caracteres a bytes
        try (OutputStream outt = new BufferedOutputStream(
            // anexar a un archivo exstente, crear un archivo si no existe inicialmente
            Files.newOutputStream(p, CREATE, APPEND))){
                outt.write(datos,0, datos.length);
                System.out.print("Archivo creado");

        } catch (Exception e) {
            System.err.println(e);
        }
        */



        int[][] numeros = { { 1, 2, 3, 4, 5},{ 6, 7, 8, 9, 10},{11, 12, 13, 14, 15},
                            {16, 17, 18, 19, 20},{21, 22, 23, 24, 25} };

        var nombreArchivo = "Numeros.txt";


        try {
            var salida = new PrintWriter(nombreArchivo);

            for (int i = 0; i < numeros.length; i++){
                for(int j = 0; j < numeros[i].length; j++){
                    salida.print(numeros[i][j] + ",");
                }
                salida.println("");
            }
            salida.close();
            
        } catch (Exception e) {
            e.printStackTrace();
        }


        


        

        


    }
}
