package co.edu.utp.misiontic2022.c2.model;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "Estudiante")
public class Estudiante implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;

    @Column(name = "nombre", columnDefinition = "VARCHAR(50)", nullable = false)
    private String nombre;

    @Column(name = "apellidos", columnDefinition = "VARCHAR(80)")
    private String apellidos;
    @Column(name = "contacto", columnDefinition = "VARCHAR(30)")
    private String contacto;

    public Estudiante(){

    }

    public Estudiante(Integer id, String nombre, String apellidos, String contacto) {
        this.id = id;
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.contacto = contacto;
    }
    
}
