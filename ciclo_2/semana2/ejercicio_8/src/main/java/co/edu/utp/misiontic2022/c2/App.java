package co.edu.utp.misiontic2022.c2;

import java.util.HashMap;
import java.util.Map;

/**
 * Map
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        HashMap<Integer, String> m = new HashMap<>();

        // añadir elementos
        m.put(924, "Juan Diaz");
        m.put(921, "Juliana Martinez");
        m.put(700, "Maria Guerra");
        m.put(219, "Jorge Brito");
        m.put(537,"Alan Marquez");
        m.put(605, "Esteban Quito");
        m.put(921,"Clara Muñoz");


        System.out.println("Tamaño del mapa: " + m.size());

        System.out.println(m.get(921));
        System.out.println(m.get(605));
        System.out.println(m.get(900));

        System.out.println("Los elementos de m es: " + m);

        System.out.println("Todos los elementos de m extraidos con entrySet: " + m.entrySet());

        for(Map.Entry pareja: m.entrySet()){
            System.out.println(pareja);
        }
    }
}
