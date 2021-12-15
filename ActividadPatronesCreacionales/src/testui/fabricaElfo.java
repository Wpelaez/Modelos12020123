
package testui;

import java.awt.Color;
import java.awt.Image;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.ImageIcon;
import javax.swing.JLabel;

public class fabricaElfo implements fabricaAbs{
    
    @Override
    public JLabel dibujo() {
        JLabel dibujo = new JLabel();
        dibujo.setSize(150, 150);
        ImageIcon icono = new ImageIcon("elfo.jpg");
        Image imagen = icono.getImage();
        imagen = imagen.getScaledInstance(dibujo.getWidth(), dibujo.getHeight(),  java.awt.Image.SCALE_SMOOTH);
        icono = new ImageIcon(imagen);
        //dibujo.setOpaque(true);
        dibujo.setIcon(icono);
        return dibujo;
    }

    @Override
    public armaduraPecho colocarArmPecho() {
        return new armaduraPechoElfo();
    }

    @Override
    public armaduraPantalon colocarArmPantalon() {
        return new armaduraPantalonElfo();
    }

    @Override
    public armaduraBotas colocarArmBotas() {
        return new armaduraBotasElfo();
    }

    @Override
    public String colocarDescripcion() {
       return "Los Elfos fueron la más antigua y noble de las razas hablantes de la Tierra Media. También llamados la Gente hermosa, Pueblo del Bosque, Primeros Nacidos, Antigua Raza y a sí mismos Quendi \"los que hablan\". Son la raza más antigua del mundo y son los primeros hijos de Eru Iluvatar en venir al mundo y más tarde encontrados por los Valar.";
    }

    @Override
    public fabricaAbs hacerCopia() {
        fabricaElfo fabricaObjeto = null;
        try {
            fabricaObjeto = (fabricaElfo) super.clone();
        } catch (CloneNotSupportedException ex) {
            Logger.getLogger(fabricaElfo.class.getName()).log(Level.SEVERE, null, ex);
        }
        return fabricaObjeto;
    }
}
