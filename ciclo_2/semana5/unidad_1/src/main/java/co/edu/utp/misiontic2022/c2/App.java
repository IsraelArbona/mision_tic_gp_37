package co.edu.utp.misiontic2022.c2;

import javax.swing.*;

/**
 * Swing
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        JFrame marco = new JFrame(); // Creamos una instancia de jframe

        JButton boton = new JButton("Click"); // Creamos una instancia de jbutton
        boton.setBounds(130, 100, 100, 40); // x axis, y axis, width, height

        marco.add(boton); // agregamos el boton dentro del Jframe

        marco.setSize(400, 500); // 400 de width y 500 de height
        marco.setLayout(null); // se asigna null
        marco.setVisible(true); // volver visible el jframe
    }
}
