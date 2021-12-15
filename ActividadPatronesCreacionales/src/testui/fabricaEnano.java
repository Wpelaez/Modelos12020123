
package testui;

import java.awt.Image;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.ImageIcon;
import javax.swing.JLabel;

public class fabricaEnano implements fabricaAbs{
    @Override
    public JLabel dibujo() {
        JLabel dibujo = new JLabel();
        dibujo.setSize(150, 150);
        ImageIcon icono = new ImageIcon("enano.jpg");
        Image imagen = icono.getImage();
        imagen = imagen.getScaledInstance(dibujo.getWidth(), dibujo.getHeight(),  java.awt.Image.SCALE_SMOOTH);
        icono = new ImageIcon(imagen);
        //dibujo.setOpaque(true);
        dibujo.setIcon(icono);
        return dibujo;
    }

    @Override
    public armaduraPecho colocarArmPecho() {
        return new armaduraPechoEnano();
    }

    @Override
    public armaduraPantalon colocarArmPantalon() {
        return new armaduraPantalonEnano();
    }

    @Override
    public armaduraBotas colocarArmBotas() {
        return new armaduraBotasEnano();
    }

    @Override
    public String colocarDescripcion() {
        return "Como su nombre indica, son más bajos que los hombres con una altura de entre 120 y 150 centímetros, pese a ello son robustos, corpulentos y más fuertes y recios que el resto de las razas. Todos tienen barba, tanto hombres como mujeres, y el cortársela es la mayor vergüenza y ofensa que se les que les puede hacer, mereciendo el odio y rencor de toda su raza. Son grandes conocedores de la minería y orfebrería agobiados por la larga labor de la busqueda y extracción de los minerales subterraneos. Poseen una gran longevidad, llegando algunos a vivir alrededor de los 600 años.";
    }

    @Override
    public fabricaAbs hacerCopia() {
        fabricaEnano fabricaObjeto = null;
        try {
            fabricaObjeto = (fabricaEnano) super.clone();
        } catch (CloneNotSupportedException ex) {
            Logger.getLogger(fabricaElfo.class.getName()).log(Level.SEVERE, null, ex);
        }
        return fabricaObjeto;         
    }
}
