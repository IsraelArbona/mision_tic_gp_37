package co.edu.utp.misiontic2022.c2.model.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import co.edu.utp.misiontic2022.c2.model.vo.ProyectoBancoVo;
import co.edu.utp.misiontic2022.c2.util.JDBCUtilities;

public class ProyectoBancoDao {

    public List<ProyectoBancoVo> listar(String banco) throws SQLException {

        ArrayList<ProyectoBancoVo> respuesta = new ArrayList<ProyectoBancoVo>();
        Connection conn = JDBCUtilities.getConnection();
        PreparedStatement stmt = null;
        ResultSet rs = null;

        String sql = "SELECT p.ID_Proyecto AS ID, p.Constructora, p.Ciudad, p.Clasificacion, " +
                          "t.Estrato, l.Nombre || ' ' || l.Primer_Apellido || ' ' || l.Segundo_Apellido AS LIDER " +
                          "FROM Proyecto p " +
                          "JOIN Tipo t ON (p.ID_Tipo = t.ID_Tipo) " +
                          "JOIN Lider l ON (p.ID_Lider = l.ID_Lider) " +
                          "WHERE p.Banco_Vinculado = ? " +
                          "ORDER BY p.Fecha_Inicio DESC, p.Ciudad, p.Constructora;";
        
        try {
            stmt = conn.prepareStatement(sql);
            stmt.setString(1, banco);
            rs = stmt.executeQuery();

            while (rs.next()) {
                ProyectoBancoVo proyectoBancoVo = new ProyectoBancoVo();

                proyectoBancoVo.setId(rs.getInt("ID"));
                proyectoBancoVo.setConstructora(rs.getString("Constructora"));
                proyectoBancoVo.setCiudad(rs.getString("Ciudad"));
                proyectoBancoVo.setClasificacion(rs.getString("Clasificacion"));
                proyectoBancoVo.setEstrato(rs.getInt("Estrato"));
                proyectoBancoVo.setLider(rs.getString("LIDER"));

                respuesta.add(proyectoBancoVo);
            }
            
        } finally {
            if (rs != null){
                rs.close();
            }
            if (stmt != null){
                stmt.close();
            }
            if (conn != null){
                conn.close();
            }
        }

        return respuesta;
    }
    
}
