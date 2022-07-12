/**
 * Colas en Java con Queue: en java podemos encontrar variedas formas de crear Colas,
 * un ejemplo es una de sus interfaces que tiene como nombre "Queue".
 * 
 * los metodos
 * 
 * Para Insertar
 * - add(e)
 * - offer(e)
 * 
 * Para Extraer
 * - remove()
 * - poll()
 * 
 * Para consultar el frente:
 * - element()
 * - peek()
 */

package co.edu.utp.misiontic2022.c2;

import java.util.LinkedList;
import java.util.Queue;

public class App 
{
    public static void main( String[] args )
    {
        // Creamo la Cola indicando el tipo de dato
        Queue<Integer> cola = new LinkedList<>();

        // insertar datos
        cola.offer(3);      // inserta un elemento(mejor método)
        cola.add(14);       // inserta otro elemento (lanza excepciones)
        cola.offer(12);
        cola.add(7);
        cola.offer(10);

        // impresión de la Cola llena de datos
        System.out.println("Cola llena : " + cola);

        // Estructura repetitiva para desencolar
        while(cola.poll() != null){   // Recupera el primer elemento, si es null = vacio
            System.out.println(cola.peek()); // muestra el primer elemento de la cola
        }

        // Muestra null debido a que la cola ya esta vacia
        System.out.println(cola.peek());
    }
}
