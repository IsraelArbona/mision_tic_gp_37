package co.edu.utp.misiontic2022.c2;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
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

    }
}
