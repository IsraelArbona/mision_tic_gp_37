package co.edu.utp.misiontic2022.c2;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import co.edu.utp.misiontic2022.c2.model.Employee;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        
        /* 
        String direccionDB = "C://Users/israelarbonaguerrero/Desktop/RUTA2_MISIONTIC_2022/grupo_37/ciclo_2/semana3/db/hr.db";

        String url = "jdbc:sqlite:" + direccionDB;
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        try {
            conn = DriverManager.getConnection(url);
            stmt = conn.createStatement();
            String sql = "SELECT e.employee_id, e.first_name, e.last_name, e.email FROM employees AS e";

            rs = stmt.executeQuery(sql);

            while(rs.next()){
                int id = rs.getInt("employee_id");
                String nombre = rs.getString("first_name");
                String apellido = rs.getString("last_name");
                String email = rs.getString("email");

                System.out.println("(" + id + ") " + nombre + " " + apellido + " \t\t-- " + email);
            }

        } catch (Exception e) {
            System.out.println("Error de conexión : " + e);
        }

        */

        String direccionDB = "C://Users/israelarbonaguerrero/Desktop/RUTA2_MISIONTIC_2022/grupo_37/ciclo_2/semana3/db/hr.db";

        String url = "jdbc:sqlite:" + direccionDB;
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        var listaEmployee = new ArrayList<Employee>();

        try {
            conn = DriverManager.getConnection(url);
            stmt = conn.createStatement();
            String sql = "SELECT e.employee_id, e.first_name, e.last_name, e.email FROM employees AS e";
            rs = stmt.executeQuery(sql);

            while (rs.next()) {
                Employee emp = new Employee();

                int id = rs.getInt("employee_id");
                String nombre = rs.getString("first_name");
                String apellido = rs.getString("last_name");
                String email = rs.getString("email");

                Employee emp2 = new Employee(
                    rs.getInt("employee_id"),
                    rs.getString("first_name"),
                    rs.getString("last_name"),
                    rs.getString("email")
                );

                emp.setEmployee_id(id);
                emp.setFirst_name(nombre);
                emp.setLast_name(apellido);
                emp.setEmail(email);
                
                listaEmployee.add(emp);
                
            }
            
        } catch (Exception e) {
           System.out.print("Error de conexión " + e);
        } finally {
            try {
                if (rs != null){
                    rs.close();
                }
                if (stmt != null){
                    stmt.close();
                }
                if (conn != null){
                    conn.close();
                }
            } catch (SQLException e) {
                
                e.printStackTrace();
            }
        }


        for (Employee le: listaEmployee){
            System.out.println(le.getEmail());
        }

    }
}
