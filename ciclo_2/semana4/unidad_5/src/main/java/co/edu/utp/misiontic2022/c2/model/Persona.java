package co.edu.utp.misiontic2022.c2.model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "Persona")
public class Persona {

    @Id
    private String nombre;
    private Integer edad;

    public String getNombre() {
        return nombre;
    }

    public Persona(String nombre, Integer edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Integer getEdad() {
        return edad;
    }

    public void setEdad(Integer edad) {
        this.edad = edad;
    }

    public Persona(){

    }

    @Override
    public String toString(){
        return this.nombre + " " + this.edad;
    }
    
}
