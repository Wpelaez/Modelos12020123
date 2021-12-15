
package testui;

import javax.swing.JLabel;


public interface fabricaAbs extends Cloneable{
    
    public JLabel dibujo();
    
    public String colocarDescripcion();

    public armaduraPecho colocarArmPecho();

    public armaduraPantalon colocarArmPantalon();

    public armaduraBotas colocarArmBotas();
    
    public fabricaAbs hacerCopia();
 
}


