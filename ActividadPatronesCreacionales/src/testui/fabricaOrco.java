
package testui;

import java.awt.Image;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.ImageIcon;
import javax.swing.JLabel;


public class fabricaOrco implements fabricaAbs{
    @Override
    public JLabel dibujo() {
        JLabel dibujo = new JLabel();
        dibujo.setSize(150, 150);
        ImageIcon icono = new ImageIcon("orco.jpg");
        Image imagen = icono.getImage();
        imagen = imagen.getScaledInstance(dibujo.getWidth(), dibujo.getHeight(),  java.awt.Image.SCALE_SMOOTH);
        icono = new ImageIcon(imagen);
        //dibujo.setOpaque(true);
        dibujo.setIcon(icono);
        return dibujo;
    }

    @Override
    public armaduraPecho colocarArmPecho() {
        return new armaduraPechoOrco();
    }

    @Override
    public armaduraPantalon colocarArmPantalon() {
        return new armaduraPantalonOrco();
    }

    @Override
    public armaduraBotas colocarArmBotas() {
        return new armaduraBotasOrco();
    }

    @Override
    public String colocarDescripcion() {
        return "Los Orcos (Orcs en el original inglés), conocidos por los elfos de Beleriand como Glamhoth «Horda Estridente» son una raza malvada, criada por Melkor como burla de los Elfos. Son los Quendi que cayeron en la trampa de Melkor cuando Oromë los fue a buscar para guiarlos a Aman. Fueron utilizados por los Señores Oscuros como la fuerza principal de sus ejércitos, y fueron mejorados y perfeccionados a lo largo de la historia, dando lugar a diversos tipos.";
    }

    @Override
    public fabricaAbs hacerCopia() {
        fabricaOrco fabricaObjeto = null;
        try {
            fabricaObjeto = (fabricaOrco) super.clone();
        } catch (CloneNotSupportedException ex) {
            Logger.getLogger(fabricaElfo.class.getName()).log(Level.SEVERE, null, ex);
        }
        return fabricaObjeto;         
    }
}
