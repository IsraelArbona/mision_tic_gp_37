package co.edu.utp.misiontic2022.c2;

/**
 * Interfases
 * 
 * Define métodos sin cuerpo
 * Implementados por subclases
 * 
 * <(modificador) "public" o "default"> interface <nombre> (<tipo parametro>)
 * 
 * Donde
 *      public: para todos los paquetes.
 *      default: No se coloca y solo es visto desde otros miembros del mismo paquete.
 * 
 * Las variables declarada en una interfaz no son variable de instancia. En cambio, 
 * son implícitamente public, final y static y deben inicializadas.
 * por lo tanto, son esencialemte constantes.
 */


public interface Series {
    
    int getSiguiente();         // retorna el siguente número de la serie
    void reiniciar();           // reiniciar
    void setComenzar(int x);    // establecer un valor inicial

}
