
package testui;

import java.awt.Image;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.ImageIcon;
import javax.swing.JLabel;


public class fabricaHumano implements fabricaAbs{
    @Override
    public JLabel dibujo() {
        JLabel dibujo = new JLabel();
        dibujo.setSize(150, 150);
        ImageIcon icono = new ImageIcon("hombre.jpg");
        Image imagen = icono.getImage();
        imagen = imagen.getScaledInstance(dibujo.getWidth(), dibujo.getHeight(),  java.awt.Image.SCALE_SMOOTH);
        icono = new ImageIcon(imagen);
        //dibujo.setOpaque(true);
        dibujo.setIcon(icono);
        return dibujo;
    }

    @Override
    public armaduraPecho colocarArmPecho() {
        return new armaduraPechoHumano();
    }

    @Override
    public armaduraPantalon colocarArmPantalon() {
        return new armaduraPantalonHumano();
    }

    @Override
    public armaduraBotas colocarArmBotas() {
        return new armaduraBotasHumano();
    }

    @Override
    public String colocarDescripcion() {
        return "La raza de los hombres se refiere a la humanidad en su conjunto y no denota el género en sí. Por tanto, también puede usarse el término para referirse a las mujeres de esta raza. Los hombres son los Hijos Menores de Ilúvatar y fueron conocidos por muchos nombres entre los Eldar o elfos, entre ellos: Hildor los Seguidores, Apanónar los Nacidos Después, Engwar los Enfermizos, y Fírimar los Mortales además los llamaron también los Usurpadores, los Forasteros e Inescrutables, los Malditos, los de Mano Torpe, los Temerosos de la Noche y los Hijos del Sol.";
    }

    @Override
    public fabricaAbs hacerCopia() {
        fabricaHumano fabricaObjeto = null;
        try {
            fabricaObjeto = (fabricaHumano) super.clone();
        } catch (CloneNotSupportedException ex) {
            Logger.getLogger(fabricaElfo.class.getName()).log(Level.SEVERE, null, ex);
        }
        return fabricaObjeto;        
    }
}
