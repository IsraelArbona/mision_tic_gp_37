package co.edu.utp.misiontic2022.c2;

import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import co.edu.utp.misiontic2022.c2.model.Estudiante;
import co.edu.utp.misiontic2022.c2.model.Persona;


/**
 * Orm
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Inicio..... " );

        Persona persona = new Persona("Maria", 25);
        Estudiante estudiante = new Estudiante(1,"Luis","Diaz","7270000");

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("unidad5-pu");
        EntityManager em = emf.createEntityManager();

        try{
            em.getTransaction().begin();
            em.persist(persona);
            // em.persist(estudiante);
            em.getTransaction().commit();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            em.close();
        }

        disableLogging();
    }


    public static void disableLogging(){
        LogManager logManager = LogManager.getLogManager();
        Logger logger = logManager.getLogger("");
        logger.setLevel(Level.SEVERE);
    }
}
