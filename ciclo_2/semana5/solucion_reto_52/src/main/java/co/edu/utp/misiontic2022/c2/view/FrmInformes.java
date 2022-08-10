/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package co.edu.utp.misiontic2022.c2.view;

import co.edu.utp.misiontic2022.c2.controller.RequerimientoController;
import co.edu.utp.misiontic2022.c2.model.vo.AsesorPorCiudadVo;
import java.sql.SQLException;
import java.util.ArrayList;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author israelarbonaguerrero
 */
public class FrmInformes extends javax.swing.JFrame {

    /**
     * Creates new form FrmInformes
     */
    public FrmInformes() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        btnInforme1 = new javax.swing.JButton();
        btnInforme2 = new javax.swing.JButton();
        btnInforme3 = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        miTabla = new javax.swing.JTable();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        btnInforme1.setText("Informe 1");
        btnInforme1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnInforme1ActionPerformed(evt);
            }
        });

        btnInforme2.setText("Informe 2");

        btnInforme3.setText("Informe 3");

        miTabla.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {

            },
            new String [] {

            }
        ));
        jScrollPane1.setViewportView(miTabla);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(25, 25, 25)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 592, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(btnInforme1)
                        .addGap(18, 18, 18)
                        .addComponent(btnInforme2)
                        .addGap(18, 18, 18)
                        .addComponent(btnInforme3)))
                .addContainerGap(27, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnInforme1)
                    .addComponent(btnInforme2)
                    .addComponent(btnInforme3))
                .addGap(18, 18, 18)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 507, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(28, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnInforme1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnInforme1ActionPerformed
           
        String[] columnNombre = {"Id Lider","Nombre", "Primer Apellido", "Residencia"};
        
        RequerimientoController controlador = new RequerimientoController();
        
        ArrayList<AsesorPorCiudadVo> listaA;
        
        try {
            listaA = controlador.consultarAsesorPorCiudad();
            Object[][] datos = new Object[listaA.size()][4];
            
            int index = 0;
            for (AsesorPorCiudadVo lista: listaA){
                datos[index][0] = lista.getIdLider();
                datos[index][1] = lista.getNombre();
                datos[index][2] = lista.getPrimerApellido();
                datos[index][3] = lista.getCiudadResidencia();
                index++;
            }
            
            DefaultTableModel model = new DefaultTableModel(datos,columnNombre);
            miTabla.setModel(model);
            
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
        
    }//GEN-LAST:event_btnInforme1ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(FrmInformes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(FrmInformes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(FrmInformes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(FrmInformes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new FrmInformes().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnInforme1;
    private javax.swing.JButton btnInforme2;
    private javax.swing.JButton btnInforme3;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTable miTabla;
    // End of variables declaration//GEN-END:variables
}